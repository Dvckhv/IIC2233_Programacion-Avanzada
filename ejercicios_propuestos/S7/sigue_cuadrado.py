import imp
from random import randint
import sys
from PyQt5.QtWidgets import QWidget, QApplication, QLabel,QHBoxLayout,QVBoxLayout,QLineEdit,QPushButton,QRadioButton,QSpinBox,QCheckBox
from PyQt5.QtGui import QPixmap,QColor
from PyQt5.QtCore import Qt


class SCuadrado(QWidget):
    def __init__(self):
        super().__init__()
        
        self.init_gui()
    
    def init_gui(self):
        self.setGeometry(200, 100, 1000, 1000)
        self.setWindowTitle('sigue el cuadrado')
        self.cuadrado=QLabel(self)
        color=QColor(Qt.blue)
        pixeles = QPixmap(150,150)
        pixeles.fill(color)
        self.cuadrado.setPixmap(pixeles)
        self.cuadrado.move(randint(0,850),randint(0,850))

    def mousePressEvent(self,event):
        en_x=self.cuadrado.x()<=event.x()<=(self.cuadrado.x()+150)
        en_y=self.cuadrado.y()<=event.y()<=(self.cuadrado.y()+150)
        if en_y and en_x:
            self.cuadrado.move(randint(0,850),randint(0,850))


if __name__ == '__main__':
    app = QApplication([])
    ventana = SCuadrado()
    ventana.show()
    sys.exit(app.exec_())