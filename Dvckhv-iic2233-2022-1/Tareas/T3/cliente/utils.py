"""
Modulo contiene funciones auxiliares
"""
import json
from os.path import join



def data_json(llave):
    """
    Lee parametros.json y retorna el valor del dato con la key correspondiente
    """

    ruta = join("parametros.json")
    with open(ruta, "r", encoding="UTF-8") as archivo:
        diccionario_data = json.load(archivo)
    valor = diccionario_data[llave]
    return valor

def codificar_mensaje(mensaje):
    """
    Codifica el mensaje a enviar
    """
    try:
        mensaje_cod=json.dumps(mensaje)
        return mensaje_cod.encode()
    except json.JSONDecodeError:
        print("ERROR: No se pudo codificar el mensaje")
        return b""

def decodificar_mensaje(mensaje_bytes):
    """
    Decodifica el mensaje del servidor
    """
    try:
        mensaje_dec=json.loads(mensaje_bytes)
        return mensaje_dec
    except json.JSONDecodeError:
        print("ERROR: No se pudo decodificar el mensaje")
        return {}

def log(mensaje: str):
    """
    Imprime un mensaje en consola
    """
    print("|" + mensaje.center(80, " ") + "|")


#REALIZAR ENCRIPTACION/DESENCRIPTACION
def encriptar_mensaje(mensaje):
    mensaje_encriptado=mensaje
    return mensaje_encriptado
def desencriptar_mensaje(mensaje):
    mensaje_desencriptado=mensaje
    return mensaje_desencriptado



