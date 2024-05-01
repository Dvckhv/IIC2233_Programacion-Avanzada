import sys

from PyQt5.QtWidgets import QApplication
from backend.logica_inicio import LogicaInicio
from backend.logica_juego import LogicaJuego
from frontend.ventana_inicio import VentanaInicio, VentanaRanking, VentanaPrincipal
from frontend.ventana_juego import VentanaJuego
from frontend.ventana_postnivel import VentanaPost


if __name__ == '__main__':
    def hook(type, value, traceback):
        print(type)
        print(traceback)
    sys.__excepthook__ = hook
    app = QApplication([])
    app.setStyleSheet('''QLabel { color: white; font-size: 16pt }
    QPushButton {
                 border-radius: 10px; border: 2px groove gray; border-style: outset;
            }
            QPushButton:pressed {
                 color: rgb(255,255,255);
            }
        ''')
    # Instanciación de ventanas
    ventana_inicio = VentanaInicio()
    ventana_juego = VentanaJuego()
    ventana_ranking = VentanaRanking()
    ventana_principal = VentanaPrincipal()
    ventana_post = VentanaPost()

    # Instanciación de lógica
    logica_juego = LogicaJuego()
    logica_inicio = LogicaInicio()

    # ~~ Conexiones de señales ~~
    ventana_inicio.senal_ventana_principal.connect(ventana_principal.iniciar_ventana)
    ventana_inicio.senal_ranking.connect(ventana_ranking.show)
    ventana_inicio.senal_ranking.connect(logica_inicio.ranking_puntajes)

    ventana_ranking.senal_volver.connect(ventana_inicio.show)

    logica_inicio.senal_puntajes.connect(ventana_ranking.asignar_puestos)
    logica_inicio.senal_abrir_juego.connect(
        logica_juego.establecer_condiciones_iniciales)
    logica_inicio.senal_errores.connect(ventana_principal.mostrar_error)

    ventana_principal.senal_comprobar_datos.connect(
        logica_inicio.comprobar_login)
    ventana_juego.senal_tecla.connect(logica_juego.manejo_teclas)
    ventana_juego.senal_salir.connect(logica_juego.resumen_nivel)
    ventana_juego.senal_click.connect(logica_juego.click_bala)

    logica_juego.senal_mostrar_mapa.connect(ventana_juego.generar_mapa)
    logica_juego.senal_mostrar_mapa.connect(ventana_principal.hide)
    logica_juego.senal_disparar.connect(ventana_juego.disparo)
    logica_juego.senal_sonido.connect(ventana_juego.emitir_sonido)
    logica_juego.mira.senal_movimiento_mira.connect(ventana_juego.mover_mira)
    logica_juego.senal_actualizar_aliens.connect(ventana_juego.mover_aliens)
    logica_juego.senal_alien_morir.connect(ventana_juego.alien_muerto)
    logica_juego.senal_explosion.connect(ventana_juego.explosion)
    logica_juego.senal_actualizar_labels.connect(ventana_juego.labels)
    logica_juego.senal_perro.connect(ventana_juego.terminator_dog)
    logica_juego.senal_reinicio_mapa.connect(ventana_juego.reiniciar_mapa)
    logica_juego.senal_postjuego.connect(ventana_juego.hide)
    logica_juego.senal_postjuego.connect(ventana_post.asignar_labels)
    logica_juego.senal_bala_extra.connect(ventana_juego.aparicion_bala)
    logica_juego.senal_estrella.connect(ventana_juego.aparicion_estrella)
    logica_juego.senal_bomba.connect(ventana_juego.aparicion_bomba)

    ventana_post.senal_salir.connect(ventana_inicio.show)
    ventana_post.senal_salir.connect(logica_juego.guardar_puntaje)
    ventana_post.senal_siguiente_nivel.connect(logica_juego.establecer_condiciones_nuevas)

    
    ventana_inicio.show()
    app.exec()
