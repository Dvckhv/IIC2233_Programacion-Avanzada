from parametros import (AFINIDAD_HIT, AFINIDAD_INICIAL, AFINIDAD_PUBLICO_POP,
                        AFINIDAD_STAFF_POP, AFINIDAD_PUBLICO_ROCK,
                        AFINIDAD_STAFF_ROCK, AFINIDAD_PUBLICO_RAP,
                        AFINIDAD_STAFF_RAP, AFINIDAD_PUBLICO_REG,
                        AFINIDAD_STAFF_REG, AFINIDAD_ACCION_POP,
                        AFINIDAD_ACCION_ROCK, AFINIDAD_ACCION_RAP,
                        AFINIDAD_ACCION_REG, AFINIDAD_MIN, AFINIDAD_MAX)


class Artista:
    def __init__(self, nombre, genero, dia_presentacion,
                 hit_del_momento):
        self.nombre = nombre
        self.hit_del_momento = hit_del_momento
        self.genero = genero
        self.dia_presentacion = dia_presentacion
        self._afinidad_con_publico = AFINIDAD_INICIAL
        self._afinidad_con_staff = AFINIDAD_INICIAL
    @property
    def afinidad_con_publico(self):    
        return self._afinidad_con_publico
    @afinidad_con_publico.setter
    def afinidad_con_publico(self,valor):
        if self._afinidad_con_publico+valor<0:
            self._afinidad_con_publico=0
        elif self._afinidad_con_publico+valor>100:
            self._afinidad_con_publico=100
        else:
            self._afinidad_con_publico+=valor
    @property
    def afinidad_con_staff(self):
        return self._afinidad_con_staff
    @afinidad_con_staff.setter
    def afinidad_con_staff(self,valor):
        if self._afinidad_con_staff+valor < 0:
            self._afinidad_con_staff = 0
        elif self._afinidad_con_publico+valor > 100:
            self._afinidad_con_staff = 100
        else:
            self._afinidad_con_staff+=valor
    @property
    def animo(self):
        return int(self.afinidad_con_publico*0.5+self.afinidad_con_staff*0.5)

    def recibir_suministros(self, suministro):
        preafinidad=self.afinidad_con_staff
        self.afinidad_con_staff += suministro.valor_de_satisfaccion
        if preafinidad>self.afinidad_con_staff:
            print(f"{self.nombre} recibió {suministro.nombre} en malas condiciones.")
        else:
            print(f"{self.nombre} recibió un {suministro.nombre} a tiempo!")

    def cantar_hit(self):
        self.afinidad_con_publico += AFINIDAD_HIT
        print(f"{self.nombre} está tocando su hit: {self.hit_del_momento}!")

    def __str__(self):
        return(f"Nombre: {self.nombre}\nGenero: {self.genero}\n Animo: {self.animo}")
        pass

class ArtistaPop(Artista):
    def __init__(self,nombre,genero,dia_presentacion,hit_del_momento): #edite estos *args y *kargs ya que no me funcionaban bien
        super().__init__(nombre,genero,dia_presentacion,hit_del_momento)
        self.accion="Cambio de vestuario"
        self._afinidad_con_publico=AFINIDAD_PUBLICO_POP
        self._afinidad_con_publico=AFINIDAD_STAFF_POP

    def accion_especial(self):
        print(f"{self.nombre} hara un {self.accion}")
        self.afinidad_con_publico+=AFINIDAD_ACCION_POP
    @property
    def animo(self):
        animo_actual=super().animo
        if animo_actual<10:
            print(f"ArtistaPop peligrando en el concierto. Animo: {animo_actual}")
        return animo_actual


class ArtistaRock(Artista):
    def __init__(self,nombre,genero,dia_presentacion,hit_del_momento):
        super().__init__(nombre,genero,dia_presentacion,hit_del_momento)
        self.accion="Solo de guitarra"
        self._afinidad_con_publico=AFINIDAD_PUBLICO_ROCK
        self._afinidad_con_publico=AFINIDAD_STAFF_ROCK

    def accion_especial(self):
        print(f"{self.nombre} hara un {self.accion}")
        self.afinidad_con_publico+=AFINIDAD_ACCION_ROCK
    @property
    def animo(self):
        animo_actual=super().animo
        if animo_actual<10:
            print(f"ArtistaRock peligrando en el concierto. Animo: {animo_actual}")
        return animo_actual


class ArtistaRap(Artista):
    def __init__(self,nombre,genero,dia_presentacion,hit_del_momento):
        super().__init__(nombre,genero,dia_presentacion,hit_del_momento)
        self.accion="Doble tempo"
        self._afinidad_con_publico=AFINIDAD_PUBLICO_RAP
        self._afinidad_con_publico=AFINIDAD_STAFF_RAP

    def accion_especial(self):
        print(f"{self.nombre} hara un {self.accion}")
        self.afinidad_con_publico+=AFINIDAD_ACCION_RAP
    @property
    def animo(self):
        animo_actual=super().animo
        if animo_actual<10:
            print(f"ArtistaRap peligrando en el concierto. Animo: {animo_actual}")
        return animo_actual


class ArtistaReggaeton(Artista):
    def __init__(self,nombre,genero,dia_presentacion,hit_del_momento):
        super().__init__(nombre,genero,dia_presentacion,hit_del_momento)
        self.accion="Solo de guitarra"
        self._afinidad_con_publico=AFINIDAD_PUBLICO_REG
        self._afinidad_con_publico=AFINIDAD_STAFF_REG

    def accion_especial(self):
        print(f"{self.nombre} hara un {self.accion}")
        self.afinidad_con_publico+=AFINIDAD_ACCION_REG
    @property
    def animo(self):
        animo_actual=super().animo
        if animo_actual<10:
            print(f"ArtistaReggaeton peligrando en el concierto. Animo: {animo_actual}")
        return animo_actual
