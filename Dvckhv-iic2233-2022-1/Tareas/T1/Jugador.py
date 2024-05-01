rom abc import ABC, abstractmethod
from random import random
from archivos import eleccion
from parametros import BONIFICACION_SUERTE_CASUAL, BONIFICACION_TACANO, PORCENTAJE_APUESTA_TACANO, DEUDA_TOTAL, MULTIPLICADOR_BONIFICACION_BEBEDOR


class Jugador(ABC):
    def __init__(self, nombre, personalidad, energia, suerte, dinero, frustracion, ego, carisma, confianza, juego_fav):
        self.nombre = nombre
        self._energia = int(energia)
        self._suerte = int(suerte)
        self._dinero = int(dinero)
        self._frustracion = int(frustracion)
        self._ego = int(ego)
        self.personalidad = personalidad
        self._confianza = int(confianza)
        self._carisma = int(carisma)
        self.juego_favorito = juego_fav
        self.juegos_jugados = []

    @property
    def energia(self):
        return self._energia

    @energia.setter
    def energia(self, valor):
        if self._energia + valor > 100:
            self._energia = 100
        elif self._energia + valor < 0:
            self._energia = 0
        else:
            self._energia = valor

    @property
    def suerte(self):
        return self._suerte

    @suerte.setter
    def suerte(self, valor):
        if self._suerte + valor > 50:
            self._suerte = 50
        elif self._suerte+valor < 0:
            self._suerte = 0
        else:
            self._suerte = valor

    @property
    def dinero(self):
        return self._dinero

    @dinero.setter
    def dinero(self, valor):
        if self._dinero + valor < 0:
            self._dinero = 0
        else:
            self._dinero = valor

    @property
    def frustracion(self):
        return self._frustracion

    @frustracion.setter
    def frustracion(self, valor):
        if self._frustracion + valor > 100:
            self._frustracion = 100
        elif self._frustracion+valor < 0:
            self._frustracion = 0
        else:
            self._frustracion = valor

    @property
    def ego(self):
        return self._ego

    @ego.setter
    def ego(self, valor):
        if self._ego + valor > 15:
            self._ego = 15
        elif self._ego+valor < 0:
            self._ego = 0
        else:
            self._ego = valor

    @property
    def confianza(self):
        return self._confianza

    @confianza.setter
    def confianza(self, valor):
        if self._confianza + valor > 30:
            self._confianza = 30
        elif self._confianza+valor < 0:
            self._confianza = 0
        else:
            self._confianza = valor

    @property
    def carisma(self):
        return self._carisma

    @carisma.setter
    def carisma(self, valor):
        if self._carisma + valor > 50:
            self._carisma = 50
        elif self._carisma+valor < 0:
            self._carisma = 0
        else:
            self._carisma = valor

    def comprar_bebestible(self, bebestible):
        if self.dinero > bebestible.precio:
            self.dinero -= bebestible.precio
            print(
                f'Bebestible comprado, se descontó {bebestible.precio} del dinero acumulado')
            if self.personalidad == "Bebedor":
                bebestible.consumir(self, MULTIPLICADOR_BONIFICACION_BEBEDOR)
                bonificacion = (MULTIPLICADOR_BONIFICACION_BEBEDOR-1)*100
                print(
                    f'Por la acción \"cliente recurrente\" se obtuvo un {bonificacion}% extra en los atributos mencionados.')
            else:
                bebestible.consumir(self)
        else:
            print("No tienes fondos suficientes para comprar el Bebestible")

    @abstractmethod
    def apostar(self, apuesta, juego):
        prob_ganar = self.probabilidad_ganar(apuesta, juego)
        self.juegos_jugados.append(juego)
        return juego.entrega_resultados(self, prob_ganar, apuesta)

    def probabilidad_ganar(self, apuesta, juego):
        favorito = int(self.juego_favorito == juego.nombre)
        prob_ganar = ((self.suerte * 15) - (apuesta * 0.4) +
                      (self.confianza * 3 * favorito) + (self.carisma * 2))
        prob_ganar = min(1, max(0, ((prob_ganar) / 1000)))
        return prob_ganar

    def __str__(self) -> str:
        estado = f'''Nombre:          {self.nombre}
Personalidad:    {self.personalidad}
Energia:         {self.energia}
Suerte:          {self.suerte}
Dinero:          {self.dinero}
Frustración:     {self.frustracion}
Ego:             {self.ego}
Carisma:         {self.carisma}
Confianza:       {self.confianza}
Juego favorito:  {self.juego_favorito}
Dinero faltante: {DEUDA_TOTAL-self._dinero}'''
        return estado


class Casual(Jugador):

    def __init__(self, nombre, personalidad, energia, suerte, dinero, frustracion, ego, carisma, confianza, juego_fav):
        super().__init__(nombre, personalidad, energia, suerte,
                         dinero, frustracion, ego, carisma, confianza, juego_fav)
        self.suerte_principiante = True

    def apostar(self, apuesta, juego):
        if self.suerte_principiante:
            self.suerte_principiante = False
            self.suerte += int(BONIFICACION_SUERTE_CASUAL)
            print(
                f'Debido a la acción \"suerte de principiante\" ganaste {int(BONIFICACION_SUERTE_CASUAL)} de suerte')
        super().apostar(apuesta, juego)


class Ludopata(Jugador):

    def __init__(self, nombre, personalidad, energia, suerte, dinero, frustracion, ego, carisma, confianza, juego_fav):
        super().__init__(nombre, personalidad, energia, suerte,
                         dinero, frustracion, ego, carisma, confianza, juego_fav)

    def apostar(self, apuesta, juego):
        resultado = super().apostar(apuesta, juego)
        print(
            f'debido a la acción \"ludopatia\" las estadisticas de {self.nombre} cambiaron... ')
        if resultado == False:
            print(
                f'debido a que {self.nombre} perdió la apuesta, su frustración aumento en 5...')
            self.frustracion += 5
        self.ego += 2
        self.suerte += 3
        print(
            f'el ego y suerte de {self.nombre} aumentaron en 2 y 3 respectivamente')


class Tacano(Jugador):

    def __init__(self, nombre, personalidad, energia, suerte, dinero, frustracion, ego, carisma, confianza, juego_fav):
        super().__init__(nombre, personalidad, energia, suerte,
                         dinero, frustracion, ego, carisma, confianza, juego_fav)

    def apostar(self, apuesta, juego):
        resultado = super().apostar(apuesta, juego)
        if apuesta < self._dinero * PORCENTAJE_APUESTA_TACANO and resultado:
            print(
                f'debido a la acción \"Tacaño extremo\" se obtuvo una bonificación de {BONIFICACION_TACANO*100}% de la apuesta')
            self.dinero += (int(BONIFICACION_TACANO*apuesta))
            print(f'{self.nombre} ganó ${int(BONIFICACION_TACANO*apuesta)} extra')


class Bebedor(Jugador):
    def __init__(self, nombre, personalidad, energia, suerte, dinero, frustracion, ego, carisma, confianza, juego_fav):
        super().__init__(nombre, personalidad, energia, suerte,
                         dinero, frustracion, ego, carisma, confianza, juego_fav)

    def apostar(self, apuesta, juego):
        super().apostar(apuesta, juego)
