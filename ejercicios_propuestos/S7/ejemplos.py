import sys
from PyQt5.QtWidgets import QWidget, QApplication


class MiVentana(QWidget):
    def __init__(self,x,y,ancho,alto,titulo):
        super().__init__()
        self.setGeometry(x, y,ancho,alto)
        self.setWindowTitle(str(titulo))


if __name__ == '__main__':
    app = QApplication([])
    ventana = MiVentana(100,300,1000,1000,"Ventana 0")
    ventana1 = MiVentana(500,300,200,400,"Ventana 1")
    ventana2 = MiVentana(1000,300,2000,100,"Ventana 2")
    ventana3 = MiVentana(2000,10,300,300,"ventana3")


    ventana.show()
    ventana1.show()
    ventana2.show()
    ventana3.show()
    sys.exit(app.exec_())
    