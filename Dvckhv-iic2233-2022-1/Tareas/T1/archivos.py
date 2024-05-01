# se transforma un archivo ".csv" a una lista de listas dada la recurrencia en el uso de ellas
def archivo_lista(archivo):
    with open(archivo+".csv", encoding="utf-8") as file:
        lista_archivo = []
        for linea in file:
            lista_archivo.append(linea.strip())
        if archivo == "reclamos":
            lista_archivo = [i.split(",", maxsplit=2) for i in lista_archivo]
        else:
            lista_archivo = [i.split(",") for i in lista_archivo]
    return lista_archivo

# se agrega la lista de texto al final de un archivo especificado separado por comas
def agregar_texto(lista_texto, archivo):
    with open(archivo+".csv", "r", encoding="utf-8") as file:
        nueva_linea = False
        if file.readlines()[-1][-1] == "\n":
            nueva_linea = True
    with open(archivo+".csv", "a", encoding="utf-8")as file:
        if nueva_linea == False:
            print("", file=file)
        print(",".join(lista_texto), file=file)

# funcion encargada de retornar un numero dentro de un rango, se evita fallos del codigo.
def eleccion(maximo):
    elec = input("Indique su opción: ")
    if elec.isdigit() == False:
        if elec == "X" or elec == "x":
            return "X"
        print("debe ingresar un numero o \"x\"")
        return eleccion(maximo)
    int_elec = int(elec)
    float_elec = float(elec)
    if float_elec-int_elec > 0:
        print(f"debe ser un numero entero entre 0 y {maximo} o \"x\"")
        return eleccion(maximo)
    if int_elec > maximo or int_elec < 0:
        print("opcion fuera de rango, intente nuevamente...")
        return eleccion(maximo)
    else:
        return int_elec

# busca la ubicacion de un parametro dado en el header
def ubicacion_parametro(lista, parametro):
    for i in range(len(lista)):
        if lista[i] == parametro:
            return i

# crea una lista con los datos de el jugador en la posicion especificada
def jugador_en_orden(posicion):
    lista_jugadores = archivo_lista("jugadores")
    UB_PERSONALIDAD = ubicacion_parametro(lista_jugadores[0], "personalidad")
    UB_NOMBRE_JUGADOR = ubicacion_parametro(lista_jugadores[0], "nombre")
    UB_ENERGIA = ubicacion_parametro(lista_jugadores[0], "energia")
    UB_SUERTE = ubicacion_parametro(lista_jugadores[0], "suerte")
    UB_DINERO = ubicacion_parametro(lista_jugadores[0], "dinero")
    UB_FRUSTRACION = ubicacion_parametro(lista_jugadores[0], "frustracion")
    UB_EGO = ubicacion_parametro(lista_jugadores[0], "ego")
    UB_CARISMA = ubicacion_parametro(lista_jugadores[0], "carisma")
    UB_CONFIANZA = ubicacion_parametro(lista_jugadores[0], "confianza")
    UB_JUEGO_FAV = ubicacion_parametro(lista_jugadores[0], "juego favorito")
    nombre = lista_jugadores[posicion][UB_NOMBRE_JUGADOR]
    personalidad = lista_jugadores[posicion][UB_PERSONALIDAD]
    energia = lista_jugadores[posicion][UB_ENERGIA]
    suerte = lista_jugadores[posicion][UB_SUERTE]
    dinero = lista_jugadores[posicion][UB_DINERO]
    frustracion = lista_jugadores[posicion][UB_FRUSTRACION]
    ego = lista_jugadores[posicion][UB_EGO]
    carisma = lista_jugadores[posicion][UB_CARISMA]
    confianza = lista_jugadores[posicion][UB_CONFIANZA]
    juego_fav = lista_jugadores[posicion][UB_JUEGO_FAV]
    jugador_ordenado = [nombre, personalidad, energia, suerte,
                        dinero, frustracion, ego, carisma, confianza, juego_fav]
    return jugador_ordenado
