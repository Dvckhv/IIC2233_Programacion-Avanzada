import socket
from threading import Thread
from backend.logica_gui import LogicaCliente
from utils import decodificar_mensaje, codificar_mensaje,log,encriptar_mensaje,desencriptar_mensaje    

class Cliente:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.socket_cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.conectado = False
        self.logica = LogicaCliente(self)
        
        self.iniciar_cliente()

    def iniciar_cliente(self):
        """
        Se encarga de iniciar el cliente y conectar el socket
        """
        try:
            self.socket_cliente.connect((self.host, self.port))
            self.conectado = True
            self.comenzar_a_escuchar()
            self.logica.mostrar_ventana_inicio()

    
        except ConnectionRefusedError as error:
            log(error)
            self.socket_cliente.close()
            

    def comenzar_a_escuchar(self):
        """
        Instancia el Thread que escucha los mensajes del servidor
        """
        T = Thread(target=self.escuchar_servidor, daemon=True)
        T.start()

    def escuchar_servidor(self):
       
        try:
            while self.conectado:
                mensaje=self.recibir()
                if len(mensaje)!=0:
                    self.logica.manejar_mensaje(mensaje)
        
        except ConnectionError as error:
            log(error)
            pass
    def recibir(self):
        """
        Recibe un mensaje del cliente, lo DECODIFICA usando el protocolo
        establecido y lo des-serializa retornando un diccionario.
        """
        bloques_b = self.socket_cliente.recv(4)
        bloques_int = int.from_bytes(bloques_b, byteorder='little')
        mensaje_bytes = bytearray()
       

        for i in range(bloques_int):
            bloque = self.socket_cliente.recv(4)
            completo=self.socket_cliente.recv(1)
            if int.from_bytes(completo,byteorder='little')==1:
                largo=self.socket_cliente.recv(1)
                mensaje_bytes+=self.socket_cliente.recv(20)
            else:
                largo=self.socket_cliente.recv(1)
                mensaje_bytes+=self.socket_cliente.recv(int.from_bytes(largo,byteorder='little'))
        mensaje_desencriptado=desencriptar_mensaje(mensaje_bytes)
        mensaje_decodificado=decodificar_mensaje(mensaje_desencriptado)
        return mensaje_decodificado


    def enviar(self, mensaje):

        mensaje_bytes = codificar_mensaje(mensaje)
        mensaje_bytes = encriptar_mensaje(mensaje_bytes)
        cant_bloques=len(mensaje_bytes)//20
        if len(mensaje_bytes)%20!=0:
            cant_bloques+=1
        self.socket_cliente.send(cant_bloques.to_bytes(4, byteorder='little'))
        for i in range(cant_bloques):
            self.socket_cliente.send(i.to_bytes(4, byteorder='big'))
            bloque=mensaje_bytes[i*20:(i+1)*20]
            largo_bloque=len(bloque).to_bytes(1, byteorder='little')
            if len(bloque)==20:
                bloque_mensaje=b'\x01'+largo_bloque+bloque
            else:
                bloque_mensaje=b'\x00'+largo_bloque+bloque
            self.socket_cliente.send(bloque_mensaje)
            