import sys
from PyQt5.QtWidgets import QWidget, QApplication, QLabel,QHBoxLayout,QVBoxLayout,QLineEdit,QPushButton
from PyQt5.QtGui import QPixmap


class RedSocial(QWidget):
    def __init__(self):
        super().__init__()
        
        self.init_gui()
    
    def init_gui(self):
        self.setGeometry(200, 100, 1000, 1000)
        self.setWindowTitle('Inicio sesión')

        self.label_usuario=QLabel("Usuario:",self)
        self.edit_usuario=QLineEdit('',self)
        self.edit_usuario.resize(100, 20)

        self.label_contraseña=QLabel("Contraseña:",self)
        self.edit_contraseña=QLineEdit('',self)
        self.edit_contraseña.resize(100, 20)

        self.label_correo=QLabel("Correo:",self)
        self.edit_correo=QLineEdit('',self)
        self.edit_correo.resize(100, 20)

        self.boton=QPushButton("Ingresar",self)
        self.boton.resize(self.boton.sizeHint())
        
        self.imagen=QLabel(self)
        pixeles = QPixmap("img.jpg")
        self.imagen.setPixmap(pixeles)
        self.imagen.resize(200,200)
        

       
        
        self.vbox1=QVBoxLayout()
        self.vbox1.addWidget(self.label_usuario)
        self.vbox1.addWidget(self.label_correo)
        self.vbox1.addWidget(self.label_contraseña)

        self.vbox2=QVBoxLayout()
        self.vbox2.addWidget(self.edit_usuario)
        self.vbox2.addWidget(self.edit_correo)
        self.vbox2.addWidget(self.edit_contraseña)

        self.hbox=QHBoxLayout()
        self.hbox.addLayout(self.vbox1)
        self.hbox.addLayout(self.vbox2)
        self.mainbox=QVBoxLayout(self)
        self.mainbox.addWidget(self.imagen)
        self.mainbox.addStretch(1)
        self.mainbox.addLayout(self.hbox)
        self.mainbox.addStretch(1)
        self.mainbox.addWidget(self.boton)
    
        self.setLayout(self.mainbox)
        


if __name__ == '__main__':
    app = QApplication([])
    ventana = RedSocial()
    ventana.show()
    sys.exit(app.exec_())