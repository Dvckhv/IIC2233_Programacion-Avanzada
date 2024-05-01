from random import choice, randint
from time import sleep
from PyQt5.QtCore import QObject, pyqtSignal, QThread, QTimer

import parametros as p


class Mira(QObject):
    senal_movimiento_mira = pyqtSignal(tuple)

    def __init__(self, max_x, max_y) -> None:
        super().__init__()
        self.centro = (p.ANCHO_MIRA/2, p.ALTO_MIRA/2)
        self._x = max_x/2-self.centro[0]
        self._y = max_y/2-self.centro[1]
        self.max_x = max_x
        self.max_y = max_y

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, value):
        if -self.centro[0] <= value <= self.max_x-self.centro[0]:
            self._x = value
        elif value <= -self.centro[0]:
            self._x = -self.centro[0]
        else:
            self._x = self.max_x-self.centro[0]

    @property
    def y(self):
        return self._y

    @y.setter
    def y(self, value):
        if (-self.centro[1]) < value < (self.max_y-self.centro[1]):
            self._y = value
        elif value <= -self.centro[1]:
            self._y = -self.centro[1]
        else:
            self._y = (self.max_y-self.centro[1])

    def cambio_nivel(self, balas):
        self.balas_restantes = balas
        self._x = self.max_x/2-self.centro[0]
        self._y = self.max_y/2-self.centro[1]


class Aliens(QThread):
    numero_alien = 0

    def __init__(self, max_x, max_y, velocidad, senal_morir, ancho, alto):

        super().__init__()
        self.numero_alien = Aliens.numero_alien
        Aliens.numero_alien += 1
        self.max_x = max_x
        self.max_y = max_y
        self._x = randint(0, self.max_x)
        self._y = randint(0, self.max_y)
        self.velocidad = velocidad
        self.vivo = True
        self.seguir = False
        self.dir_x = choice((-1, 1))
        self.dir_y = choice((-1, 1))
        self.senal_morir = senal_morir
        self.ancho = ancho
        self.alto = alto
        self.congelado = False

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, value):
        if 0 <= value <= self.max_x-self.ancho:
            self._x = value
        elif value <= 0:
            self._x = 0
            self.dir_x *= -1
        else:
            self._x = self.max_x-self.ancho
            self.dir_x *= -1

    @property
    def y(self):
        return self._y

    @y.setter
    def y(self, value):
        if 0 <= value <= self.max_y-self.alto:
            self._y = value
        elif value <= 0:
            self._y = 0
            self.dir_y *= -1
        else:
            self._y = self.max_y-self.alto
            self.dir_y *= -1

    def moverse(self):
        if not(self.congelado):
            self.x += self.dir_x*self.velocidad[0]
            self.y += self.dir_y*self.velocidad[1]

    def morir(self):
        self.vivo = False
        self.senal_morir.emit(self.numero_alien)

    def run(self) -> None:
        self.seguir = True
        while self.vivo:
            self.moverse()
            sleep(0.1)
        while self._y < (self.max_y + p.ALTO_MENU):
            self._y += self.velocidad[1]
            sleep(0.1)
        self.seguir = False


class Estrella(QObject):
    def __init__(self, senal_mostrar):
        super().__init__()
        self.activo = False
        self.senal_mostrar = senal_mostrar
        self.x = None
        self.y = None
        self.ancho = 99
        self.alto = 100

    def apagar(self):
        if self.activo:
            self.senal_mostrar.emit((self.x, self.y, self.ancho, self.alto))
            self.activo = False

    def activar(self):
        self.activo = True
        self.senal_mostrar.emit((self.x, self.y, self.ancho, self.alto))


class Bomba(QObject):
    def __init__(self, senal_mostrar):
        super().__init__()
        self.activo = False
        self.senal_mostrar = senal_mostrar
        self.x = None
        self.y = None
        self.ancho = 95
        self.alto = 100

    def apagar(self):
        if self.activo:
            self.senal_mostrar.emit((self.x, self.y, self.ancho, self.alto))
            self.activo = False

    def activar(self):
        self.activo = True
        self.senal_mostrar.emit((self.x, self.y, self.ancho, self.alto))


class Bala(QObject):
    def __init__(self, senal_mostrar):
        super().__init__()
        self.activo = False
        self.senal_mostrar = senal_mostrar
        self.x = None
        self.y = None
        self.ancho = 50
        self.alto = 100
        self.usado = False

    def apagar(self):
        if self.activo:
            self.senal_mostrar.emit((self.x, self.y, self.ancho, self.alto))
            self.activo = False

    def activar(self):
        self.activo = True
        self.senal_mostrar.emit((self.x, self.y, self.ancho, self.alto))


class SecuenciasImagen(QThread):
    def __init__(self, lista_rutas, senal) -> None:
        self.senal = senal
        self.lista_rutas = lista_rutas
        super().__init__()

    def run(self) -> None:
        for ruta_imagen in self.lista_rutas:
            lista = [ruta_imagen]
            self.senal.emit(lista)
            sleep(0.5)
