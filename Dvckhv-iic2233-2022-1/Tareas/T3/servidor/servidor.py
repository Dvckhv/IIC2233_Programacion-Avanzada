import json
import socket
import threading
from logica import Logica
from utils import log,codificar_mensaje,decodificar_mensaje,data_json,desencriptar_mensaje,encriptar_mensaje


class Servidor:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.socket_servidor = None
        self.conectado = False
        self.logica = Logica(self)
        self.jugadores=dict()
        log("".center(80, "-"))
        log("Inicializando servidor...")
        self.iniciar_servidor()

    def iniciar_servidor(self):
        """
        Crea el socket, lo enlaza y comienza a escuchar
        """
        self.socket_servidor=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.socket_servidor.bind((self.host,self.port))
        self.socket_servidor.listen()
        log(f'Servidor Escuchando...')
        log(f'Host: {self.host}  Puerto: {self.port}')
        self.conectado = True
        self.comenzar_a_aceptar()
        

    def comenzar_a_aceptar(self):
        """
        Crea y comienza el thread encargado de aceptar clientes
        """
        T=threading.Thread(target=self.aceptar_clientes,daemon=True)
        T.start()
        

    def aceptar_clientes(self):
        """
        Es arrancado como thread para de aceptar clientes, este se ejecuta
        siempre que se este conectado y acepta el socket del servidor. Luego
        se crea y comienza a escuchar al cliente. para finalmente aumentar en 1
        el id_cliente.
        """
        while self.conectado:
            try:
                socket_cliente, address = self.socket_servidor.accept()
                thread_cliente = threading.Thread(target=self.escuchar_cliente, args=(socket_cliente,), daemon=True)
                thread_cliente.start()
            except ConnectionError as error:
                print("Se generó un error de conexión:",error)

    def escuchar_cliente(self, socket_cliente):
        """
        Ciclo encargado de escuchar a cada cliente de forma individual, esta
        funcion se ejecuta siempre que el servidor este conectado, recibe el
        socket del cliente y si hay un mensaje, lo procesa con la funcion
        instanciada en la logica.
        """
        log(f"Comenzando a escuchar un jugador!")
        try:
            while self.conectado:
                mensaje=self.recibir_mensaje(socket_cliente)
                if len(mensaje)==0:
                    raise ConnectionError("mensaje vacio")
                self.logica.procesar_mensaje(mensaje,socket_cliente)
                
        except ConnectionError:
            self.eliminar_cliente(socket_cliente)
        


    def recibir_mensaje(self, socket_cliente):
        """
        Recibe un mensaje del cliente, lo DECODIFICA usando el protocolo
        establecido y lo des-serializa retornando un diccionario.
        """
        bloques_b = socket_cliente.recv(4)
        bloques_int = int.from_bytes(bloques_b, byteorder='little')
        mensaje_bytes = bytearray()
       

        for i in range(bloques_int):
            bloque = socket_cliente.recv(4)
            completo=socket_cliente.recv(1)
            if int.from_bytes(completo,byteorder='little')==1:
                largo=socket_cliente.recv(1)
                mensaje_bytes+=socket_cliente.recv(20)
            else:
                largo=socket_cliente.recv(1)
                mensaje_bytes+=socket_cliente.recv(int.from_bytes(largo,byteorder='little'))
        mensaje_desencriptado=desencriptar_mensaje(mensaje_bytes)
        mensaje_decodificado=decodificar_mensaje(mensaje_desencriptado)
        return mensaje_decodificado


    def enviar_mensaje(self, mensaje, socket_cliente):

        mensaje_bytes = codificar_mensaje(mensaje)
        mensaje_bytes = encriptar_mensaje(mensaje_bytes)
        cant_bloques=len(mensaje_bytes)//20
        if len(mensaje_bytes)%20!=0:
            cant_bloques+=1
        socket_cliente.send(cant_bloques.to_bytes(4, byteorder='little'))
        for i in range(cant_bloques):
            socket_cliente.send(i.to_bytes(4, byteorder='big'))
            bloque=mensaje_bytes[i*20:(i+1)*20]
            largo_bloque=len(bloque).to_bytes(1, byteorder='little')
            if len(bloque)==20:
                bloque_mensaje=b'\x01'+largo_bloque+bloque
            else:
                bloque_mensaje=b'\x00'+largo_bloque+bloque
            socket_cliente.send(bloque_mensaje)

    

    def enviar_broadcast(self,mensaje,sockets_clientes):
        for socket in sockets_clientes:
            self.enviar_mensaje(mensaje,socket)




    def eliminar_cliente(self, socket_cliente):
        """
        Elimina un cliente del diccionario de clientes conectados
        """
        try:
            # Cerramos el socket
            log(f"Borrando socket del cliente.")
            socket_cliente.close()
            # Desconectamos el usuario de la lista de jugadores
            self.logica.procesar_mensaje(
                {"comando": "desconectar"}, socket_cliente
            )

        except KeyError as e:
            log(f"ERROR: {e}")

