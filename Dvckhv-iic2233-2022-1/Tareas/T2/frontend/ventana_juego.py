from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import (QLabel, QPushButton, QMainWindow)
from PyQt5.QtMultimedia import QSound
from PyQt5.QtGui import QPixmap, QColor, QMouseEvent

import parametros as p


class VentanaJuego(QMainWindow):
    senal_tecla = pyqtSignal(str)
    senal_salir = pyqtSignal()
    senal_click = pyqtSignal(QMouseEvent)

    def __init__(self):
        super().__init__()
        self.setGeometry(50, 50, p.MAX_X_VENTANA, p.MAX_Y_VENTANA)
        self.mover_explosion = True
        self.init_gui()

    def init_gui(self):
        self.fondo = QLabel(self)
        self.perro = QLabel(self)
        pixeles = QPixmap(p.RUTA_PERRO_RIENDO)
        self.perro.setPixmap(pixeles)
        self.perro.setScaledContents(True)
        self.perro.setGeometry(300, p.MAX_Y_VENTANA -
                               (p.ALTO_MENU+270), 258, 300)
        self.cuadro = QLabel(self)
        color = QColor(33, 30, 47)
        pixeles = QPixmap(p.MAX_X_VENTANA, p.ALTO_MENU)
        pixeles.fill(color)
        self.cuadro.setPixmap(pixeles)
        self.cuadro.setScaledContents(True)
        self.cuadro.setGeometry(
            0, p.MAX_Y_VENTANA-p.ALTO_MENU, p.MAX_X_VENTANA, p.ALTO_MENU)
        self.label_termino = QLabel(" ", self)
        self.label_termino.move(p.MAX_X_VENTANA-500, 400)
        self.label_termino.setStyleSheet("font-size : 26pt")

        self.boton_pausa = QPushButton("Pausa", self)
        self.boton_salir = QPushButton("Salir", self)
        self.boton_pausa.setStyleSheet("background-color : grey")
        self.boton_salir.setStyleSheet("background-color : grey")
        self.boton_pausa.move(p.MAX_X_VENTANA-200, p.MAX_Y_VENTANA-180)
        self.boton_salir.move(p.MAX_X_VENTANA-200, p.MAX_Y_VENTANA-130)
        self.boton_pausa.clicked.connect(self.pausar)
        self.boton_salir.clicked.connect(self.senal_salir)
        self.boton_pausa.setFocusPolicy(4)
        self.boton_salir.setFocusPolicy(4)

        self.label_bala_extra = QLabel(self)
        pix_bala_extra = QPixmap(p.RUTA_BALA_EXTRA)
        self.label_bala_extra.setPixmap(pix_bala_extra)
        self.label_bala_extra.setScaledContents(True)
        self.label_estrella = QLabel(self)
        pix_estrella = QPixmap(p.RUTA_ESTRELLA)
        self.label_estrella.setPixmap(pix_estrella)
        self.label_estrella.setScaledContents(True)
        self.label_bomba = QLabel(self)
        pix_bomba = QPixmap(p.RUTA_BOMBA)
        self.label_bomba.setPixmap(pix_bomba)
        self.label_bomba.setScaledContents(True)
        self.label_bala_extra.hide()
        self.label_bomba.hide()
        self.label_estrella.hide()

        self.imagen_bala = QLabel(self)
        pix_bala = QPixmap(p.RUTA_BALA)
        self.imagen_bala.setPixmap(pix_bala)
        self.imagen_bala.setScaledContents(True)
        self.imagen_bala.setGeometry(400, p.MAX_Y_VENTANA-140, 50, 100)
        self.label_balas = QLabel("Balas Restantes", self)
        self.label_balas.resize(self.label_balas.sizeHint())
        self.label_balas.move(400, p.MAX_Y_VENTANA-180)
        self.cantidad_balas = QLabel("", self)
        self.cantidad_balas.move(530, p.MAX_Y_VENTANA-130)

        self.label_tiempo = QLabel("Tiempo Restante", self)
        self.label_tiempo.resize(self.label_tiempo.sizeHint())
        self.label_tiempo.move(50, p.MAX_Y_VENTANA-180)
        self.contador_tiempo = QLabel("", self)
        self.contador_tiempo.move(50, p.MAX_Y_VENTANA-130)

        self.label_puntaje = QLabel("Puntaje Actual", self)
        self.label_puntaje.resize(self.label_puntaje.sizeHint())
        self.label_puntaje.move(700, p.MAX_Y_VENTANA-180)
        self.cantidad_puntos = QLabel("", self)
        self.cantidad_puntos.move(700, p.MAX_Y_VENTANA-130)

        self.label_nivel = QLabel("Nivel Actual", self)
        self.label_nivel.resize(self.label_nivel.sizeHint())
        self.label_nivel.move(1000, p.MAX_Y_VENTANA-180)
        self.nivel_actual = QLabel("", self)
        self.nivel_actual.move(1000, p.MAX_Y_VENTANA-130)

        self.mira = QLabel(self)
        pixeles_mira = QPixmap(p.RUTA_MIRA)
        self.mira.setPixmap(pixeles_mira)
        self.mira.resize(p.ANCHO_MIRA, p.ALTO_MIRA)
        self.mira.setScaledContents(True)

        self.label_explosion = QLabel(self)
        self.label_explosion.resize(p.ANCHO_MIRA, p.ALTO_MIRA)

        self.label_explosion.hide()

    def keyPressEvent(self, event) -> None:
        self.senal_tecla.emit(event.text())

    def mousePressEvent(self, event):
        self.senal_click.emit(event)

    def generar_mapa(self, dic):
        self.label_termino.setText(" ")
        pixeles_fondo = QPixmap(dic["fondo"])
        self.fondo.setPixmap(pixeles_fondo)
        self.fondo.resize(p.MAX_X_VENTANA, p.MAX_Y_VENTANA-p.ALTO_MENU)
        self.fondo.setScaledContents(True)
        self.label_termino.setText(" ")
        self.show()
        self.lista_aliens = []
        self.pixeles_alien = QPixmap(dic["alien vivo"])
        self.pixeles_alien_muerto = QPixmap(dic["alien muerto"])
        for i in range(dic["cantidad aliens"]):
            label_alien = QLabel(self)
            label_alien.setPixmap(self.pixeles_alien)
            label_alien.resize(*dic["dimensiones alien"])
            label_alien.setScaledContents(True)
            label_alien.hide()
            self.lista_aliens.append(label_alien)

    def mover_aliens(self, list):
        for estados_alien in list:
            if estados_alien[2]:
                self.lista_aliens[estados_alien[0]].show()
                self.lista_aliens[estados_alien[0]].move(*estados_alien[1])
            else:
                self.lista_aliens[estados_alien[0]].hide()

    def alien_muerto(self, posicion):
        self.lista_aliens[posicion].setPixmap(self.pixeles_alien_muerto)

    def reiniciar_mapa(self):
        for alien in self.lista_aliens:
            alien.clear()
        pixeles = QPixmap(p.RUTA_PERRO_RIENDO)
        self.perro.setPixmap(pixeles)

    def disparo(self, lista_ruta):
        pixeles = QPixmap(lista_ruta[0])
        self.mira.setPixmap(pixeles)

    def mover_mira(self, posicion):
        self.mira.move(*posicion)
        if self.mover_explosion:
            self.label_explosion.move(*posicion)
        self.label_explosion.raise_()
        self.mira.raise_()

    def explosion(self, lista_ruta):
        if lista_ruta[0] == "end":
            self.mover_explosion = True
            self.label_explosion.hide()
        else:
            self.mover_explosion = False
            pixeles = QPixmap(lista_ruta[0])
            self.label_explosion.setPixmap(pixeles)
            self.label_explosion.setScaledContents(True)
            self.label_explosion.show()

    def emitir_sonido(self, ruta):
        QSound.play(ruta)

    def terminator_dog(self, dic):
        pixeles = QPixmap(dic["alien"])
        self.perro.setPixmap(pixeles)
        self.emitir_sonido(dic["risa"])
        self.label_termino.setText("¡Nivel superado!")
        self.label_termino.resize(self.label_termino.sizeHint())

    def labels(self, dict):
        self.cantidad_balas.setText(" x"+str(dict["balas"]))
        self.cantidad_balas.resize(self.cantidad_balas.sizeHint())

        self.cantidad_puntos.setText(str(dict["puntaje"]))
        self.cantidad_puntos.resize(self.cantidad_puntos.sizeHint())

        self.nivel_actual.setText(str(dict["nivel"]))
        self.cantidad_balas.resize(self.cantidad_balas.sizeHint())

        self.contador_tiempo.setText(str(dict["tiempo"]))
        self.contador_tiempo.resize(self.contador_tiempo.sizeHint())

    def pausar(self):
        self.senal_tecla.emit("p")

    def aparicion_estrella(self, dimensiones):
        if self.label_estrella.isVisible():
            self.label_estrella.hide()
        else:
            self.label_estrella.setGeometry(*dimensiones)
            self.label_estrella.show()

    def aparicion_bala(self, dimensiones):
        if self.label_bala_extra.isVisible():
            self.label_bala_extra.hide()
        else:
            self.label_bala_extra.setGeometry(*dimensiones)
            self.label_bala_extra.show()

    def aparicion_bomba(self, dimensiones):
        if self.label_bomba.isVisible():
            self.label_bomba.hide()
        else:
            self.label_bomba.setGeometry(*dimensiones)
            self.label_bomba.show()
