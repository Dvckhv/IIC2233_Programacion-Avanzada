from collections import deque
from entidades import Cocinero, Mesero
from time import sleep
from random import randint


class Cocina:

    def __init__(self, bodega, recetas):
        super().__init__()
        self.cola_pedidos = deque()
        self.cola_pedidos_listos = deque()
        self.cocineros = []
        self.meseros = []
        self.bodega = bodega
        self.recetas = recetas
        self.abierta = True

    def initialize_threads(self):
        for cocinero in self.cocineros:
            cocinero.start()
        for mesero in self.meseros:
            mesero.start()
#ambas funciones asignar se encuentran mal definidas en el enunciado y generan que muchos cocineros y meseros entren cuando hay minimo 1 plato.
    def asignar_cocinero(self): 
        while self.abierta:
            sleep(1)
            for cocinero in self.cocineros:
                if cocinero.disponible and len(self.cola_pedidos) > 0:
                    cocinero.evento_plato_asignado.set()

    def asignar_mesero(self):
        while self.abierta:
            sleep(1)
            for mesero in self.meseros:
                if mesero.disponible and len(self.cola_pedidos_listos) > 0:
                    mesero.evento_manejar_pedido.set()
                    mesero.entregar_pedido(self)
        self.finalizar_jornada_laboral()

    def finalizar_jornada_laboral(self):
        for mesero in self.meseros:
            mesero.trabajando = False

        for cocinero in self.cocineros:
            cocinero.trabajando = False
