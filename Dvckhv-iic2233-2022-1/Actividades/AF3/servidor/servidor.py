"""
Modulo contiene la implementación principal del servidor
"""
import json
import socket
import threading
from logica import Logica


class Servidor:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.socket_servidor = None
        self.conectado = False
        self.logica = Logica(self)
        self.id_cliente = 0
        self.log("".center(80, "-"))
        self.log("Inicializando servidor...")
        self.iniciar_servidor()

    def iniciar_servidor(self):
        """
        Crea el socket, lo enlaza y comienza a escuchar
        """
        self.socket_servidor=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.socket_servidor.bind((self.host,self.port))
        self.socket_servidor.listen()
        self.log(f'Servidor Escuchando...')
        self.log(f'Host: {self.host}  Puerto: {self.port}')
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
                self.id_cliente+=1
                thread_cliente = threading.Thread(target=self.escuchar_cliente, args=(self.id_cliente,socket_cliente), daemon=True)
                thread_cliente.start()
            except ConnectionError as error:
                print("Se generó un error de conexión:",error)

    def escuchar_cliente(self, id_cliente, socket_cliente):
        """
        Ciclo encargado de escuchar a cada cliente de forma individual, esta
        funcion se ejecuta siempre que el servidor este conectado, recibe el
        socket del cliente y si hay un mensaje, lo procesa con la funcion
        instanciada en la logica.
        """
        self.log(f"Comenzando a escuchar al cliente {id_cliente}...")
        # TODO: Completado por estudiante
        try:
            while self.conectado:
                mensaje=self.recibir_mensaje(socket_cliente)
                if len(mensaje)==0:
                    raise ConnectionError("mensaje vacio")
                respuesta=self.logica.procesar_mensaje(mensaje,socket_cliente)
                if len(respuesta)!=0:
                    self.enviar_mensaje(respuesta,socket_cliente)

        except ConnectionError:
            self.eliminar_cliente(id_cliente,socket_cliente)
        


    def recibir_mensaje(self, socket_cliente):
        """
        Recibe un mensaje del cliente, lo DECODIFICA usando el protocolo
        establecido y lo des-serializa retornando un diccionario.
        """
        largo_bytes = socket_cliente.recv(4)
        largo_int = int.from_bytes(largo_bytes, byteorder='little')
        mensaje_bytes = bytearray()
        while len(mensaje_bytes) < largo_int:
            largo_restante=largo_int-len(mensaje_bytes)
            mensaje_bytes += socket_cliente.recv(min(64,largo_restante))

        mensaje_decodificado=self.decodificar_mensaje(mensaje_bytes)
        return mensaje_decodificado


    def enviar_mensaje(self, mensaje, socket_cliente):
        """
        Recibe una instruccion,
        lo CODIFICA usando el protocolo establecido y lo envía al cliente
        """
        mensaje_bytes = self.codificar_mensaje(mensaje)
        largo_bytes_mensaje = len(mensaje_bytes).to_bytes(4, byteorder='little')
        socket_cliente.send(largo_bytes_mensaje + mensaje_bytes)


    def enviar_archivo(self, socket_cliente, ruta):
        """
        Recibe una ruta a un archivo a enviar y los separa en chunks de 8 kb
        """
        with open(ruta, "rb") as archivo:
            chunk = archivo.read(8000)
            largo = len(chunk)
            while largo > 0:
                chunk = chunk.ljust(8000, b"\0")  # Padding
                msg = {
                    "comando": "chunk",
                    "argumentos": {"largo": largo, "contenido": chunk.hex()},
                    "ruta": ruta,
                }
                self.enviar_mensaje(msg, socket_cliente)
                chunk = archivo.read(8000)
                largo = len(chunk)

    def eliminar_cliente(self, id_cliente, socket_cliente):
        """
        Elimina un cliente del diccionario de clientes conectados
        """
        try:
            # Cerramos el socket
            self.log(f"Borrando socket del cliente {id_cliente}.")
            socket_cliente.close()
            # Desconectamos el usuario de la lista de jugadores
            self.logica.procesar_mensaje(
                {"comando": "desconectar", "id": id_cliente}, socket_cliente
            )

        except KeyError as e:
            self.log(f"ERROR: {e}")

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
