import sys

from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import (QWidget, QLabel,
                             QVBoxLayout, QHBoxLayout, QPushButton)
from PyQt5.QtGui import QPixmap


class VentanaPost(QWidget):
    senal_siguiente_nivel = pyqtSignal()
    senal_salir = pyqtSignal()

    def __init__(self):
        super().__init__()
        self.senal_salir.connect(self.hide)
        self.senal_siguiente_nivel.connect(self.hide)
        # Geometría
        self.setGeometry(50, 50, 800, 1000)
        self.setWindowTitle('A cazar aliens!')
        self.setStyleSheet("background-color: #211e2f;")
        self.crear_elementos()

    def crear_elementos(self):

        self.titulo = QLabel("RESUMEN DEL NIVEL", self)
        self.titulo.setStyleSheet("font-size : 26pt")

        self.label_nivel = QLabel("Nivel actual", self)
        self.label_balas = QLabel("Balas restantes", self)
        self.label_tiempo = QLabel("Tiempo restante", self)
        self.Label_puntaje_total = QLabel("Puntaje total", self)
        self.label_puntaje_obtenido = QLabel("Puntaje obtenido en nivel", self)
        self.nivel = QLabel("", self)
        self.cantidad_balas = QLabel("", self)
        self.tiempo = QLabel("", self)
        self.puntaje_total = QLabel("", self)
        self.puntaje_obtenido = QLabel("", self)
        self.label_continuar_juego = QLabel(self)
        self.label_continuar_juego.move(150, 600)

        self.boton_salir = QPushButton("  Salir  ", self)
        self.boton_salir.setStyleSheet("background-color : grey")
        self.boton_salir.resize(self.boton_salir.sizeHint())
        self.boton_salir.move(500, 800)
        self.boton_siguiente = QPushButton("  Siguiente nivel  ", self)
        self.boton_siguiente.setStyleSheet("background-color : grey")
        self.boton_siguiente.resize(self.boton_siguiente.sizeHint())
        self.boton_siguiente.move(150, 800)

        self.labels = QVBoxLayout()
        self.labels.addWidget(self.label_nivel)
        self.labels.addWidget(self.label_balas)
        self.labels.addWidget(self.label_tiempo)
        self.labels.addWidget(self.Label_puntaje_total)
        self.labels.addWidget(self.label_puntaje_obtenido)

        self.datos_nivel = QVBoxLayout()
        self.datos_nivel.addWidget(self.nivel)
        self.datos_nivel.addWidget(self.cantidad_balas)
        self.datos_nivel.addWidget(self.tiempo)
        self.datos_nivel.addWidget(self.puntaje_total)
        self.datos_nivel.addWidget(self.puntaje_obtenido)

        self.hbox = QHBoxLayout()
        self.hbox.addStretch(2)
        self.hbox.addLayout(self.labels)
        self.hbox.addStretch(1)
        self.hbox.addLayout(self.datos_nivel)
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

        self.boton_salir.clicked.connect(self.senal_salir)
        self.boton_siguiente.clicked.connect(self.senal_siguiente_nivel)

    def closeEvent(self, event):
        self.senal_salir.emit()

    def asignar_labels(self, dic):
        self.alien=QLabel(self)
        pixeles = QPixmap(dic["alien"])
        self.alien.setPixmap(pixeles)
        self.alien.setScaledContents(True)
        self.alien.setGeometry(600,170,*dic["dimensiones"])

        self.nivel.setText(str(dic["nivel"]))
        self.cantidad_balas.setText(str(dic["balas restantes"]))
        self.tiempo.setText(str(dic["tiempo restante"]))
        self.puntaje_total.setText(str(dic["puntaje total"]))
        self.puntaje_obtenido.setText(str(dic["puntaje nivel"]))
        self.boton_siguiente.setEnabled(dic["pasado"])

        if dic["pasado"]:
            self.label_continuar_juego.setText(
                "!Puedes dominar el siguente nivel!")
            self.label_continuar_juego.setStyleSheet("background-color : green")
            self.boton_siguiente.setEnabled(True)
        else:
            self.label_continuar_juego.setText("!Perdiste! No puedes seguir jugando :(")
            self.label_continuar_juego.setStyleSheet("background-color : red")
            self.boton_siguiente.setEnabled(False)
        self.label_continuar_juego.resize(
            self.label_continuar_juego.sizeHint())

        self.show()
