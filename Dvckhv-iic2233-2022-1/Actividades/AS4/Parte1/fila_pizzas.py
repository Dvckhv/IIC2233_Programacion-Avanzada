from asyncio.proactor_events import _ProactorDuplexPipeTransport
from http import client


class Cliente:
    def __init__(self, nombre):
        self.nombre = nombre
        self.siguiente = None

        pass

    def __str__(self):
        # NO MODIFICAR
        return self.nombre


class FilaPizza:
    def __init__(self):
        self.primero = None
        self.ultimo = None
        self.largo = 0
        pass

    def llega_cliente(self, cliente: Cliente):
        if self.primero is None:
            self.primero = cliente
        if self.ultimo is not None:
            self.ultimo.siguiente = cliente
        self.ultimo = cliente
        self.largo += 1

    def alguien_se_cuela(self, cliente: Cliente, posicion: int):

        if posicion == 0:
            cliente.siguiente = self.primero
            self.primero = cliente
            self.largo += 1

            if self.ultimo is None:
                self.ultimo = cliente
            return
        posicion_actual = self.primero
        for _ in range(posicion-1):
            if posicion_actual.siguiente is not None:
                posicion_actual = posicion_actual.siguiente
        cliente.siguiente = posicion_actual.siguiente
        posicion_actual.siguiente = cliente
        if cliente.siguiente is None:
            self.ultimo = cliente
        self.largo += 1

    def cliente_atendido(self):
        atender = self.primero
        if self.primero is self.ultimo:
            self.ultimo = None
        self.primero = self.primero.siguiente
        self.largo -= 1
        return atender

    def __str__(self):
        ubicacion = self.primero
        cola_actual = "Inicio -> "
        seguir = True
        while seguir:
            if ubicacion is not None:
                cola_actual += str(ubicacion)+"-> "
                ubicacion = ubicacion.siguiente
            else:
                seguir = False
                cola_actual += "Fin"
        return cola_actual


if __name__ == "__main__":
    print("\nNO DEBES EJECUTAR AQUÍ EL PROGRAMA!!!!")
    print("Ejecuta el main.py\n")
    raise(ModuleNotFoundError)
