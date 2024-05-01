from PyQt5.QtCore import QObject, pyqtSignal

import parametros as p


class LogicaInicio(QObject):

    senal_puntajes = pyqtSignal(list)
    senal_abrir_juego = pyqtSignal(dict)
    senal_errores = pyqtSignal(str)

    def __init__(self):
        super().__init__()

    def ranking_puntajes(self):
        with open(p.RUTA_PUNTAJES, "r") as archivo_puntajes:
            lista_puntajes = []
            for linea in archivo_puntajes:
                if len(linea.strip()) != 0:
                    lista_puntajes.append(linea.strip().split(","))

        lista_puntajes.sort(reverse=True, key=sort_puntajes)
        while len(lista_puntajes) < 5:
            lista_puntajes.append([" ", " "])

        self.senal_puntajes.emit(lista_puntajes)

    def comprobar_login(self, dic):
        Error = str()  # si no hay errores es un string vacio
        if dic["mapa"] == "":
            Error = "mapa"
        elif not dic["nombre"].isalnum():
            Error = "nombre"
        self.senal_errores.emit(Error)
        if Error == "":
            self.senal_abrir_juego.emit(dic)


def sort_puntajes(puntaje):
    return int(puntaje[1])


if __name__ == "__main__":
    pass
