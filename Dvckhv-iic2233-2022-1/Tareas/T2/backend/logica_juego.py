from random import random, uniform, choice
from PyQt5.QtCore import QObject, pyqtSignal, QTimer
from backend.objetos_juego import Mira, Aliens, SecuenciasImagen, Bala, Estrella, Bomba
import parametros as p


class LogicaJuego(QObject):
    senal_mostrar_mapa = pyqtSignal(dict)
    senal_disparar = pyqtSignal(list)
    senal_actualizar_aliens = pyqtSignal(list)
    senal_alien_morir = pyqtSignal(int)
    senal_actualizar_labels = pyqtSignal(dict)
    senal_explosion = pyqtSignal(list)
    senal_sonido = pyqtSignal(str)
    senal_perro = pyqtSignal(dict)
    senal_postjuego = pyqtSignal(dict)
    senal_reinicio_mapa = pyqtSignal()
    senal_bala_extra = pyqtSignal(tuple)
    senal_estrella = pyqtSignal(tuple)
    senal_bomba = pyqtSignal(tuple)

    def __init__(self):
        super().__init__()
        self.combinacion_teclas = str()
        self.pausado = False
        self.ponderador = 0
        self.balas_inf = False
        self.max_x = p.MAX_X_VENTANA
        self.max_y = (p.MAX_Y_VENTANA-p.ALTO_MENU)
        self.mira = Mira(self.max_x, self.max_y)

        self.bala_extra = Bala(self.senal_bala_extra)
        self.estrella = Estrella(self.senal_estrella)
        self.bomba = Bomba(self.senal_bomba)

    def establecer_condiciones_iniciales(self, dic):
        # TIMERS DE CONTROL
        self.timers = []
        self.timer_juego = QTimer()
        self.timer_juego.setInterval(1000)
        self.timer_juego.timeout.connect(self.tiempo_juego)
        self.timers.append(self.timer_juego)

        self.aliens_vivos = 0
        self.aliens_generados = []
        self.generador_aliens = QTimer()
        self.generador_aliens.setInterval(p.TASA_ACTUALIZACION)
        self.generador_aliens.timeout.connect(self.manejo_de_alien)
        self.timers.append(self.generador_aliens)

        self.timer_actualizar_mira = QTimer()
        self.timer_actualizar_mira.setInterval(p.TASA_ACTUALIZACION)
        self.timer_actualizar_mira.timeout.connect(self.actualizar_mira)
        self.timers.append(self.timer_actualizar_mira)

        self.timer_actualizar_labels = QTimer()
        self.timer_actualizar_labels.setInterval(p.TASA_ACTUALIZACION)
        self.timer_actualizar_labels.timeout.connect(self.actualizar_labels)
        self.timers.append(self.timer_actualizar_labels)

        self.timer_evento = QTimer()
        self.timer_evento.setInterval(p.TASA_EVENTO)
        self.timer_evento.timeout.connect(self.crear_evento)
        self.timers.append(self.timer_evento)

        # PRIMER NIVEL
        self.balas_inf = False
        self.pausado = False
        self.bala_extra.usado = False
        self.nivel = 1
        self.puntaje_total = 0
        self.aliens_totales = self.nivel*2
        balas = self.aliens_totales*2
        self.mira.cambio_nivel(balas)
        self.bala_extra.apagar()
        self.estrella.apagar()
        self.bomba.apagar()
    
        self.nombre_jugador = dic["nombre"]
        self.mapa = dic["mapa"]

        if self.mapa == "Tutorial Lunar":
            self.ponderador = p.PONDERADOR_TUTORIAL
            self.alien = p.RUTA_ALIENV
            self.alien_muerto = p.RUTA_ALIENV_MUERTO
            self.fondo = p.RUTA_LUNA
            self.ancho_alien = p.ANCHO_ALIENV
            self.alto_alien = p.ALTO_ALIENV
            self.tdog_alien = p.RUTA_TERMINATOR_DOG_ALIENV
        if self.mapa == "Entrenamiento en Júpiter":
            self.ponderador = p.PONDERADOR_ENTRENAMIENTO
            self.alien = p.RUTA_ALIENR
            self.alien_muerto = p.RUTA_ALIENR_MUERTO
            self.fondo = p.RUTA_JUPITER
            self.ancho_alien = p.ANCHO_ALIENR
            self.alto_alien = p.ALTO_ALIENR
            self.tdog_alien = p.RUTA_TERMINATOR_DOG_ALIENR
        if self.mapa == "Invasión Intergaláctica":
            self.ponderador = p.PONDERADOR_INVASION
            self.alien = p.RUTA_ALIENA
            self.alien_muerto = p.RUTA_ALIENA_MUERTO
            self.fondo = p.RUTA_INVASION
            self.ancho_alien = p.ANCHO_ALIENA
            self.alto_alien = p.ALTO_ALIENA
            self.tdog_alien = p.RUTA_TERMINATOR_DOG_ALIENA

        Aliens.numero_alien = 0
        self.velocidad_alien = (
            p.VELOCIDAD_ALIEN[0] / self.ponderador, p.VELOCIDAD_ALIEN[1]/self.ponderador)
        self.tiempo_nivel = int(p.DURACION_NIVEL_INICIAL * self.ponderador)

        self.sprites = {"alien vivo": self.alien, "alien muerto": self.alien_muerto, "dimensiones alien":
                        (self.ancho_alien, self.alto_alien), "cantidad aliens": self.aliens_totales, "fondo": self.fondo}
        self.senal_mostrar_mapa.emit(self.sprites)
        for timer in self.timers:
            timer.start()

    def tiempo_juego(self):
        if not self.pausado:
            self.tiempo_nivel -= 1
        if self.tiempo_nivel == 0:
            self.revision_condiciones()

    def manejo_de_alien(self):
        self.revision_condiciones()
        if self.aliens_vivos < 2 and len(self.aliens_generados) < self.aliens_totales:
            nuevo_alien = Aliens(self.max_x, self.max_y,
                                 self.velocidad_alien, self.senal_alien_morir, self.ancho_alien, self.alto_alien)
            nuevo_alien.start()
            self.aliens_generados.append(nuevo_alien)
            self.aliens_vivos += 1
        lista_posiciones_aliens = []
        for alien in self.aliens_generados:
            index, pos_x, pos_y = alien.numero_alien, alien.x, alien.y
            lista_posiciones_aliens.append(
                [index, (pos_x, pos_y), alien.seguir])
        self.senal_actualizar_aliens.emit(lista_posiciones_aliens)

    def congelar_aliens(self):
        for alien in self.aliens_generados:
            alien.congelado = not(alien.congelado)

    def revision_condiciones(self):
        if not self.pausado:
            if len(self.aliens_generados) == self.aliens_totales and self.aliens_vivos == 0:
                self.resumen_nivel(True)
            elif self.mira.balas_restantes == 0 or self.tiempo_nivel == 0:
                self.resumen_nivel(False)

    def manejo_teclas(self, tecla):
        if tecla == p.TECLA_PAUSA:
            self.pausado = not(self.pausado)
            self.congelar_aliens()
            self.congelar_bonus()

        if not self.pausado:
            self.combinacion_teclas += tecla
            if self.combinacion_teclas in p.CHEAT[0]:  # OVNI

                if len(self.combinacion_teclas) == len(p.CHEAT[0]):
                    self.balas_inf = True
                    self.combinacion_teclas = ""
            elif self.combinacion_teclas in p.CHEAT[1]:  # CIA

                if len(self.combinacion_teclas) == len(p.CHEAT[1]):
                    self.resumen_nivel(True)
                    self.combinacion_teclas = ""
            else:
                self.combinacion_teclas = ""

            if tecla == p.TECLA_ARRIBA:
                self.mira.y -= p.RAPIDEZ_MIRA
            elif tecla == p.TECLA_ABAJO:
                self.mira.y += p.RAPIDEZ_MIRA
            elif tecla == p.TECLA_DERECHA:
                self.mira.x += p.RAPIDEZ_MIRA
            elif tecla == p.TECLA_IZQUIERDA:
                self.mira.x -= p.RAPIDEZ_MIRA
            elif tecla == p.TECLA_DISPARO:
                self.manejo_disparo()
                if self.mira.balas_restantes == 0:
                    self.revision_condiciones()

    def manejo_disparo(self):
        if not(self.balas_inf):
            self.mira.balas_restantes -= 1
        self.thread_disparo = SecuenciasImagen(
            [p.RUTA_MIRA_DISPARO, p.RUTA_MIRA], self.senal_disparar)
        self.thread_disparo.start()
        self.senal_sonido.emit(p.RUTA_DISPARO)
        posicion_mira = (
            self.mira.x+self.mira.centro[0], self.mira.y+self.mira.centro[1])

        self.disparar_alien(posicion_mira)
        self.disparar_eventos(posicion_mira)
        self.revision_condiciones()

    def disparar_alien(self, posicion_mira):
        for alien in self.aliens_generados:
            if (alien.x < posicion_mira[0] < alien.x+self.ancho_alien and
                    alien.y < posicion_mira[1] < alien.y+self.alto_alien and alien.vivo):
                self.actualizar_labels()
                self.thread_explosion = SecuenciasImagen([p.RUTA_EXPLOSION_1,
                    p.RUTA_EXPLOSION_2,p.RUTA_EXPLOSION_3, "end"],self.senal_explosion)
                self.thread_explosion.start()
                alien.morir()
                self.aliens_vivos -= 1

    def disparar_eventos(self, posicion_mira):
        if self.estrella.activo:
            if (self.estrella.x < posicion_mira[0] < self.estrella.x+self.estrella.ancho and
                    self.estrella.y < posicion_mira[1] < self.estrella.y+self.estrella.alto):
                self.thread_explosion = SecuenciasImagen([p.RUTA_EXPLOSION_1, 
                    p.RUTA_EXPLOSION_2,p.RUTA_EXPLOSION_3, "end"],self.senal_explosion)
                self.thread_explosion.start()
                self.tiempo_nivel -= p.TIEMPO_PERDIDO
                self.bomba.apagar()
                
        if self.bomba.activo:
            if (self.bomba.x < posicion_mira[0] < self.bomba.x+self.bomba.ancho and
                    self.bomba.y < posicion_mira[1] < self.bomba.y+self.bomba.alto):
                self.thread_explosion = SecuenciasImagen([p.RUTA_EXPLOSION_1, p.RUTA_EXPLOSION_2,
                    p.RUTA_EXPLOSION_3, "end"],self.senal_explosion)
                self.thread_explosion.start()
                self.congelar_aliens()
                self.timer_congelado = QTimer()
                self.timer_congelado.setInterval(p.TIEMPO_CONGELAMIENTO)
                self.timer_congelado.setSingleShot(True)
                self.timer_congelado.timeout.connect(self.congelar_aliens)
                self.timer_congelado.start()
                self.bomba.apagar()

    def actualizar_mira(self):
        self.mira.senal_movimiento_mira.emit((self.mira.x, self.mira.y))

    def actualizar_labels(self):
        dic = {"nivel": self.nivel, "balas": self.mira.balas_restantes,
               "puntaje": self.puntaje_total, "tiempo": self.tiempo_nivel}
        self.senal_actualizar_labels.emit(dic)

    def resumen_nivel(self, bool_pasado=False):
        self.pausado = True
        for timer in self.timers:
            timer.stop()
        self.puntaje_obtenido = 0
        if bool_pasado:
            self.puntaje_obtenido = self.aliens_totales * 100
            self.puntaje_obtenido += (self.tiempo_nivel*30 +
                                      self.mira.balas_restantes*70)*self.nivel
            self.puntaje_obtenido /= self.ponderador
            self.puntaje_total += int(self.puntaje_obtenido)
            self.animacion_terminator_dog()
        else:
            self.siguiente_nivel(False)

    def siguiente_nivel(self, pasado=True):
        datos_resumen = {"nivel": self.nivel, "balas restantes": self.mira.balas_restantes,
                         "tiempo restante": self.tiempo_nivel, "puntaje total": self.puntaje_total,
                         "puntaje nivel": int(self.puntaje_obtenido), "pasado": pasado,
                         "alien": self.alien,"dimensiones":(self.ancho_alien,self.alto_alien)}
        self.senal_postjuego.emit(datos_resumen)
        self.senal_reinicio_mapa.emit()

    def animacion_terminator_dog(self):
        dic_perro = {"risa": p.RUTA_RISA, "alien": self.tdog_alien}
        self.senal_perro.emit(dic_perro)
        self.timer_risa = QTimer(self)
        self.timer_risa.setSingleShot(True)
        self.timer_risa.setInterval(p.TIEMPO_TERMINATOR_DOG)
        self.timer_risa.timeout.connect(self.siguiente_nivel)
        self.timer_risa.start()

    def establecer_condiciones_nuevas(self):
        self.nivel += 1
        self.tiempo_nivel = int(p.DURACION_NIVEL_INICIAL * (self.ponderador**(self.nivel)))
        self.aliens_totales = self.nivel*2
        balas = self.aliens_totales*2
        self.mira.cambio_nivel(balas)
        self.bala_extra.apagar()
        self.estrella.apagar()
        self.bomba.apagar()
        Aliens.numero_alien = 0
        self.aliens_generados = []
        self.aliens_vivos = 0
        self.velocidad_alien = (
            self.velocidad_alien[0] / self.ponderador, self.velocidad_alien[1]/self.ponderador)
        self.actualizar_labels()

        self.timer_juego.setInterval(1000)
        self.pausado = False
        self.balas_inf = False
        for timer in self.timers:
            timer.start()

        self.sprites = {"alien vivo": self.alien, "alien muerto": self.alien_muerto,
        "fondo": self.fondo, "dimensiones alien": (self.ancho_alien, self.alto_alien),
         "cantidad aliens": self.aliens_totales }
        self.senal_mostrar_mapa.emit(self.sprites)

    def guardar_puntaje(self):
        with open(p.RUTA_PUNTAJES, "r", encoding="utf-8") as archivo_puntajes:
            nueva_linea = False
            if archivo_puntajes.readlines()[-1][-1] == "\n":
                nueva_linea = True

        with open(p.RUTA_PUNTAJES, "a", encoding="utf-8") as archivo_puntajes:
            if not(nueva_linea):
                print("", file=archivo_puntajes)
            linea_archivo = str(self.nombre_jugador) + \
                ","+str(self.puntaje_total)
            print(linea_archivo, file=archivo_puntajes)

    #ABAJO BONUS
    def crear_evento(self):
        prob = random()
        if p.PROBABILIDAD_EVENTO_BONUS > prob and not(self.pausado):
            evento_elegido = choice(p.EVENTOS)
            if evento_elegido == "estrella" and not(self.estrella.activo):
                self.estrella.x = uniform(0, self.max_x-self.estrella.ancho)
                self.estrella.y = uniform(0, self.max_y-self.estrella.alto)
                self.timer_apagar_estrella = QTimer()
                self.timer_apagar_estrella.setSingleShot(True)
                self.timer_apagar_estrella.setInterval(p.TIEMPO_BALA)
                self.timer_apagar_estrella.timeout.connect(
                    self.estrella.apagar)
                self.estrella.activar()
                self.timer_apagar_estrella.start()

            elif evento_elegido == "bala" and not(self.bala_extra.activo)\
                    and not(self.bala_extra.usado):
                self.bala_extra.x = uniform(
                    0, self.max_x-self.bala_extra.ancho)
                self.bala_extra.y = uniform(0, self.max_y-self.bala_extra.alto)
                self.timer_apagar_bala = QTimer()
                self.timer_apagar_bala.setSingleShot(True)
                self.timer_apagar_bala.setInterval(p.TIEMPO_BALA)
                self.timer_apagar_bala.timeout.connect(self.bala_extra.apagar)
                self.timer_apagar_bala.start()
                self.bala_extra.activar()
            elif evento_elegido == "bomba" and not(self.bomba.activo):
                self.bomba.x = uniform(0, self.max_x-self.bomba.ancho)
                self.bomba.y = uniform(0, self.max_y-self.bomba.alto)
                self.timer_apagar_bomba = QTimer()
                self.timer_apagar_bomba.setSingleShot(True)
                self.timer_apagar_bomba.setInterval(p.TIEMPO_BALA)
                self.timer_apagar_bomba.timeout.connect(self.bomba.apagar)
                self.timer_apagar_bomba.start()
                self.bomba.activar()

    def click_bala(self, event):
        if not(self.pausado):
            if self.bala_extra.x <= event.x() <= self.bala_extra.x+self.bala_extra.ancho \
                    and self.bala_extra.y <= event.y() <= self.bala_extra.y+self.bala_extra.alto\
                    and self.bala_extra.activo:
                self.mira.balas_restantes += 3
                self.bala_extra.apagar()
                self.bala_extra.usado = True

    def congelar_bonus(self):
        if self.bala_extra.activo:
            if self.timer_apagar_bala.isActive():
                self.timer_apagar_bala.stop()
            else:
                self.timer_apagar_bala.start()

        if self.bomba.activo:
            if self.timer_apagar_bomba.isActive():
                self.timer_apagar_bomba.stop()
            else:
                self.timer_apagar_bomba.start()
                
        if self.estrella.activo:
            if self.timer_apagar_estrella.isActive():
                self.timer_apagar_estrella.stop()
            else:
                self.timer_apagar_estrella.start()
