from Jugador import Bebedor, Casual, Ludopata, Tacano
from archivos import eleccion, jugador_en_orden, archivo_lista


def menu_inicio():
    print('''
*** Menú de Inicio ***
----------------------
[1] Iniciar partida
[X] Salir    ''')
    Bool = True
    # dado que no hay opcion 0, no se utiliza eleccion()
    while Bool:
        elec = input("Indique su opción: ")
        if elec.isdigit() == False:
            if elec == "X" or elec == "x":
                Bool = False
            else:
                print("debe ingresar \"1\" o \"x\"")
        else:
            if elec == "1":
                Bool = False
            else:
                print("debe ingresar \"1\" o \"x\"")

    if elec == "1":
        return opciones_jugador()
    else:
        return True

# imprime lista con todos los jugadores disponibles en el archivo
def opciones_jugador():
    c = 0
    lista_jugadores = archivo_lista("jugadores")
    print(f'{"*** Opciones de Jugador ***": ^50s}')
    print("-"*50)
    print(f'N°    | {"Nombre":25s}| {"Personalidad":14s}|')
    for jugador in lista_jugadores[1:]:
        c += 1
        print(f'{"["+str(c)+"]":6s}| {jugador[0]:25s}: {jugador[1]:14s}|')
    print("[0] Volver")
    print("[x] Salir")
    elegido = eleccion(c)
    if elegido == 0:
        return menu_inicio()
    elif elegido == "X":
        return True
    else:
        jugador_ordenado = jugador_en_orden(elegido)
        if jugador_ordenado[1] == "Ludopata":
            Jugador = Ludopata(*jugador_ordenado)
        elif jugador_ordenado[1] == "Bebedor":
            Jugador = Bebedor(*jugador_ordenado)
        elif jugador_ordenado[1] == "Casual":
            Jugador = Casual(*jugador_ordenado)
        else:
            Jugador = Tacano(*jugador_ordenado)
    return Jugador


def menu_principal(Casino):
    print('''
   *** Menú Principal ***   
----------------------------
[1] Opciones de Juego
[2] Comprar bebestible
[3] Estado Jugador
[4] Ver el Show
[5] Lista de juegos jugados
[0] Seleccionar otro jugador
[X] Salir    ''')
    accion = eleccion(5)
    if accion == "X":
        return True
    elif accion == 0:
        return opciones_jugador()
    elif accion == 1:
        return opciones_juego(Casino)
    elif accion == 2:
        return carta_bebestibles(Casino)
    elif accion == 3:
        return estado_jugador(Casino)
    elif accion == 4:
        return Casino.show()
    elif accion == 5:
        return juegos_jugados(Casino.jugador)

# imprime juegos y revisa que se cumplan todas las condiciones para jugar
def opciones_juego(Casino):
    print('''
 *** Opciones de Juegos  ***
-----------------------------''')
    c = 0
    for juego in Casino.juegos:
        c += 1
        print(f'[{c}] {juego}')
    print("[0] Volver")
    print("[x] Salir")
    elegido = eleccion(c)
    if elegido == "X":
        return True
    elif elegido == 0:
        return menu_principal(Casino)
    else:
        # se elige un juego y no otra opción
        consumo = round(
            (Casino.jugador.energia+Casino.jugador.frustracion)*0.15)
        # condicion energia
        if Casino.jugador.energia > consumo:
            juego_elegido = Casino.juegos[elegido-1]
            print(f'Se ha elegido el juego { juego_elegido.nombre}')
            print(
                f'Rango de apuesta: {juego_elegido.apuesta_minima}, {juego_elegido.apuesta_maxima}')
            dinero_apostar = input(
                "Ingrese el dinero(entero) ha apostar o [Salir]: ")
            while dinero_apostar.isdigit() == False:
                if dinero_apostar == "Salir":
                    # en caso de que sea Salir termina el bucle
                    return opciones_juego(Casino)
                print("el valor ingresado no es un numero entero...")
                dinero_apostar = input(
                    "Ingrese el dinero(entero) ha apostar o [Salir]: ")
            dinero_apostar = int(dinero_apostar)
            if dinero_apostar <= Casino.jugador.dinero:
                # condicion dinero disponible
                if juego_elegido.apuesta_minima <= dinero_apostar <= juego_elegido.apuesta_maxima:
                    # condicion apuesta dentro del intervalo
                    Casino.jugador.apostar(dinero_apostar, juego_elegido)
                    # probabilidad de que ocurra el evento especial *despues* de apostar
                    Casino.evento_especial()
                else:
                    print(
                        f'La apuesta no se encuentra dentro del rango de apuesta de {juego_elegido.nombre}')
                    print(
                        f'Rango de apuesta de {juego_elegido.nombre}: [{juego_elegido.apuesta_minima}, {juego_elegido.apuesta_maxima}]')

            else:
                print("No tienes dinero suficiente para realizar esta apuesta x.x")
                print(f'Dinero actual: {Casino.jugador.dinero}')

        else:
            print("No posees energia suficiente para realizar una apuesta :(")
            print(f'Energia requerida: {consumo}')

# imprime la carta y revisa si se elije un bebestible
def carta_bebestibles(Casino):
    c = 0
    print(f'{"*** Bebestibles ***": ^53s}')
    print("-"*53)
    print(f'N°    | {"Nombre":20s}| {"Tipo":15s}| Precio')
    for bebestible in Casino.bebestibles:
        c += 1
        print(f'{"["+str(c)+"]":6s}|{bebestible}')
    print("[0] Volver")
    print("[x] Salir")
    posicion_bebida = eleccion(c)
    if posicion_bebida == "X":
        return True
    elif posicion_bebida != 0:
        trago = Casino.bebestibles[posicion_bebida-1]
        Casino.jugador.comprar_bebestible(trago)

# lista con los juegos jugados hasta el momento
def juegos_jugados(jugador):
    print(f'{"*** Juegos Jugados ***": ^40s}')
    print("-"*40)
    print(f'N°    | {"Nombre":20s}')
    c = 0
    if len(jugador.juegos_jugados) == 0:
        print("Aun no se ha jugado ningun juego...")
    else:
        for juego in jugador.juegos_jugados:
            c += 1
            print(f'[{c}] {juego}')
    print("-"*40)


def estado_jugador(Casino):
    print(f'{"*** Estado Jugador ***":^26s}')
    print("-"*26)
    print(Casino.jugador)
    print("-"*26)
