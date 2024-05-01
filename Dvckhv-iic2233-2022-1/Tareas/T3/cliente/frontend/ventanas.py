import sys

from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import (QWidget, QApplication, QLabel,
                             QVBoxLayout, QHBoxLayout, QPushButton,QLineEdit)
from PyQt5.QtGui import QPixmap
from os.path import join
from utils import data_json

class VentanaInicio(QWidget):
    senal_inicio=pyqtSignal(str)
    def __init__(self):
        super().__init__()
        self.setGeometry(50, 50, 1008, 800)
        self.setMinimumSize(1008,800)
        self.setMaximumSize(1008,800)
        self.setWindowTitle('DCCasillas')    
        self.crear_elementos()

    def crear_elementos(self):
        self.fondo = QLabel(self)
        pixeles = QPixmap(join(*data_json("RUTA_FONDO"))) 
        self.fondo.setPixmap(pixeles)
        self.fondo.setScaledContents(True)
        self.fondo.resize(1008,800)

        self.logo = QLabel()
        pixeles = QPixmap(join(*data_json("RUTA_LOGO")))
        self.logo.setPixmap(pixeles)
        self.logo.setScaledContents(True)
        self.logo.setMinimumSize(300,300)
        self.logo.setMaximumSize(300,300)

        self.nombre=QLineEdit(self)
        self.nombre.setPlaceholderText("Ingrese tu nombre")

        self.boton = QPushButton("JUGAR!",self)
        self.boton.clicked.connect(self.enviar_datos)
        vbox=QVBoxLayout()
        vbox.addStretch(1)
        vbox.addWidget(self.logo)
        vbox.addStretch(1)
        vbox.addWidget(self.nombre)
        vbox.addWidget(self.boton)
        vbox.addStretch(1)

        hbox=QHBoxLayout()
        hbox.addStretch(1)
        hbox.addLayout(vbox)
        hbox.addStretch(1)
        self.setLayout(hbox)
        

    def enviar_datos(self):
        usuario=self.nombre.text()
        print("boton pulsado")
        self.senal_inicio.emit(usuario)
    def login_rechazado(self,motivo):
        self.nombre.clear()
        self.nombre.setPlaceholderText(motivo)
        if motivo == "partida en curso":
            self.boton.setEnabled(False)


        
        

class VentanaEspera(QWidget):
    senal_iniciar_juego=pyqtSignal()
    def __init__(self):
        super().__init__()
        self.setGeometry(50, 50, 1008, 800)
        self.setMinimumSize(1008,800)
        self.setMaximumSize(1008,800)
        self.setWindowTitle('DCCasillas')
        self.crear_elementos()  
        
    def crear_elementos(self):
        self.fondo = QLabel(self)
        pixeles = QPixmap(join(*data_json("RUTA_FONDO"))) 
        self.fondo.setPixmap(pixeles)
        self.fondo.setScaledContents(True)
        self.fondo.setGeometry(0,0,1008,800)
        self.boton = QPushButton("Iniciar Partida",self)
        self.boton.clicked.connect(self.iniciar_partida)
        self.boton.setEnabled(False)
        self.hbox=QHBoxLayout()
        self.vbox=QVBoxLayout()
        self.hbox.addStretch(1)
        self.hbox.addLayout(self.vbox)
        self.hbox.addStretch(1)
        self.vbox.addWidget(QLabel("Esperando a iniciar la partida"))
        self.vbox.addStretch(1)
        self.boton.move(400,700)
        self.setLayout(self.hbox)
    
    def anadir_jugador(self,dic):
        ficha=QLabel()
        if dic["color"]=="amarillo":
            color="amarilla"
        elif dic["color"]=="rojo":
            color="roja"
        else:
            color=dic["color"]

        ruta=join(*data_json("RUTA_FICHA_SIMPLE"))+color
        pixeles=QPixmap(ruta)
        ficha.setPixmap(pixeles)
        ficha.setScaledContents(True)
        ficha.setMaximumSize(75,75)
        ficha.setMinimumSize(75,75)
        nombre=QLabel(dic["nombre"])
        color=QLabel(dic["color"])
        container = QWidget(self)
        self.vbox.addWidget(container)
        hbox_jugador=QHBoxLayout(container)
        container.setStyleSheet('''
.QLabel {
    color: black;
    font-weight: bold;
    border: 0px;
    margin: 0px;
    padding: 0px;
}
.QWidget {
    background-color:white  ;
    border-radius: 10px; 
    border: 2px groove gray;
    border-style: outset;
}''')   
        hbox_jugador.addStretch(1)
        hbox_jugador.addWidget(nombre)
        hbox_jugador.addWidget(color)
        hbox_jugador.addWidget(ficha)
        hbox_jugador.addStretch(1)
        self.vbox.addStretch(1)

    def administrador(self,bool)    :
        self.boton.setEnabled(bool)
    def iniciar_partida(self):
        self.senal_iniciar_juego.emit()
        
class VentanaJuego(QWidget):
    senal_dado=pyqtSignal()
    def __init__(self):
        super().__init__()
        self.setGeometry(50, 50, 1008, 800)
        self.setMinimumSize(1008,800)
        self.setMaximumSize(1008,800)
        self.setWindowTitle('DCCasillas')
        self.containers=list()
        self.fichas=list()
        self.crear_elementos()

    def crear_elementos(self):
        self.fondo = QLabel(self)
        self.fondo.setStyleSheet("background-color:#d8e4fc")
        self.fondo.setMinimumSize(1008,800)
        self.tablero=QWidget(self)
        self.imagen_tablero=QLabel(self.tablero)
        pixeles=QPixmap(join(*data_json("RUTA_TABLERO")))
        self.imagen_tablero.setPixmap(pixeles)
        self.tablero.setMaximumSize(480,480)
        self.tablero.setMinimumSize(480,480)
        self.imagen_tablero.setScaledContents(True)
        self.imagen_tablero.setMinimumSize(480,480)
        self.imagen_tablero.setMaximumSize(480,480)
        for i in range(len(data_json("UBICACION_ESTRELLAS"))):
            estrella = QLabel(self.tablero)
            pixeles = QPixmap(join(*data_json("RUTA_ESTRELLA")))        
            estrella.setPixmap(pixeles)
            estrella.setScaledContents(True)
            estrella.setMinimumSize(50,50)
            estrella.setMaximumSize(50,50)
            estrella.move(*data_json("UBICACION_ESTRELLAS")[i])
        self.dado=QLabel(self)
        pixeles=QPixmap(join(*data_json("RUTA_DADO")))
        self.dado.setPixmap(pixeles)
        self.dado.setScaledContents(True)
        self.dado.setMaximumSize(75,75)
        self.dado.setMinimumSize(75,75)
        self.boton_dado = QPushButton(" Tirar dado ",self)
        self.boton_dado.clicked.connect(self.manejo_dado)
        self.boton_dado.setEnabled(False)
        self.lanzamiento_dado=QLabel("Numero obtenido: ? ")
        self.main_layout=QHBoxLayout()
        self.layout_dado=QHBoxLayout()
        self.layout_dado.addWidget(self.dado)
        self.layout_dado.addWidget(self.boton_dado)
        self.vbox1=QVBoxLayout()
        self.vbox1.addLayout    (self.layout_dado)
        self.vbox1.addStretch(1)
        self.vbox1.addWidget(self.lanzamiento_dado)
        self.vbox1.addStretch(1)
        self.vbox1.addWidget(self.tablero)
        self.vbox1.addStretch(1)

        self.jugador_de_turno=QLabel("Jugador de turno: ?",self)
        self.jugador_de_turno.setStyleSheet("background-color: lightblue;")
        self.vbox2=QVBoxLayout()
        self.vbox2.addWidget(self.jugador_de_turno)
        self.vbox2.addSpacing(15)
        
        self.setLayout(self.main_layout)
        self.main_layout.addLayout(self.vbox1)
        self.main_layout.addLayout(self.vbox2)
        


    def añadir_jugador(self,dic):
        
        container = QWidget(self)
        self.containers.append(container)
        container.setStyleSheet('''
.QLabel {
    color: black;
    font-weight: bold;
    border: 0px;
    margin: 0px;
    padding: 0px;
}
.QWidget {
    background-color:white  ;
    border-radius: 10px; 
    border: 2px groove gray;
    border-style: outset;
}''')   
        self.vbox2.addWidget(container)
        hbox_jugador=QHBoxLayout(container)

        ficha=QLabel()
        if dic["color"]=="amarillo":
            color="amarilla"
        elif dic["color"]=="rojo":
            color="roja"
        else:
            color=dic["color"]
        
        ruta=join(*data_json("RUTA_FICHA_SIMPLE"))+color
        pixeles=QPixmap(ruta)
        ficha.setPixmap(pixeles)
        ficha.setScaledContents(True)
        ficha.setMaximumSize(75,75)
        ficha.setMinimumSize(75,75)
        nombre=QLabel(dic["nombre"])
        turno=QLabel(f"Turno: {dic['turno']}")
        fichas_en_base=QLabel(f"Fichas en base: { dic['fichas_en_base']}",self)
        fichas_en_color=QLabel(f"Fichas en color: { dic['fichas_en_color']}",self)
        fichas_en_victoria=QLabel(f"Fichas en victoria: { dic['fichas_en_victoria']}",self)

        vbox_jugador=QVBoxLayout()
        vbox_jugador.addStretch(1)
        vbox_jugador.addWidget(nombre)
        vbox_jugador.addWidget(turno)
        vbox_jugador.addWidget(fichas_en_base)
        vbox_jugador.addWidget(fichas_en_color)
        vbox_jugador.addWidget(fichas_en_victoria)
        vbox_jugador.addStretch(1)
        hbox_jugador.addWidget(ficha)
        hbox_jugador.addLayout(vbox_jugador)
 
    def actualizar_juego(self,datos):
        self.limpiar_juego()
        for dic_jugador in datos["cambios"]:

            self.añadir_jugador(dic_jugador)
            if dic_jugador["fichas_juntas"]:
                ficha=QLabel(self.tablero)
                if dic_jugador["color"]=="amarillo":
                    color="amarillas"
                elif dic_jugador["color"]=="rojo":
                    color="rojas"
                elif dic_jugador["color"]=="azul":
                    color="azules"
                elif dic_jugador["color"]=="verde":
                    color="verdes"
                pixeles=QPixmap(join(*data_json("RUTA_FICHA_DOBLE"))+color)
                ficha.setPixmap(pixeles)
                ficha.setScaledContents(True)
                ficha.setMaximumSize(75,75)
                ficha.setMinimumSize(75,75)
                ficha.move(*dic_jugador["posicion_ficha_1"]) #ambas fichas tienen la misma posicion
                ficha.show()
                ficha.raise_()
                self.fichas.append(ficha)
            else:
                ficha1=QLabel(self.tablero)
                ficha2=QLabel(self.tablero)
                if dic_jugador["color"]=="amarillo":
                    color="amarilla"
                elif dic_jugador["color"]=="rojo":
                    color="roja"
                else:
                    color=dic_jugador["color"]
                pixeles=QPixmap(join(*data_json("RUTA_FICHA_SIMPLE"))+color)
                ficha1.setPixmap(pixeles)
                ficha1.setScaledContents(True)
                ficha1.setMaximumSize(75,75)
                ficha1.setMinimumSize(75,75)
                ficha1.move(*dic_jugador["posicion_ficha_1"])
                ficha2.setPixmap(pixeles)
                ficha2.setScaledContents(True)
                ficha2.setMaximumSize(75,75)
                ficha2.setMinimumSize(75,75)
                ficha2.move(*dic_jugador["posicion_ficha_2"])
                self.fichas.append(ficha1)
                self.fichas.append(ficha2)
                ficha1.show()
                ficha2.show()
                ficha1.raise_()
                ficha2.raise_()
        self.lanzamiento_dado.setText(f"Numero obtenido : {datos['numero_dado']}")
        self.jugador_de_turno.setText(f"Jugador de turno: {datos['en_turno']}")

    def manejo_dado(self):
        self.senal_dado.emit()
        self.boton_dado.setEnabled(False)

    def activar_dado(self):
        self.boton_dado.setEnabled(True)
    def limpiar_juego(self):
        for ficha in self.fichas:
            ficha.hide()
            ficha.setParent(None)
            
        for container in self.containers:
            container.close()
            container.setParent(None)
        
        self.containers=[]
        self.fichas=[]
        
class VentanaPost(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(50, 50, 1008, 800)
        self.setMinimumSize(1008,800)
        self.setMaximumSize(1008,800)
        self.setWindowTitle('DCCasillas')
    def crear_ranking(self,ganador,dic):
        self.fondo = QLabel(self)
        pixeles = QPixmap(join(*data_json("RUTA_FONDO"))) 
        self.fondo.setPixmap(pixeles)
        self.fondo.setScaledContents(True)
        self.fondo.setGeometry(0,0,1008,800)
        self.hbox=QHBoxLayout()
        self.vbox=QVBoxLayout()
        self.hbox.addStretch(1)
        self.hbox.addLayout(self.vbox)
        self.hbox.addStretch(1)
        self.vbox.addWidget(QLabel(f"La victoria es para {ganador}"))
        self.vbox.addStretch(2)
        self.setLayout(self.hbox)
        for jugador in dic:
            container = QWidget(self)
            self.vbox.addWidget(container)
            hbox_jugador=QHBoxLayout(container)
            container.setStyleSheet('''
    .QLabel {
        color: black;
        font-weight: bold;
        border: 0px;
        margin: 0px;
        padding: 0px;
    }
    .QWidget {
        background-color:white  ;
        border-radius: 10px; 
        border: 2px groove gray;
        border-style: outset;
    }''')   
            nombre=QLabel(jugador["nombre"])
            fichas_base=QLabel(jugador["fichas_en_base"])
            fichas_color=QLabel(jugador["fichas_en_color"])
            fichas_victoria=QLabel(jugador["fichas_en_victoria"])
            vbox_jugador=QVBoxLayout()
            vbox_jugador.addWidget(fichas_base)
            vbox_jugador.addWidget(fichas_color)
            vbox_jugador.addWidget(fichas_victoria)
            hbox_jugador.addWidget(nombre)
            hbox_jugador.addStretch(1)
            hbox_jugador.addLayout(vbox_jugador)
            self.vbox.addStretch(1)
        self.vbox.addStretch(1)
        self.show()