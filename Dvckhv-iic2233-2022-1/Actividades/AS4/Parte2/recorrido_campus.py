from Parte2.campus import Lugar
from collections import deque


def comprobar_chismoso(lugar: Lugar):
    # NO MODIFICAR
    for ayudante in lugar.ayudantes:
        if "Croak" in ayudante.frase:
            return True
    return False


def bfs_iterativo(inicio: Lugar, final: Lugar):
    visitados = list()
    por_visitar = deque([inicio])
    en_destino = False
    while not(en_destino) and len(por_visitar) > 0:
        lugar_actual = por_visitar.popleft()
        if lugar_actual is final:
            en_destino = True
        if not(comprobar_chismoso(lugar_actual)):
            visitados.append(lugar_actual)
            for vecino in lugar_actual.vecinos:
                if vecino not in visitados and vecino not in por_visitar:
                    por_visitar.append(vecino)
    return en_destino


def dfs_iterativo(inicio: Lugar, final: Lugar):
    visitados = list()
    por_visitar = deque([inicio])
    en_destino = False
    while not(en_destino) and len(por_visitar) > 0:
        lugar_actual = por_visitar.pop()
        if lugar_actual is final:
            en_destino = True
        if not(comprobar_chismoso(lugar_actual)):
            visitados.append(lugar_actual)
            for vecino in lugar_actual.vecinos:
                if vecino not in visitados and vecino not in por_visitar:
                    por_visitar.append(vecino)
    return en_destino


def bfs_iterativo_largo(inicio: Lugar, final: Lugar):
    visitados = list()
    por_visitar = deque([(inicio, 0)])
    en_destino = False
    while not(en_destino) and len(por_visitar) > 0:
        tupla = por_visitar.popleft()
        lugar_actual, recorrido = tupla
        if lugar_actual is final:
            return recorrido
        if not(comprobar_chismoso(lugar_actual)):
            visitados.append(lugar_actual)
            for vecino in lugar_actual.vecinos:
                if vecino not in visitados and vecino not in por_visitar:
                    por_visitar.append((vecino, recorrido+1))
    return -1


def dfs_iterativo_largo(inicio: Lugar, final: Lugar):
    visitados = list()
    por_visitar = deque([(inicio, 0)])
    en_destino = False

    while not(en_destino) and len(por_visitar) > 0:

        lugar_actual, recorrido = por_visitar.pop()
        if lugar_actual is final:
            return recorrido
        if not(comprobar_chismoso(lugar_actual)):
            visitados.append(lugar_actual)
            for vecino in lugar_actual.vecinos:
                if vecino not in visitados and vecino not in por_visitar:
                    por_visitar.append((vecino, recorrido+1))
    return -1


def bfs_iterativo_camino(inicio: Lugar, final: Lugar):
    # Utiliza este diccionario para implementar el camino.
    # Las llaves del diccionario es UN nodo vecino (NO un listado de todos los nodos vecinos)
    # y el valor el nodo en cuestion
    padres = dict()
    padres[inicio] = None
    visitados = list()
    por_visitar = deque([(inicio, None)])
    en_destino = False
    while not(en_destino) and len(por_visitar) > 0:
        tupla = por_visitar.popleft()
        lugar_actual, padre = tupla

        padres[lugar_actual] = padre
        if lugar_actual is final:
            return creador_camino(padres, final)
        if not(comprobar_chismoso(lugar_actual)):
            visitados.append(lugar_actual)
            for vecino in lugar_actual.vecinos:
                if vecino not in visitados and vecino not in por_visitar:
                    por_visitar.append((vecino, lugar_actual))
    # Completar
    pass


def dfs_iterativo_camino(inicio: Lugar, final: Lugar):
    # Utiliza este diccionario para implementar el camino.
    # Las llaves del diccionario es UN nodo vecino (NO un listado de todos los nodos vecinos)
    # y el valor el nodo en cuestion
    padres = dict()
    padres = dict()
    padres[inicio] = None
    padres = dict()
    padres[inicio] = None
    visitados = list()
    por_visitar = deque([(inicio, None)])
    en_destino = False
    while not(en_destino) and len(por_visitar) > 0:
        tupla = por_visitar.pop()
        lugar_actual, padre = tupla

        padres[lugar_actual] = padre
        if lugar_actual is final:
            return creador_camino(padres, final)
        if not(comprobar_chismoso(lugar_actual)):
            visitados.append(lugar_actual)
            for vecino in lugar_actual.vecinos:
                if vecino not in visitados and vecino not in por_visitar:
                    por_visitar.append((vecino, lugar_actual))

    # Completar
    pass


def creador_camino(diccionario_padres, final):
    # NO MODIFICAR
    camino = []
    camino.append(final)
    while diccionario_padres[final] is not None:
        camino.append(diccionario_padres[final])
        final = diccionario_padres[final]
    camino.reverse()
    return camino


def imprimir_camino(camino):
    # NO MODIFICAR
    recorrido = ""
    largo = len(camino)
    contador = 1
    for lugar in camino:
        if contador < largo:
            recorrido = recorrido + f"[{lugar.nombre}] -> "
        else:
            recorrido = recorrido + f"[{lugar.nombre}]."
        contador += 1
    print(recorrido)


if __name__ == "__main__":
    print("\nNO DEBES EJECUTAR AQUÍ EL PROGRAMA!!!!")
    print("Ejecuta el main.py\n")
    raise(ModuleNotFoundError)
