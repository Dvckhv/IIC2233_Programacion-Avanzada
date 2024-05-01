from collections import namedtuple,defaultdict
Plato=namedtuple("platos",["nombre", "categoria", "tiempo", "precio","ingredientes"])
# --- EXPLICACION --- #
# los datos vienen en este orden el el .csv:
# nombre,categoria,tiempo_preparacion,precio,ingrediente_1,...,ingrediente_n
def cargar_platos(ruta_archivo: str) -> list:
    with open(ruta_archivo) as file:
        lista_platillos=file.readlines()
        lista_platillos=[i.strip().split(",") for i in lista_platillos]
    for i in range(len(lista_platillos)):
        lista_platillos[i][-1]=set(lista_platillos[i][-1].split(";"))
        lista_platillos[i][2]=int(lista_platillos[i][2])
        lista_platillos[i][3]=int(lista_platillos[i][3])

    platos_namedtuple=[Plato(*i) for i in lista_platillos ]
    return platos_namedtuple


# --- EXPLICACION --- #
# los datos vienen en este orden el el .csv:
# nombre,cantidad
def cargar_ingredientes(ruta_archivo: str) -> dict:
    dicionario_ingredientes=dict()
    with open(ruta_archivo) as file:
        lista_ingredientes=file.readlines()
    for ingrediente in lista_ingredientes:
        ingrediente=ingrediente.strip().split(",")
        dicionario_ingredientes[ingrediente[0]]=int(ingrediente[1])
    return dicionario_ingredientes

print(cargar_ingredientes("ingredientes.csv"))
