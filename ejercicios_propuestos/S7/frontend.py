import sys
from os import path
from PyQt5.QtCore import pyqtSignal, QObject, Qt
from PyQt5.QtWidgets import (QApplication, QWidget, QLabel)
from PyQt5.QtGui import QPixmap

from backend import Movimientos


class Ventana(QWidget):
    tecla_apretada = pyqtSignal(tuple)
    mostrar=pyqtSignal(tuple)
    def __init__(self):
        super().__init__()
        self.posicion = (1, 1)
        self.ruta_imagen = path.join('img', 'python_icon.png')
        self.inicializa_gui()
    
    def inicializa_gui(self):
        self.setGeometry(300, 300, 300, 300)
        self.etiquetas = {}
        for fila in range(3):
            for columna in range(3):
                nueva_etiqueta = QLabel(self)
                nueva_etiqueta.setGeometry(fila * 100, columna * 100, 100, 100)
                if (fila, columna) == self.posicion:
                    pixmap = QPixmap(self.ruta_imagen)
                else:
                    pixmap = QPixmap(100, 100)
                    pixmap.fill(Qt.white)
                nueva_etiqueta.setPixmap(pixmap)
                nueva_etiqueta.setScaledContents(True)
                self.etiquetas[(fila, columna)] = nueva_etiqueta
                self.mostrar.connect(self.imprimir_python)

    def imprimir_python(self, nueva_posicion):
        pixmap = QPixmap(100, 100)
        pixmap.fill(Qt.white)
        self.etiquetas[self.posicion].setPixmap(pixmap)
        pixmap = QPixmap(self.ruta_imagen)
        self.etiquetas[nueva_posicion].setPixmap(pixmap)
        self.posicion=nueva_posicion


    def keyPressEvent(self, event):
        self.tecla_apretada.emit((event.key(),self.posicion))
        

if __name__ == '__main__':
    app = QApplication([])
    ventana = Ventana()
    movimientos=Movimientos(ventana.tecla_apretada,ventana.mostrar)
    ventana.show()
    sys.exit(app.exec_())