from PyQt5.QtCore import QObject, pyqtSignal

import parametros as p


class LogicaInicio(QObject):

    senal_respuesta_validacion = pyqtSignal(bool, list)
    senal_abrir_juego = pyqtSignal(str)

    def __init__(self):
        super().__init__()

    def comprobar_usuario(self, tupla_respuesta):
        Login=True
        Errores=list()
        nombre=tupla_respuesta[0]
        
        contraseña=tupla_respuesta[1]
        if len(nombre)>=p.MAX_CARACTERES:
            Login=False
            Errores.append("Usuario")
        elif contraseña!=p.PASSWORD:
            Login=False
            Errores.append("Contraseña")
        self.senal_respuesta_validacion.emit(Login,Errores)
        if Login==True:
            self.senal_abrir_juego.emit(nombre)

