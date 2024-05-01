from PyQt5.QtCore import QObject, pyqtSignal
from frontend.ventanas import VentanaEspera,VentanaInicio\
                                ,VentanaJuego,VentanaPost
from utils import log
class LogicaCliente(QObject):
    senal_rechazar_login=pyqtSignal(str)

    senal_ventana_espera=pyqtSignal()
    senal_usuario=pyqtSignal(dict)
    senal_boton=pyqtSignal(bool)

    senal_actualizar_juego=pyqtSignal(dict)
    senal_comenzar_juego=pyqtSignal()
    senal_terminar_juego=pyqtSignal(str,dict)
    def __init__(self,cliente):
        super().__init__()
        self.ventana_espera=VentanaEspera()
        self.ventana_inicio=VentanaInicio()
        self.ventana_juego=VentanaJuego()
        self.ventana_post=VentanaPost()
        self.cliente=cliente
        #CONEXIONES VENTANA INICIO
        self.ventana_inicio.senal_inicio.connect(self.validar_inicio)
        self.senal_rechazar_login.connect(self.ventana_inicio.login_rechazado)
        #CONEXIONES VENTANA ESPERA
        self.senal_ventana_espera.connect(self.mostrar_ventana_espera)
        self.senal_boton.connect(self.ventana_espera.administrador)
        self.senal_usuario.connect(self.ventana_espera.anadir_jugador)
        self.ventana_espera.senal_iniciar_juego.connect(self.iniciar_juego)
        #CONEXIONES VENTANA JUEGO
        self.senal_actualizar_juego.connect(self.ventana_juego.actualizar_juego)
        self.senal_comenzar_juego.connect(self.mostrar_ventana_juego)
        self.senal_terminar_juego.connect(self.mostrar_ventana_postjuego)
        self.senal_terminar_juego.connect(self.ventana_post.crear_ranking)
        self.ventana_juego.senal_dado.connect(self.enviar_senal_dado)
    def mostrar_ventana_inicio(self):
        self.ventana_inicio.show()

    def mostrar_ventana_espera(self):
        self.ventana_inicio.hide()
        self.ventana_espera.show()
    
    def mostrar_ventana_juego(self):
        self.ventana_espera.hide()
        self.ventana_juego.show()
    
    def mostrar_ventana_postjuego(self):
        self.ventana_juego.hide()
        self.ventana_post.show()

    def manejar_mensaje(self,mensaje):
        try:
            comando = mensaje["comando"]
        except KeyError:
            return {}


        #VENTANA DE INICIO
        if comando == "respuesta_validacion_login":
            if mensaje["estado"] == "aceptado":
                
                self.senal_ventana_espera.emit()
            else:
                self.senal_rechazar_login.emit(mensaje["motivo"])

        #VENTANA DE ESPERA
        elif comando == "anadir_usuario":
            nombre=mensaje["nombre"]
            color=mensaje["color"]
            self.senal_usuario.emit({"nombre":nombre,"color":color})


        #VENTANA DE JUEGO
        elif comando == "comenzar_juego":
            self.senal_comenzar_juego.emit()
        
        elif comando == "boton_comenzar":
            self.senal_boton.emit(mensaje["estado"])
        elif comando == "boton_dado":
            self.ventana_juego.activar_dado()
        elif comando == "actualizar_juego":   
            self.senal_actualizar_juego.emit(mensaje["datos"])
        elif comando == "terminar_juego":
            self.senal_terminar_juego.emit(mensaje["ganador"],mensaje["jugadores"])


    def validar_inicio(self,nombre):
        dic={"comando":"validar_nombre","nombre":nombre}
        log("enviando usuario")
        self.cliente.enviar(dic)
    def manejar_datos_jugadores(self,lista):
        dic={"comando":"datos_jugadores","datos":lista}
        self.cliente.enviar(dic)
    def iniciar_juego(self):
        dic={"comando":"boton_comenzar"}
        self.cliente.enviar(dic)
    def enviar_senal_dado(self):
        dic={"comando":"dado_lanzado"}
        self.cliente.enviar(dic)

    


    
    
                        
