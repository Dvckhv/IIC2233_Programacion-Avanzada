import sys
sys.path.append("..")
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import (QWidget, QApplication, QLabel, QLineEdit,
                             QVBoxLayout, QHBoxLayout, QPushButton)
from PyQt5.QtGui import QPixmap
import os
import parametros as p


class VentanaInicio(QWidget):

    senal_enviar_login = pyqtSignal(tuple)

    def __init__(self):
        super().__init__()

        # Geometría
        self.setGeometry(600, 200, 500, 500)
        self.setWindowTitle('Ventana de Inicio')
        self.setStyleSheet("background-color: lightblue;")
    
        self.crear_elementos()

    def crear_elementos(self):
        
        self.logo=QLabel()
        pixeles = QPixmap(p.RUTA_LOGO)
        self.logo.setPixmap(pixeles)
        self.logo.setScaledContents(True)

        self.label_usuario=QLabel("Nombre de usuario:")
        self.edit_usuario=QLineEdit('')
        self.edit_usuario.resize(100, 20)

        self.label_contraseña=QLabel("Contraseña:")
        self.edit_contraseña=QLineEdit('')
        self.edit_contraseña.resize(100, 20)

        self.boton=QPushButton("Empezar juego!")
        
        self.vbox1=QVBoxLayout()
        self.vbox1.addWidget(self.label_usuario)
        self.vbox1.addWidget(self.label_contraseña)

        self.vbox2=QVBoxLayout()
        self.vbox2.addWidget(self.edit_usuario)
        self.vbox2.addWidget(self.edit_contraseña)

        self.hbox=QHBoxLayout()
        self.hbox.addLayout(self.vbox1)
        self.hbox.addLayout(self.vbox2)
        self.mainbox=QVBoxLayout()
        self.mainbox.addWidget(self.logo)
        
        self.mainbox.addLayout(self.hbox)
        self.mainbox.addWidget(self.boton)
    
        self.setLayout(self.mainbox)
        self.boton.clicked.connect(self.enviar_login)

    def enviar_login(self):
        usuario=self.edit_usuario.text()
        contraseña=self.edit_contraseña.text()
        self.senal_enviar_login.emit((usuario,contraseña))
        pass

    def recibir_validacion(self, valid, errores):
        if valid:
            self.hide()
        else:
            if "Usuario" in errores:
                self.edit_usuario.setText("")
                self.edit_usuario.setPlaceholderText("usuario invalido")
            elif "Contraseña" in errores:
                self.edit_contraseña.setText("")
                self.edit_contraseña.setPlaceholderText("Contraseña incorrecta")


if __name__ == '__main__':
    app = QApplication([])
    ventana = VentanaInicio()
    ventana.crear_elementos()
    ventana.show()
    sys.exit(app.exec_())
