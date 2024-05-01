
from random import choice, randint
from utils import data_json, log


class Logica:
    def __init__(self, servidor):
        super().__init__()
        self.servidor = servidor
        self.contador_jugadores = 0
        self.colores_disponibles = ["rojo", "amarillo", "verde", "azul"]
        self.nombres = dict()
        self.maximo = data_json("MAXIMO_JUGADORES")
        self.minimo = data_json("MINIMO_JUGADORES")
        self.jugadores = list()
        self.orden_ganadores = list()
        self.turno = 0
        self.jugador_en_turno = None
        self.admin = None
        self.en_juego = False

    def nuevo_jugador(self, nombre, socket_usuario):

        if self.contador_jugadores > self.maximo:
            self.servidor.enviar_mensaje(
                {"comando": "respuesta_validacion_login",
                 "estado": "rechazado", "motivo": "sala llena"}, socket_usuario)
            log(nombre +" fue rechazado por sala llena")
        elif nombre in self.nombres.values():
            self.servidor.enviar_mensaje(
                {"comando": "respuesta_validacion_login", 
                "estado": "rechazado", "motivo": "nombre usado"}, socket_usuario)
            log(nombre +" fue rechazado por nombre usado")
        elif not(nombre.isalpha()):
            self.servidor.enviar_mensaje({"comando": "respuesta_validacion_login",
                                         "estado": "rechazado", "motivo": "nombre invalido"},
                                          socket_usuario)
            log(nombre +" fue rechazado por nombre invalido, no era alfabetico")
                    
        elif not(data_json("LARGO_MIN") <= len(nombre) <= data_json("LARGO_MAX")):
            self.servidor.enviar_mensaje({"comando": "respuesta_validacion_login",
                                         "estado": "rechazado", "motivo": "nombre invalido"},
                                          socket_usuario)
            log(nombre +" fue rechazado por nombre invalido, no cumplia con el largo correcto") 
        elif self.en_juego:
            self.servidor.enviar_mensaje({"comando": "respuesta_validacion_login",
                                         "estado": "rechazado", "motivo": "partida en curso"}, 
                                         socket_usuario)
            log(nombre +" fue rechazado por que hay una partida en curso")
        else:
            self.contador_jugadores += 1
            self.nombres[nombre] = socket_usuario
            if self.contador_jugadores == 1:
                self.admin = socket_usuario

            color_jugador = choice(self.colores_disponibles)
            self.colores_disponibles.remove(color_jugador)
            dic = {"comando": "anadir_usuario", "estado": "aceptado",
                   "nombre": nombre, "color": color_jugador}
            self.jugadores.append(
                {"nombre": dic["nombre"], "color": dic["color"]})
            for jugador in self.jugadores:
                if jugador["nombre"] != nombre:
                    self.servidor.enviar_mensaje(
                        {"comando": "anadir_usuario", "estado": "aceptado", **jugador}, 
                        socket_usuario)
            self.servidor.enviar_broadcast(dic, self.nombres.values())
            self.servidor.enviar_mensaje(
                {"comando": "respuesta_validacion_login", "estado": "aceptado"}, socket_usuario)
            self.servidor.enviar_mensaje(
                {"comando": "boton_comenzar", "estado": self.contador_jugadores >= self.minimo},
                 self.admin)
            if self.contador_jugadores == self.maximo:
                self.comenzar_partida()

    def manejo_turno(self):
        jugador = self.jugadores[self.turno % len(self.jugadores)]
        if jugador["Jugando"]:
            self.jugador_en_turno = jugador
            log("comienza el turno de "+self.jugador_en_turno["nombre"])
            self.servidor.enviar_mensaje(
                {"comando": "boton_dado", "estado": True}, self.nombres[self.jugador_en_turno["nombre"]])
            self.turno += 1
        else:
            self.turno += 1
            self.manejo_turno()

    def actualizar_juego(self):
        numero = randint(1, 3) #se tira el dado en servidor
        log(self.jugador_en_turno["nombre"] + " tiro el dado y obtuvo " + str(numero))
        ruta = "camino_"+self.jugador_en_turno["color"]
        camino_ficha = data_json(ruta.upper())
        if self.jugador_en_turno["fichas_en_victoria"] == 0:
            self.jugador_en_turno["avanzado_ficha_1"] += self.manejar_movimiento(
                self.jugador_en_turno["avanzado_ficha_1"], numero)
            self.jugador_en_turno["posicion_ficha_1"] = camino_ficha[self.jugador_en_turno[
                                                                            "avanzado_ficha_1"]]
            self.jugador_en_turno["fichas_en_base"] = 1
            if self.jugador_en_turno["avanzado_ficha_1"] == 19:
                self.jugador_en_turno["fichas_en_victoria"] = 1
                self.jugador_en_turno["fichas_en_color"] = 0
            elif 16 < self.jugador_en_turno["avanzado_ficha_1"]:
                self.jugador_en_turno["fichas_en_color"] = 1
        else:
            self.jugador_en_turno["avanzado_ficha_2"] += self.manejar_movimiento(
                self.jugador_en_turno["avanzado_ficha_2"], numero)
            self.jugador_en_turno["posicion_ficha_2"] = camino_ficha[self.jugador_en_turno[
                                                                            "avanzado_ficha_2"]]
            self.jugador_en_turno["fichas_en_base"] = 0
            if self.jugador_en_turno["avanzado_ficha_2"] == 19:
                self.jugador_en_turno["fichas_en_victoria"] = 2
                self.jugador_en_turno["fichas_en_color"] = 0
                self.terminar_partida(self.jugador_en_turno["nombre"])
            elif 19 < self.jugador_en_turno["avanzado_ficha_2"]:
                self.jugador_en_turno["fichas_en_color"] = 1
        if self.jugador_en_turno["posicion_ficha_1"] == self.jugador_en_turno["posicion_ficha_2"]:
            self.jugador_en_turno["fichas_juntas"] = True
        else:
            self.jugador_en_turno["fichas_juntas"] = False
        self.revisar_fichas_comidas()
        self.manejo_turno()
        self.servidor.enviar_broadcast({"comando": "actualizar_juego", "datos":
                                        {"cambios": self.jugadores, 
                                        "en_turno": self.jugador_en_turno["nombre"], 
                                        "numero_dado": numero}}, self.nombres.values())

    def manejar_movimiento(self, avanzado, dado):
        if avanzado+dado <= 19:
            return dado
        else:
            return 19-(avanzado+dado)%19

    def revisar_fichas_comidas(self):
        if self.jugador_en_turno["fichas_en_victoria"] == 0:
            posicion_ficha_en_movimiento = self.jugador_en_turno["posicion_ficha_1"]
        else:
            posicion_ficha_en_movimiento = self.jugador_en_turno["posicion_ficha_2"]
        for jugador in self.jugadores:
            if jugador is not self.jugador_en_turno:
                ruta = "camino_"+jugador["color"]
                camino_ficha = data_json(ruta.upper())
                if jugador["posicion_ficha_1"] == posicion_ficha_en_movimiento:
                    jugador["fichas_en_base"] = 2
                    jugador["avanzado_ficha_1"] = 0
                    jugador["fichas_juntas"] = True
                    jugador["posicion_ficha_1"] = camino_ficha[0]
                    log(self.jugador_en_turno["nombre"] + " comio la ficha de"+jugador["nombre"])
                elif jugador["posicion_ficha_2"] == posicion_ficha_en_movimiento:
                    jugador["fichas_en_base"] = 1
                    jugador["avanzado_ficha_2"] = 0
                    jugador["posicion_ficha_2"] = camino_ficha[0]
                    log(self.jugador_en_turno["nombre"] + " comio la ficha de"+jugador["nombre"])

    def comenzar_partida(self):
        self.en_juego = True
        nombre_jugadores=list(self.nombres.keys())
        log("Partida comenzada con"+ ",".join(nombre_jugadores))
        for turno, jugador in enumerate(self.jugadores):
            jugador["Jugando"] = True
            jugador["fichas_juntas"] = True
            jugador["fichas_en_victoria"] = 0
            jugador["fichas_en_base"] = 2
            jugador["fichas_en_color"] = 0
            jugador["turno"] = turno
            jugador["avanzado_ficha_1"] = 0
            jugador["avanzado_ficha_2"] = 0
            jugador["posicion_ficha_1"] = data_json(
                "CAMINO_"+jugador["color"].upper())[0]
            jugador["posicion_ficha_2"] = data_json(
                "CAMINO_"+jugador["color"].upper())[0]
        
        self.servidor.enviar_broadcast({"comando": "comenzar_juego"},
                                                    self.nombres.values())
        self.manejo_turno()
        self.servidor.enviar_broadcast({"comando": "actualizar_juego", "datos": {
                                       "cambios": self.jugadores,
                                        "en_turno": self.jugador_en_turno["nombre"],
                                         "numero_dado": None}}, self.nombres.values())

    def terminar_partida(self, ganador):
        self.servidor.enviar_broadcast(
            {"comando": "terminar_juego", "ganador": ganador, "jugadores": self.jugadores}
            , self.nombres.values())
        log(f"Partida terminada, el triunfo es para {ganador}")
        self.en_juego = False
        self.jugadores = []

    def procesar_mensaje(self, mensaje, socket_usuario):
        """
        Procesa un mensaje recibido desde el cliente
        """
        try:
            log("procesando")
            comando = mensaje["comando"]
        except KeyError:
            return {}
        if comando == "validar_nombre":
            print("validando jugador")
            self.nuevo_jugador(mensaje["nombre"], socket_usuario)
        elif comando == "dado_lanzado":
            self.actualizar_juego()

        elif comando == "desconectar":
            self.eliminar_nombre(mensaje["id_usuario"])
            self.contador_jugadores -= 1
        elif comando == "boton_comenzar":
            self.comenzar_partida()
    
    def eliminar_nombre(self, socket):
        self.nombres.pop(socket)
        self.servidor.cant_jugadores -= 1
