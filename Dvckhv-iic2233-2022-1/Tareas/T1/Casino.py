from random import random, choice
from parametros import DEUDA_TOTAL, DINERO_SHOW, ENERGIA_SHOW, FRUSTRACION_SHOW, PROBABILIDAD_EVENTO
from archivos import ubicacion_parametro, archivo_lista
from Bebidas import BrebajeMagico, Jugo, Gaseosa
from Juego import Juego
from ConexionMenus import menu_principal


class Casino:
    def __init__(self, jugador):
        self.jugador = jugador
        self.bebestibles = []
        self.juegos = []
        self.dinero_faltante = DEUDA_TOTAL

    def actualizar_deuda(self):
        self.dinero_faltante = DEUDA_TOTAL-self.jugador._dinero

    def generar_bebestibles(self):
        lista_bebestibles = archivo_lista("bebestibles")
        UB_NOMBRE_BEBESTIBLE = ubicacion_parametro(
            lista_bebestibles[0], "nombre")
        UB_TIPO = ubicacion_parametro(lista_bebestibles[0], "tipo")
        UB_PRECIO = ubicacion_parametro(lista_bebestibles[0], "precio")
        for bebestible in lista_bebestibles[1:]:
            if bebestible[UB_TIPO] == "Jugo":
                B = Jugo(bebestible[UB_NOMBRE_BEBESTIBLE],
                         bebestible[UB_PRECIO])
            elif bebestible[UB_TIPO] == "Gaseosa":
                B = Gaseosa(
                    bebestible[UB_NOMBRE_BEBESTIBLE], bebestible[UB_PRECIO])
            else:
                B = BrebajeMagico(
                    bebestible[UB_NOMBRE_BEBESTIBLE], bebestible[UB_PRECIO])
            self.bebestibles.append(B)

    def generar_juegos(self):
        lista_juegos = archivo_lista("juegos")
        UB_NOMBRE_JUEGO = ubicacion_parametro(lista_juegos[0], "nombre")
        UB_ESPERANZA = ubicacion_parametro(lista_juegos[0], "esperanza")
        UB_APUESTA_MIN = ubicacion_parametro(lista_juegos[0], "apuesta minima")
        UB_APUESTA_MAX = ubicacion_parametro(lista_juegos[0], "apuesta maxima")
        for juego in lista_juegos[1:]:
            juego_disp = Juego(juego[UB_NOMBRE_JUEGO], juego[UB_ESPERANZA],
                               juego[UB_APUESTA_MIN], juego[UB_APUESTA_MAX])
            self.juegos.append(juego_disp)

    def evento_especial(self):
        if random() < PROBABILIDAD_EVENTO:
            bebestible = choice(self.bebestibles)
            print("¡¡Ha ocurrido un evento especial!!")
            print(f"{self.jugador.nombre} ha recibido un {bebestible.nombre}")
            return bebestible.consumir(self.jugador)

    def show(self):
        if self.jugador.dinero > DINERO_SHOW:
            self.jugador.dinero -= DINERO_SHOW
            print('¡Se ha comprado un ticket al show!')
            print(f'se descontó {DINERO_SHOW} del dinero acumulado')
            self.jugador.energia += ENERGIA_SHOW
            self.jugador.frustracion -= FRUSTRACION_SHOW
            print(f'''
                @-_________________-@
          @-_____|                 |_____-@
           |            DCCHOW           |
    _______|_____________________________|__________
   |________________________________________________|
   |               -                -               |
   |   -       -             -                    - |
   |        ____    ______________-   ____          |
   | -  -  |    |   |  TICKETS   |   |    | -       |
   |       |    |   |{DINERO_SHOW:^12d}|   |    |         |
   |  --   |____| - |_o___oo___o_| - |____|     -   |
   | -     |    |  |     --       |  |    |         |
   |    -  |    |- | -      -     |  |    | --      |
   |_______|====|__|______________|__|====|_________|
    ''')
            print(f'{self.jugador.nombre} ha ganado {ENERGIA_SHOW} de energia')
            print(
                f'la frustración de {self.jugador.nombre} disminuyó en {FRUSTRACION_SHOW}')
        else:
            print("No tienes fondos suficientes para un ticket al show")

    def jugar(self):
        self.actualizar_deuda()  # genera deuda
        self.generar_bebestibles()  # genera lista de bebestibles disponibles
        self.generar_juegos()  # genera lista de juegos disponibles
        end = menu_principal(self)  # bool indicando termino temprano de ciclo
        while self.dinero_faltante > 0 and end != True and self.jugador.dinero > 0:
            end = menu_principal(self)
            self.actualizar_deuda()
        if self.jugador.dinero == 0:
            print("Te quedaste sin dinero para apostar")
            end = True
        if end == True:
            print("No completaste el pago de la deuda :(")
        else:
            print("LOGRASTE PAGAR LA DEUDA :)")
