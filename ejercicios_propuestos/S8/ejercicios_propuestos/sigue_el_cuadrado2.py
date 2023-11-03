from random import randint
import sys
from time import sleep
from PyQt5.QtWidgets import QWidget, QApplication, QLabel,QHBoxLayout,QVBoxLayout,QLineEdit,QPushButton,QRadioButton,QSpinBox,QCheckBox
from PyQt5.QtGui import QPixmap,QColor
from PyQt5.QtCore import Qt, QThread,pyqtSignal

class SCuadrado(QWidget):
    senal=pyqtSignal(tuple)
    def __init__(self):
        super().__init__()
        
        self.init_gui()
    
    def init_gui(self):
        self.setGeometry(200, 100, 500, 500)
        self.setWindowTitle('sigue el cuadrado')
        self.cuadrado=QLabel(self)
        color=QColor(Qt.blue)
        pixeles = QPixmap(50,50)
        pixeles.fill(color)
        self.cuadrado.setPixmap(pixeles)
        self.cuadrado.move(randint(0,500),randint(0,500))
        self.senal.connect(self.posicionar_cuadrado)
        self.T=CuadradoThread(self.senal,self)
        

    def posicionar_cuadrado(self,posicion):
        self.cuadrado.move(*posicion)
        

    def mousePressEvent(self,event):
        en_x=self.cuadrado.x()<=event.x()<=(self.cuadrado.x()+150)
        en_y=self.cuadrado.y()<=event.y()<=(self.cuadrado.y()+150)
        if en_y and en_x:
            self.nueva_pos=(randint(0,450),randint(0,450))
            self.T.start()
           

class CuadradoThread(QThread):
    def __init__(self, senal,ventana):
        super().__init__()
        self.senal=senal
        self.ventana=ventana
        self.daemon=True
    def run(self):
        nueva_posicion=self.ventana.nueva_pos
        posicion_actual=(self.ventana.cuadrado.x(),self.ventana.cuadrado.y())
        while posicion_actual!=nueva_posicion:    
            n_x=self.ventana.cuadrado.x()
            n_y=self.ventana.cuadrado.y()
            if self.ventana.cuadrado.x()<nueva_posicion[0]:
                n_x=self.ventana.cuadrado.x()+1
            elif self.ventana.cuadrado.x()>nueva_posicion[0]:
                n_x=self.ventana.cuadrado.x()-1
            
            if self.ventana.cuadrado.y()<nueva_posicion[1]:
                n_y=self.ventana.cuadrado.y()+1

            elif self.ventana.cuadrado.y()>nueva_posicion[1]:
                n_y=self.ventana.cuadrado.y()-1
            posicion_actual=(n_x,n_y)  
            self.senal.emit(posicion_actual)
            sleep(0.0001)
            
        self.exit()
            
            

        
        
        
if __name__ == '__main__':
    app = QApplication([])
    ventana = SCuadrado()
    ventana.show()
    sys.exit(app.exec_())