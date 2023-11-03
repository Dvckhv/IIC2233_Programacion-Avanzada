from PyQt5.QtCore import QObject

class Movimientos(QObject):
    def __init__(self,tecla_apretada,mostrar):
        super().__init__()
        self.tecla_apretada=tecla_apretada
        self.tecla_apretada.connect(self.evento_tecla)
        self.mostrar=mostrar
    
    def mover_python(self, direccion,posicion):
        
        if direccion == 'arriba':
            nueva_posicion = (posicion[0], (posicion[1] - 1) % 3)
        elif direccion == 'abajo':
            nueva_posicion = (posicion[0], (posicion[1] + 1) % 3)
        elif direccion == 'izquierda':
            nueva_posicion = ((posicion[0] - 1) % 3, posicion[1])
        elif direccion == 'derecha':
            nueva_posicion = ((posicion[0] + 1) % 3, posicion[1])
        if posicion != nueva_posicion:
            self.mostrar.emit(nueva_posicion)

    def evento_tecla(self,tuple):
        num=tuple[0]
        posicion=tuple[1]
        if num == 65: # A
            self.mover_python('izquierda',posicion)
        elif num == 87: # W
            self.mover_python('arriba',posicion)
        elif num == 83: # S
            self.mover_python('abajo',posicion)
        elif num == 68: # D
            self.mover_python('derecha',posicion)