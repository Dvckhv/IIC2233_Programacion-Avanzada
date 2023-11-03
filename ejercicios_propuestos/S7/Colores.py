import imp
from random import randint
import sys
from PyQt5.QtWidgets import QWidget, QApplication, QLabel,QHBoxLayout,QVBoxLayout,QLineEdit,QPushButton,QRadioButton,QSpinBox,QCheckBox
from PyQt5.QtGui import QPixmap,QColor
from PyQt5.QtCore import Qt
from bs4 import Stylesheet


class SCuadrado(QWidget):
    def __init__(self):
        super().__init__()
        
        self.init_gui()
    
    def init_gui(self):
        self.setGeometry(200, 100, 800, 800)
        self.setWindowTitle('colores')
        self.label=QLabel("Blanco",self)
        self.label.move(120,80)
        self.cuadrado=QLabel(self)
        color=QColor(Qt.white)
        self.pixeles = QPixmap(100,100)
        self.pixeles.fill(color)
        self.cuadrado.setPixmap(self.pixeles)
        self.cuadrado.move(100,100)
        hlayouts=QHBoxLayout(self)
        container = QWidget(self)
        layout = QHBoxLayout(container )
        hlayouts.addWidget(container)
        container.setStyleSheet('''.QLabel {
    color: black;
    font-weight: bold;
    border: 0px;
    margin: 0px;
    padding: 0px;
}
.QWidget {
background-color:blue;
border-radius: 10px; 
border: 2px groove gray;
border-style: outset;
}''')
        
        nombre=QLabel("Hola")
        layout.addWidget(nombre)
        layout.addWidget(QLabel("adios"))
        container2 = QWidget(self)
        layout2= QHBoxLayout(container2 )
        hlayouts.addWidget(container2)
        container2.setStyleSheet("background-color:blue;")
        layout2.addWidget(QLabel("Hola"))
        layout2.addWidget(QLabel("adios"))
        

    def keyPressEvent(self, event):
        if event.key()==86:
            self.label.setText("Verde")
            self.pixeles.fill(QColor(Qt.green))
        if event.key()==82:
            self.label.setText("Rojo")
            self.pixeles.fill(QColor(Qt.red))
        if event.key()==65:
            self.label.setText("Azul")
            self.pixeles.fill(QColor(Qt.blue))
        if event.key()==66:
            self.label.setText("Blanco")
            self.pixeles.fill(QColor(Qt.white))
        self.cuadrado.setPixmap(self.pixeles)


if __name__ == '__main__':
    app = QApplication([])
    ventana = SCuadrado()
    ventana.show()
    sys.exit(app.exec_())