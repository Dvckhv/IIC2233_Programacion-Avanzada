from Casino import Casino
from ConexionMenus import menu_inicio, opciones_jugador
from archivos import eleccion

jugador = menu_inicio()
if jugador == True:
    print("¡Hasta la proxima!")
else:
    casino = Casino(jugador)
    casino.jugar()  # empieza el juego
