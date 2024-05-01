from parametros import PROBABILIDAD_EVENTO, PUBLICO_EXITO, PUBLICO_INICIAL, \
                       PUBLICO_TERREMOTO, AFINIDAD_OLA_CALOR, \
                       AFINIDAD_LLUVIA, PUBLICO_OLA_CALOR
from random import random, choice


class DCConcierto:

    def __init__(self):
        self.artista_actual = ''
        self.__dia = 1
        self.line_up = []
        self.cant_publico = PUBLICO_INICIAL
        self.artistas = []
        self.prob_evento = PROBABILIDAD_EVENTO
        self.suministros = []

    @property
    def dia(self):
        return self.__dia
    @property
    def funcionando(self):
        return self.exito_del_concierto and self.dia <= 3

    @property
    def exito_del_concierto(self):
        return self.cant_publico >= PUBLICO_EXITO

    def imprimir_estado(self):
        print(f"Día: {self.__dia}\nCantidad de Personas: "
              f"{self.cant_publico}\nArtistas:")
        for artista in self.line_up:
            print(f"- {artista.nombre}")

    def ingresar_artista(self, artista):
        self.line_up.append(artista)
        print(f'Se ha ingresado un nuevo artista!!!\n{artista}')

    def asignar_lineup(self):
        self.line_up = []
        for artista in self.artistas:
            if self.dia == artista.dia_presentacion:
                self.ingresar_artista(artista)

    def nuevo_dia(self):
        if self.exito_del_concierto:
            print("Comienza un nuevo día")
            self.__dia+=1

    def ejecutar_evento(self):
        if self.prob_evento<=random():
            evento=choice(["Terremoto","Lluvia","Ola de calor"])
            if evento=="Terremoto":
                self.cant_publico-=PUBLICO_TERREMOTO
                print(f"¡Se ha disminuido el publico {PUBLICO_TERREMOTO} debido a un terremoto!")
            elif evento=="Lluvia":
                self.artista_actual._afinidad_con_publico-=AFINIDAD_LLUVIA
                print(f"La afinidad del artista con el publico a disminuido {AFINIDAD_LLUVIA} debido a la lluvia T-T")
            else:
                self.artista_actual._afinidad_con_publico-=AFINIDAD_OLA_CALOR
                print(f"La afinidad del artista con el publico a disminuido {AFINIDAD_OLA_CALOR} debido a una ola de calor 🥵")
                self.cant_publico-=PUBLICO_OLA_CALOR
                print(f"¡Se ha disminuido el publico {PUBLICO_OLA_CALOR} debido al calor!")


            

