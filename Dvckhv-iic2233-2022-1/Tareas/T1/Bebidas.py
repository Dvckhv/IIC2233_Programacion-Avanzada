from abc import ABC, abstractmethod
from random import randint
from parametros import MAX_ENERGIA_BEBESTIBLE, MIN_ENERGIA_BEBESTIBLE


class Bebestible(ABC):
    def __init__(self, nombre, tipo, precio):
        self.nombre = nombre
        self.tipo = tipo
        self.precio = int(precio)

    @abstractmethod
    def consumir(self, jugador, multiplicador=1):
        energia_ganada = randint(
            MIN_ENERGIA_BEBESTIBLE, MAX_ENERGIA_BEBESTIBLE)
        jugador.energia += int(energia_ganada*multiplicador)
        print(
            f'la energia de {jugador.nombre} aumentó en {int(energia_ganada*multiplicador)}')

    def __str__(self) -> str:
        return f' {self.nombre:20s}| {self.tipo:15s}| {self.precio}'


class Jugo(Bebestible):
    def __init__(self, nombre, precio, tipo="Jugo"):
        super().__init__(nombre, tipo, precio)
        self.largo = len(self.nombre)

    def consumir(self, jugador, multiplicador=1):
        super().consumir(jugador, multiplicador)
        if self.largo <= 4:
            jugador.ego += int(4*multiplicador)
            print(
                f'el ego de {jugador.nombre} aumentó en {int(4*multiplicador)}')
        elif 5 <= self.largo <= 7:
            jugador.suerte += int(7*multiplicador)
            print(
                f'la suerte de {jugador.nombre} aumentó en {int(7*multiplicador)}')
        else:
            jugador.frustracion -= int(10*multiplicador)
            jugador.ego += int(10*multiplicador)
            print(
                f'la frustración de {jugador.nombre} disminuyó en {int(10*multiplicador)}')
            print(
                f'el ego de {jugador.nombre} aumentó en {int(10*multiplicador)}')


class Gaseosa(Bebestible):
    def __init__(self, nombre, precio, tipo="Gaseosa"):
        super().__init__(nombre, tipo, precio)

    def consumir(self, jugador, multiplicador=1):
        super().consumir(jugador, multiplicador)
        if jugador.personalidad == "Tacano" or jugador.personalidad == "Ludopata":
            jugador.frustracion -= 5
            print(f'la frustración de {jugador.nombre} dismunuyó en 5')
        else:
            jugador.frustracion += int(5*multiplicador)
            print(
                f'la frustración de {jugador.nombre} aumentó en {int(5*multiplicador)}')
        jugador.ego += int(6*multiplicador)
        print(f'el ego de {jugador.nombre} aumentó en {int(6*multiplicador)}')


class BrebajeMagico(Jugo, Gaseosa):
    def __init__(self, nombre, precio, tipo="Brebaje magico"):
        super().__init__(nombre, tipo, precio)

    def consumir(self, jugador, multiplicador=1):
        super().consumir(jugador, multiplicador)
        jugador.carisma += int(5*multiplicador)
        print(
            f'el carisma de {jugador.nombre} aumentó en {int(5*multiplicador)}')
