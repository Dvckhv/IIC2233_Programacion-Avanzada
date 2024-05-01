"""
Modulo contiene implementación principal del cliente
"""
import socket
import json
from threading import Thread
from backend.interfaz import Interfaz


class Cliente:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.socket_cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.conectado = False
        self.interfaz = Interfaz(self)
        self.iniciar_cliente()

    def iniciar_cliente(self):
        """
        Se encarga de iniciar el cliente y conectar el socket
        """
        try:
            self.socket_cliente.connect((self.host, self.port))
            self.conectado = True
            self.comenzar_a_escuchar()
            self.interfaz.mostrar_ventana_carga()

    
        except ConnectionRefusedError as error:
            self.log(error)
            self.socket_cliente.close()
            

    def comenzar_a_escuchar(self):
        """
        Instancia el Thread que escucha los mensajes del servidor
        """
        T = Thread(target=self.escuchar_servidor, daemon=True)
        T.start()

    def escuchar_servidor(self):
        """
        Recibe mensajes constantes desde el servidor y responde.
        """
        try:
            while self.conectado:
                mensaje=self.recibir()
                if len(mensaje)!=0:
                    self.interfaz.manejar_mensaje(mensaje)
        
        except ConnectionError as error:
            self.log(error)
            pass
            

    def recibir(self):
        """
        Se encarga de recibir lis mensajes del servidor.
        """
        largo_bytes = self.socket_cliente.recv(4)
        largo_int = int.from_bytes(largo_bytes, byteorder='little')
        mensaje_bytes = bytearray()
        while len(mensaje_bytes) < largo_int:
            largo_restante=largo_int-len(mensaje_bytes)
            mensaje_bytes += self.socket_cliente.recv(min(64,largo_restante))
        
        mensaje_decodificado=self.decodificar_mensaje(mensaje_bytes)
        return mensaje_decodificado

    def enviar(self, mensaje):
        """
        Envía un mensaje a un cliente.
        """
        mensaje_bytes = self.codificar_mensaje(mensaje)
        largo_bytes_mensaje = len(mensaje_bytes).to_bytes(4, byteorder='little')
        self.socket_cliente.send(largo_bytes_mensaje + mensaje_bytes)

    def codificar_mensaje(self, mensaje):
        """
        Codifica el mensaje a enviar
        """
        try:
            mensaje_cod=json.dumps(mensaje)
            return mensaje_cod.encode()
        except json.JSONDecodeError:
            print("ERROR: No se pudo codificar el mensaje")
            return b""

    def decodificar_mensaje(self, mensaje_bytes):
        """
        Decodifica el mensaje del servidor
        """
        try:
            mensaje_dec=json.loads(mensaje_bytes)
            return mensaje_dec
        except json.JSONDecodeError:
            print("ERROR: No se pudo decodificar el mensaje")
            return {}
    def log(self, mensaje: str):
        """
        Imprime un mensaje en consola
        """
        print("|" + mensaje.center(80, " ") + "|")

