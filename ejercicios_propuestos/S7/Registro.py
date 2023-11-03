import sys
from PyQt5.QtWidgets import QWidget, QApplication, QLabel,QHBoxLayout,QVBoxLayout,QLineEdit,QPushButton,QRadioButton,QSpinBox,QCheckBox
from PyQt5.QtGui import QPixmap


class RegistroRed(QWidget):
    def __init__(self):
        super().__init__()
        
        self.init_gui()
    
    def init_gui(self):
        self.setGeometry(200, 100, 1000, 1000)
        self.setWindowTitle('Inicio sesión')

        self.label_usuario=QLabel("Usuario:",self)
        self.edit_usuario=QLineEdit('',self)
        self.edit_usuario.resize(100, 20)

        self.label_genero=QLabel("Genero:",self)
        self.rbtn1 = QRadioButton('Femenino')
        self.rbtn2 = QRadioButton('Masculino')
        self.rbtn3 = QRadioButton('No Binario')
        self.rbtn4 = QRadioButton('No mencionar')

        self.label_edad=QLabel("Edad:",self)
        self.selec_edad=QSpinBox(self)


        self.label_configuracion=QLabel("Configuracion",self)
        self.priv=QCheckBox("Cuenta privada",self)
        self.noti=QCheckBox("Recibir noticias",self)
        self.terminos=QCheckBox("Acepto terminos y condiciones",self)

        self.boton=QPushButton("Ingresar",self)
        self.boton.resize(self.boton.sizeHint())
        

       
        self.vbox1=QVBoxLayout()
        self.vbox1.addWidget(self.rbtn1)
        self.vbox1.addWidget(self.rbtn2)
        self.vbox1.addWidget(self.rbtn3)
        self.vbox1.addWidget(self.rbtn4)

        self.vbox2=QVBoxLayout()
        self.vbox2.addWidget(self.priv)
        self.vbox2.addWidget(self.noti)
        self.vbox2.addWidget(self.terminos)

        self.hbox1=QHBoxLayout()
        
        self.hbox1.addWidget(self.label_usuario)
        self.hbox1.stretch(1)
        self.hbox1.addWidget(self.edit_usuario)
        self.hbox1.stretch(1)

        self.hbox2=QHBoxLayout()
        self.hbox2.addWidget(self.label_genero)
        self.hbox2.addLayout(self.vbox1)

        
        self.hbox3=QHBoxLayout()
        self.hbox3.addWidget(self.label_edad)
        self.hbox3.addWidget(self.selec_edad)

        self.hbox4=QHBoxLayout()
        self.hbox4.addWidget(self.label_configuracion)
        self.hbox4.addLayout(self.vbox2)


        self.mainbox=QVBoxLayout(self)
        self.mainbox.addStretch(1)
        self.mainbox.addLayout(self.hbox1)
        self.mainbox.addLayout(self.hbox2)
        self.mainbox.addLayout(self.hbox3)
        self.mainbox.addLayout(self.hbox4)
        self.mainbox.addStretch(1)
        self.mainbox.addWidget(self.boton)
    
        self.setLayout(self.mainbox)
        


if __name__ == '__main__':
    app = QApplication([])
    ventana = RegistroRed()
    ventana.show()
    sys.exit(app.exec_())