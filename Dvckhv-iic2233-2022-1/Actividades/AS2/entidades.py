from abc import ABC, abstractmethod
from random import randint
from threading import Thread, Lock, Event, Timer
from time import sleep


class Persona(ABC, Thread):

    lock_bodega = Lock()
    lock_cola_pedidos = Lock()
    lock_pedidos_listos = Lock()

    def __init__(self, nombre):
        super().__init__()
        self.nombre = nombre
        self.disponible = True
        self.trabajando = True
        self.daemon = True

    @abstractmethod
    def run(self):
        pass


class Cocinero(Persona):

    def __init__(self, nombre, cocina):
        super().__init__(nombre)
        self.lugar_trabajo = cocina
        self.evento_plato_asignado = Event()

    def run(self):
        while self.trabajando:
            self.evento_plato_asignado.wait()
            sleep(randint(1, 3))
            self.cocinar()

    def cocinar(self):
        self.disponible = False
        plato = self.sacar_plato()
        # como no existe plato se reinicia la condicion como si nada ubiese pasado.
        #esto ocurre por que entran muchos cocineros a cocinar
        if plato == False:
            self.evento_plato_asignado.clear()
            self.disponible = True
            return
        print(f'Cocinero {self.nombre} cocinando {plato[1]}')
        bodega = self.lugar_trabajo.bodega
        recetas = self.lugar_trabajo.recetas
        self.buscar_ingredientes(plato, bodega, recetas)
        sleep(randint(1, 3))
        self.agregar_plato(plato)
        self.evento_plato_asignado.clear()
        self.disponible = True

    def sacar_plato(self):
        with self.lock_cola_pedidos:
            if len(self.lugar_trabajo.cola_pedidos) > 0:
                plato_sacado = self.lugar_trabajo.cola_pedidos.popleft()
            else:
                plato_sacado = False  # no existe pedido para entregar
        return plato_sacado

    def buscar_ingredientes(self, plato, bodega, recetas):
        # Formato de los dicts entregados:
        # bodega = {
        #     "alimento_1": int cantidad_alimento_1,
        #     "alimento_2": int cantidad_alimento_2,
        # }
        # recetas = {
        #     "nombre_plato_1": [("ingrediente_1", "cantidad_ingrediente_1"),
        #                        ("ingrediente_2", "cantidad_ingrediente_2")],
        #     "nombre_plato_2": [("ingrediente_1", "cantidad_ingrediente_1"),
        #                        ("ingrediente_2", "cantidad_ingrediente_2")]
        # }
        nombre_plato = plato[1]
        print(f'buscando ingredientes en la bodega para {nombre_plato}')
        receta_plato = recetas[nombre_plato]
        for ingrediente in receta_plato:
            if ingrediente[0] in receta_plato:
                with self.lock_bodega:
                    cantidad = bodega[ingrediente[0]]
                    cantidad -= int(ingrediente[1])
                    bodega[ingrediente[0]] = cantidad

    def agregar_plato(self, plato):
        with self.lock_pedidos_listos:
            self.lugar_trabajo.cola_pedidos_listos.append(plato)


class Mesero(Persona):

    def __init__(self, nombre):
        super().__init__(nombre)
        self.evento_manejar_pedido = Event()

    def run(self):
        while self.trabajando:
            if self.disponible:
                self.evento_manejar_pedido.set()

    def agregar_pedido(self, pedido, cocina):
        self.evento_manejar_pedido.clear()
        sleep(randint(1, 2))
        with self.lock_cola_pedidos:
            cocina.cola_pedidos.append(pedido)
        self.evento_manejar_pedido.set()

    def entregar_pedido(self, cocina):
        self.evento_manejar_pedido.clear()
        with self.lock_pedidos_listos:
            if len(cocina.cola_pedidos_listos) > 0:
                pedido_a_entregar = cocina.cola_pedidos_listos.popleft()
            else:
                # ya que no hay pedido debido a que entran muchos meseros se debe reiniciar el evento como si se ubiese entregado.
                self.evento_manejar_pedido.set()
                return
        print(
            f'{self.nombre} está entregando {pedido_a_entregar[1]} a la mesa {pedido_a_entregar[0]}')
        sleep(randint(1, 3))
        self.pedido_entregado(pedido_a_entregar)

    def pedido_entregado(self, pedido):
        print(
            f'{self.nombre} entrego el plato {pedido[1]} a la mesa {pedido[0]}')
        self.evento_manejar_pedido.set()
