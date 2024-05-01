# --- EJEMPLO --- #
from collections import defaultdict
# [Plato1, Plato2, Plato2, Plato4]
# pasa a ser
# {"Categoria1": [Plato3, Plato2], "Categoria2": [Plato1, Plato4]}
# Plato=namedtuple("platos",["nombre", "categoria", "tiempo", "precio","ingredientes"])
def platos_por_categoria(lista_platos: list) -> dict:
    diccionario_categorias=defaultdict(list)
    categorias=[]
    for i in lista_platos:
        categorias.append[i[1]]
    categorias=set(categorias)
    diccionario_categorias[categorias*]
    
        
    pass


# Debe devolver los platos que no tengan ninguno de los ingredientes descartados
def descartar_platos(ingredientes_descartados: set, lista_platos: list):
    pass


# --- EXPLICACION --- #
# Si el plato necesita un ingrediente que no tiene cantidad suficiente,
# entonces retorna False
#
# En caso que tenga todo lo necesario, resta uno a cada cantidad y retorna True
def preparar_plato(plato, ingredientes: dict) -> bool:
    for ingrediente_plato in plato.ingredientes:
        if ingredientes[ingrediente_plato] <= 0:
            return False

    for ingrediente_plato in plato.ingredientes:
        ingredientes[ingrediente_plato] -= 1

    return True


# --- EXPLICACION --- #
# Debe retornar un diccionario que agregue toda la información ...
#  de la lista de platos.
# precio total, tiempo total, cantidad de platos, platos
def resumen_orden(lista_platos: list) -> dict:
    pass
