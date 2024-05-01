from collections import namedtuple, defaultdict
import enum
from functools import reduce

Plato = namedtuple('nombre', 'nombre ingredientes')

class Ayudante:
    def __init__(self, nombre, platos, dinero):
        self.nombre = nombre
        self.platos = platos # lista con namedtuples de platos
        self.dinero = dinero

    def obtener_ingredientes_platos(self):
        lista_ingredientes=list(map(lambda x:x.ingredientes,self.platos))
        return lista_ingredientes

    def cantidad_ingredientes(self, lista_ingredientes_platos): #REVISAR
        lista_ingredientes=reduce(lambda x,y:x+y ,lista_ingredientes_platos)
        lista_nombres=[]
        lista_cantidades=[]
        for ingrediente in lista_ingredientes:
            if ingrediente[0] not in lista_nombres:
                lista_nombres.append(ingrediente[0])
                lista_cantidades.append(ingrediente[1])
            else:
                for n,nombre in enumerate(lista_nombres):
                    if nombre==ingrediente[0]:
                        lista_cantidades[n]+=ingrediente[1]
        lista_reducida=zip(lista_nombres,lista_cantidades)
        for ingrediente in lista_reducida:
            yield ingrediente
        
        
    def total_compra(self, ingredientes_platos, supermercado):
        ingredientes=reduce(lambda x,y:x+y ,ingredientes_platos)
        precios_por_ingrediente=list(map(lambda ing:supermercado.consulta_precio(ing[0])*ing[1],ingredientes))
        total=reduce(lambda x,y: x+y,precios_por_ingrediente)
        return total

