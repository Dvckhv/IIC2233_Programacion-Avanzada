import sys
from PyQt5.QtCore import pyqtSignal, QObject
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QLineEdit,QVBoxLayout,QHBoxLayout
from calculadora import Calculadora


class Ventana(QWidget):

    senal_mostrar_resultado=pyqtSignal(str)
    def __init__(self):
        super().__init__()
        self.senal_calcular=None
        self.init_gui()
    
    def init_gui(self):
        self.setGeometry(200, 100, 300, 500)
        self.setWindowTitle('Calculadora')

        self.valor1=QLabel("Valor 1:",self)
        self.edit_valor1=QLineEdit('',self)

        self.valor2=QLabel("Valor 2:",self)
        self.edit_valor2=QLineEdit('',self)


        self.boton_suma=QPushButton("+",self)
        self.boton_suma.resize(self.boton_suma.sizeHint())

        self.boton_resta=QPushButton("-",self)
        self.boton_resta.resize(self.boton_resta.sizeHint())

        self.boton_mult=QPushButton("X",self)
        self.boton_mult.resize(self.boton_mult.sizeHint())

        self.boton_div=QPushButton(":",self)
        self.boton_div.resize(self.boton_div.sizeHint())

        self.resultado=QLabel("Resultado: ",self)
        
        self.hbox=QHBoxLayout()
        self.hbox.addWidget(self.boton_suma)
        self.hbox.addWidget(self.boton_resta)
        self.hbox.addWidget(self.boton_mult)
        self.hbox.addWidget(self.boton_div)
       
        self.vbox1=QVBoxLayout()
        self.vbox1.addWidget(self.valor1)
        self.vbox1.addWidget(self.edit_valor1)
        self.vbox1.addWidget(self.valor2)
        self.vbox1.addWidget(self.edit_valor2)
        self.vbox1.addLayout(self.hbox)
        self.vbox1.addWidget(self.resultado)
        self.setLayout(self.vbox1)
        self.boton_div.clicked.connect(self.emisor)
        self.boton_mult.clicked.connect(self.emisor)
        self.boton_resta.clicked.connect(self.emisor)
        self.boton_suma.clicked.connect(self.emisor)
        self.show()
    def emisor(self):
        sender=self.sender()
        op=sender.text()
        if op=="+":
            operacion="sumar"
        elif op=="-":
            operacion="restar"
        elif op =="X":
            operacion="multiplicar"
        elif op == ":":
            operacion="dividir"
        dic={"operacion":operacion,"valor1": self.edit_valor1.text(),"valor2":self.edit_valor2.text()}
        self.senal_calcular.emit(dic)
        self.senal_mostrar_resultado.connect(self.imprimir_resultado)
    def imprimir_resultado(self,event):
        self.resultado.setText("Resultado: "+str(event))

if __name__ == '__main__':
    app = QApplication([])
    calculadora = Calculadora()
    ventana = Ventana()
    ventana.senal_calcular=calculadora.senal_calcular
    calculadora.senal_mostrar_resultado=ventana.senal_mostrar_resultado
    
    sys.exit(app.exec_())