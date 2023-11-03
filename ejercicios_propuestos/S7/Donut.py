import sys
import os
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtGui import QPixmap

class VentanaDeHomero(QWidget):
    
    senal_abrir_ventana = pyqtSignal()

    rutas_por_titulo = {
        'Primero': os.path.join('img', 'ejercicio_5', 'primero.jpg'),
        'Segundo': os.path.join('img', 'ejercicio_5', 'segunda.jpg'),
        'Tercera': os.path.join('img', 'ejercicio_5', 'tercera.jpg')
    }

    def __init__(self, titulo, x, y, otra_ventana=None):
        super().__init__()

        self.setWindowTitle(titulo)
        self.setGeometry(x, y, 500, 600)
        self.senal_abrir_ventana.connect(self.show)

        self.ventana_donut = otra_ventana # Podría pasarla así la donut...
        self.senal_abrir_ventana_donut = None # ¿O con una señal? Solo quiero mi donut...

        # Las ventanas tienen pistas :o
        self.label_pista = QLabel(self)
        self.label_pista.setGeometry(0, 0, 500, 500)
        ruta_imagen = os.path.join(self.rutas_por_titulo.get(titulo, ''))
        pixeles = QPixmap(ruta_imagen)
        self.label_pista.setPixmap(pixeles)
        self.label_pista.setScaledContents(True)

        self.layout_principal = QVBoxLayout()
        self.layout_principal.addWidget(self.label_pista)

        if titulo == "Primero":
            self.boton = QPushButton("Abrir Primer Botón", self)
            self.boton.clicked.connect(self.abrir_ventana_1)

            self.boton2 = QPushButton("Abrir Segundo Botón", self)
            self.boton2.clicked.connect(self.abrir_ventana_2)

            self.layout_principal.addWidget(self.boton)
            self.layout_principal.addWidget(self.boton2)

        elif titulo == "Tercera":

            self.boton2 = QPushButton("Volver", self)
            self.boton2.clicked.connect(self.abrir_ventana_2)

            self.layout_principal.addWidget(self.boton2)

        self.setLayout(self.layout_principal)

    # Esta no es la mejor forma de abrir ventanas,
    # arregla esta función para que Homero pueda encontrar
    # su donut.
    def abrir_ventana_1(self):
        self.ventana_donut.show()


    def abrir_ventana_2(self):
        if self.senal_abrir_ventana_donut:
            self.hide()
            self.senal_abrir_ventana_donut.emit()


if __name__ == '__main__':
    app = QApplication([])

    ventana_donut_1 = VentanaDeHomero("Segundo", 300, 100)
    ventana_inicial = VentanaDeHomero("Primero", 100, 100, ventana_donut_1)
    ventana_donut_2 = VentanaDeHomero("Tercera", 500, 100)

    senal_abrir_ventana = pyqtSignal()
    ventana_inicial.senal_abrir_ventana_donut=ventana_donut_2.senal_abrir_ventana
    ventana_donut_2.senal_abrir_ventana_donut=ventana_inicial.senal_abrir_ventana
    ventana_inicial.show()
    sys.exit(app.exec_())