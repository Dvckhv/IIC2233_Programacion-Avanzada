from pickletools import TAKEN_FROM_ARGUMENT1
from random import randint
import sys
from time import sleep
from PyQt5.QtWidgets import QWidget, QApplication, QLabel,QHBoxLayout,QVBoxLayout,QLineEdit,QPushButton,QRadioButton,QSpinBox,QCheckBox
from PyQt5.QtGui import QPixmap,QColor
from PyQt5.QtCore import Qt,pyqtSignal,QTimer
class CuadradosCambiantes(QWidget):
    senal=pyqtSignal()
    def __init__(self):
        super().__init__()
        self.timer=QTimer()
        self.direccion_crec=True #crece o se achica el cuadrado 1
        self.timer.setInterval(1)
        self.timer.timeout.connect(self.senal)
        self.senal.connect(self.tamanos_cuadrados)
        
        self.init_gui()
    
    def init_gui(self):
        self.setGeometry(200, 100, 250, 250)
        self.setWindowTitle('Cuadrados Cambiantes')
        self.cuadrado1=QLabel(self)
        self.cuadrado2=QLabel(self)
        self.cuadrado1.move(10,50)
        self.cuadrado2.move(140,50)

        self.boton_iniciar=QPushButton("Iniciar",self)
        self.boton_detener=QPushButton("Detener",self)
        self.boton_detener.resize(self.boton_detener.sizeHint())
        self.boton_iniciar.resize(self.boton_iniciar.sizeHint())
        self.boton_iniciar.move(10,200)
        self.boton_detener.move(130,200)
        
        color=QColor(Qt.blue)
        pixeles = QPixmap(50,50)
        pixeles.fill(color)
        self.cuadrado1.setPixmap(pixeles)
        self.cuadrado2.setPixmap(pixeles)
        self.cuadrado1.saveGeometry()
        self.cuadrado1.setScaledContents(True)
        self.cuadrado2.saveGeometry()
        self.cuadrado2.setScaledContents(True)
        
        self.boton_detener.clicked.connect(self.pausar_cuadrados)
        self.boton_iniciar.clicked.connect(self.iniciar_cuadrados)

    
    
    
    def pausar_cuadrados(self):
        self.timer.stop()
    def iniciar_cuadrados(self):
        self.timer.start()
    
    def tamanos_cuadrados(self):
        if self.direccion_crec:
            self.cuadrado1.resize(self.cuadrado1.width()+1,self.cuadrado1.height()+1)
            self.cuadrado2.resize(self.cuadrado2.width()-1,self.cuadrado2.height()-1)
        else:
            self.cuadrado2.resize(self.cuadrado2.width()+1,self.cuadrado2.height()+1)
            self.cuadrado1.resize(self.cuadrado1.width()-1,self.cuadrado1.height()-1)
        sleep(0.01)
        
        tamaño1=(self.tamano_cuadrado1.width(),self.tamano_cuadrado1.height())
        if tamaño1==(75,75) or tamaño1==(25,25):
            self.direccion_crec=not(self.direccion_crec)
            
    @property
    def tamano_cuadrado1(self):
        return self.cuadrado1.size()

    @property
    def tamano_cuadrado2(self):
        return self.cuadrado2.size()


if __name__ == '__main__':
    app = QApplication([])


    ventana = CuadradosCambiantes()
    ventana.show()
    sys.exit(app.exec_())
        

    