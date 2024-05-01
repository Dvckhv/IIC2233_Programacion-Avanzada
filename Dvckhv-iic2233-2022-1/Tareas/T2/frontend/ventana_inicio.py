import sys

from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import (QWidget, QApplication, QLabel, QRadioButton,
                             QVBoxLayout, QHBoxLayout, QPushButton)
from PyQt5.QtGui import QPixmap
from PyQt5 import uic


import os
import parametros as p


class VentanaInicio(QWidget):

    senal_ventana_principal = pyqtSignal()
    senal_ranking = pyqtSignal()

    def __init__(self):
        super().__init__()

        self.setGeometry(50, 50, 1500, 1000)
        self.setWindowTitle('A cazar aliens!')
        self.setStyleSheet("background-color: #211e2f;")
        self.senal_ventana_principal.connect(self.hide)
        self.senal_ranking.connect(self.hide)
        self.crear_elementos()

    def crear_elementos(self):

        self.logo = QLabel()
        pixeles = QPixmap(p.RUTA_LOGO)  # deshardcodear
        self.logo.setPixmap(pixeles)
        self.logo.setScaledContents(False)

        self.espacio = QLabel()

        self.boton1 = QPushButton("  Empezar juego!  ")
        self.boton2 = QPushButton("  Ranking  ")

        self.boton1.setStyleSheet("background-color : grey")
        self.boton2.setStyleSheet("background-color : grey")

        self.botones = QVBoxLayout()
        self.botones.addWidget(self.boton1)
        self.botones.addWidget(self.boton2)

        hbox = QHBoxLayout()
        hbox.addStretch(1)
        hbox.addLayout(self.botones)
        hbox.addStretch(1)
        boxlogo = QHBoxLayout()
        boxlogo.addStretch(1)
        boxlogo.addWidget(self.logo)
        boxlogo.addStretch(1)

        self.mainbox = QVBoxLayout()
        self.mainbox.addLayout(boxlogo)
        self.mainbox.addWidget(self.espacio)
        self.mainbox.addLayout(hbox)
        self.mainbox.addWidget(self.espacio)

        self.setLayout(self.mainbox)
        self.boton1.clicked.connect(self.senal_ventana_principal.emit)
        self.boton2.clicked.connect(self.senal_ranking.emit)


class VentanaRanking(QWidget):
    senal_posicionamiento = pyqtSignal()
    senal_volver = pyqtSignal()

    def __init__(self):
        super().__init__()
        self.senal_volver.connect(self.hide)

        self.setGeometry(50, 50, 800, 1000)
        self.setWindowTitle('A cazar aliens!')
        self.setStyleSheet("background-color: #211e2f;")
        self.crear_elementos()

    def crear_elementos(self):

        self.titulo = QLabel("RANKING DE PUNTAJES", self)
        self.titulo.setStyleSheet("font-size : 26pt")

        self.primero = QLabel("1", self)
        self.segundo = QLabel("2", self)
        self.tercero = QLabel("3", self)
        self.cuarto = QLabel("4", self)
        self.quinto = QLabel("5", self)
        self.puntaje_primero = QLabel("", self)
        self.puntaje_segundo = QLabel("", self)
        self.puntaje_tercero = QLabel("", self)
        self.puntaje_cuarto = QLabel("", self)
        self.puntaje_quinto = QLabel("", self)

        self.boton = QPushButton("Volver", self)
        self.boton.setStyleSheet("background-color : grey")
        self.boton.move(350, 800)
        self.perro = QLabel(self)
        pixeles = QPixmap(p.RUTA_PERRO_RIENDO)
        self.perro.setPixmap(pixeles)
        self.perro.setScaledContents(False)
        self.perro.setGeometry(550, 750, 258, 300)

        self.puestos = QVBoxLayout()
        self.puestos.addWidget(self.primero)
        self.puestos.addWidget(self.segundo)
        self.puestos.addWidget(self.tercero)
        self.puestos.addWidget(self.cuarto)
        self.puestos.addWidget(self.quinto)

        self.puntajes = QVBoxLayout()
        self.puntajes.addWidget(self.puntaje_primero)
        self.puntajes.addWidget(self.puntaje_segundo)
        self.puntajes.addWidget(self.puntaje_tercero)
        self.puntajes.addWidget(self.puntaje_cuarto)
        self.puntajes.addWidget(self.puntaje_quinto)

        self.hbox = QHBoxLayout()
        self.hbox.addStretch(2)
        self.hbox.addLayout(self.puestos)
        self.hbox.addStretch(1)
        self.hbox.addLayout(self.puntajes)
        self.hbox.addStretch(2)

        centrar = QHBoxLayout()
        centrar.addStretch(1)
        centrar.addWidget(self.titulo)
        centrar.addStretch(1)
        self.vbox = QVBoxLayout()
        self.vbox.addLayout(centrar)
        self.vbox.addStretch(1)
        self.vbox.addLayout(self.hbox)
        self.vbox.addStretch(2)
        
        self.setLayout(self.vbox)

        self.boton.clicked.connect(self.senal_volver)

    def closeEvent(self, event):
        self.senal_volver.emit()

    def asignar_puestos(self, list):
        self.primero.setText("1.- "+list[0][0])
        self.puntaje_primero.setText(list[0][1])

        self.segundo.setText("2.- "+list[1][0])
        self.puntaje_segundo.setText(list[1][1])

        self.tercero.setText("3.- "+list[2][0])
        self.puntaje_tercero.setText(list[2][1])

        self.cuarto.setText("4.- "+list[3][0])
        self.puntaje_cuarto.setText(list[3][1])

        self.quinto.setText("5.- "+list[4][0])
        self.puntaje_quinto.setText(list[4][1])


window_name, base_class = uic.loadUiType(p.RUTA_UI_VENTANA_PRINCIPAL)


class VentanaPrincipal(window_name, base_class):

    senal_comprobar_datos = pyqtSignal(dict)

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.move(50,50)

        self.boton_empezar = QPushButton("A cazar!", self)
        self.boton_empezar.setStyleSheet(
            "background-color : grey; font-size : 16pt")
        self.boton_empezar.move(700, 900)
        self.boton_empezar.clicked.connect(self.recolectar_datos)
        self.boton_empezar.resize(self.boton_empezar.sizeHint())

        self.label_error = QLabel(self)
        self.label_error.setStyleSheet("color : lightgrey")
        self.label_error.move(30, 850)

        self.label_nombre.resize(self.label_nombre.sizeHint())
        self.lineEdit.resize(self.label_nombre.sizeHint())
        self.titulo.resize(self.titulo.sizeHint())
        self.titulo.move(550, 30)

        

        # QRadioButtons
        self.b_luna.toggled.connect(self.mapa)
        self.b_jupiter.toggled.connect(self.mapa)
        self.b_invasion.toggled.connect(self.mapa)
        self.b_luna.setChecked(True)

    def iniciar_ventana(self):
        self.label_error.setText("")
        self.b_luna.setChecked(True)
        self.lineEdit.setText("")
        self.show()

    def recolectar_datos(self):

        nombre = self.lineEdit.text()
        informacion_partida = {"nombre": nombre,
                               "mapa": self.mapa_seleccionado}

        self.senal_comprobar_datos.emit(informacion_partida)

    def mapa(self):
        sender = self.sender()
        if sender.isChecked():
            self.mapa_seleccionado = sender.text()

    def mostrar_error(self, error):
        if error == "nombre":
            self.label_error.setText(
                "El nombre solo puede contener caracteres alfanumericos")
        self.label_error.resize(self.label_error.sizeHint())


if __name__ == '__main__':
    app = QApplication([])
    app.setStyleSheet('''QLabel { color: white; font-size: 16pt }
    QPushButton {
                 border-radius: 10px; border: 2px groove gray; border-style: outset;
            }
            QPushButton:pressed {
                 color: rgb(255,255,255);
            }
        ''')
    ventana = VentanaRanking()
    ventana.show()
    sys.exit(app.exec_())
