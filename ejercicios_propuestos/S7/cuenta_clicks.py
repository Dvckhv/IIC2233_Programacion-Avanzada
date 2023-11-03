import sys
from PyQt5.QtWidgets import QWidget, QApplication, QLabel,QVBoxLayout,QPushButton
from PyQt5.QtGui import QPixmap


class CuentaClicks(QWidget):
    def __init__(self):
        super().__init__()
        self.contador_click=0
        self.init_gui()
    
    def init_gui(self):
        self.setGeometry(200, 100, 400, 200)
        self.setWindowTitle('cuenta clicks')

        self.label=QLabel("0 clicks",self)
        self.boton=QPushButton("Click",self)
        self.boton.resize(self.boton.sizeHint())
        self.boton.clicked.connect(self.contador)
        self.box=QVBoxLayout()
        self.box.addWidget(self.label)
        self.box.addWidget(self.boton)
        self.setLayout(self.box)

    def contador(self):
        self.contador_click+=1
        self.label.setText(f'{self.contador_click} clicks')
    

if __name__ == '__main__':
    app = QApplication([])
    ventana = CuentaClicks()
    ventana.show()
    sys.exit(app.exec_())