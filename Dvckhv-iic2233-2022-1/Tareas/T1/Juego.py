from random import random
from parametros import CARISMA_GANAR, CONFIANZA_PERDER, EGO_GANAR, FRUSTRACION_GANAR, FRUSTRACION_PERDER


class Juego:
    def __init__(self, nombre, esperanza, a_minima, a_maxima):
        self.nombre = nombre
        self.esperanza = int(esperanza)
        self.apuesta_minima = int(a_minima)
        self.apuesta_maxima = int(a_maxima)

    def probabilidad_de_ganar(self, apuesta, favorito, prob_ganar):
        numero = apuesta-(favorito * 50) - (self.esperanza * 30)
        numero = numero/10000  # especificar formula readme
        return min(1, prob_ganar - numero)

    def entrega_resultados(self, jugador, prob_ganar, apuesta):
        favorito = int(jugador.juego_favorito == self.nombre)
        prob_ganar_juego = self.probabilidad_de_ganar(
            apuesta, favorito, prob_ganar)
        if random() < prob_ganar_juego:
            print("ganaste la apuesta!!")
            jugador.dinero += apuesta
            jugador.ego += EGO_GANAR
            jugador.carisma += CARISMA_GANAR
            jugador.frustracion -= FRUSTRACION_GANAR
            jugador.energia -= round((jugador.ego +
                                     jugador.frustracion) * 0.15)

            print(f'el dinero de {jugador.nombre} aumentó en {apuesta}')
            print(f'el ego de {jugador.nombre} aumentó en {EGO_GANAR}')
            print(f'el carisma de {jugador.nombre} aumentó en {CARISMA_GANAR}')
            print(
                f'la frustración de {jugador.nombre} disminuyó en {FRUSTRACION_GANAR}')
            return True
        else:
            print("perdiste la apuesta :(")
            jugador.frustracion += FRUSTRACION_PERDER
            jugador.confianza -= CONFIANZA_PERDER
            jugador.dinero -= apuesta
            print(f'el dinero de {jugador.nombre} disminuyó en {apuesta}')
            print(
                f'la frustración de {jugador.nombre} aumentó en {FRUSTRACION_PERDER}')
            print(
                f'la confianza de {jugador.nombre} disminuyó en {CONFIANZA_PERDER}')
            return False

    def __str__(self) -> str:
        return self.nombre
