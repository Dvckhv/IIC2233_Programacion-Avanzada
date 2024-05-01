from abc import ABC, abstractmethod
from random import choice, randint, random
from unidades import Guerrero, Mago, MagoGuerrero
from parametros import PROB_CRITICO_MURO, PROB_CRITICO_CATAPULTA, \
                       HP_MUROCATAPULTA, PROB_CRITICO_MURO_CATAPULTA, \
                       HP_BARRACAS, HP_MURO, HP_CATAPULTA


# Recuerda que es una clase abstracta
class Estructura(ABC):

    def __init__(self, edad, *args):
        # No modificar
        super().__init__(*args)
        self.edad = edad
        self.asignar_atributos_segun_edad()

    @abstractmethod
    def asignar_atributos_segun_edad(self):
        pass

    @abstractmethod
    def accion(self):
        pass

    @abstractmethod
    def avanzar_edad(self):
        pass

class Barracas(Estructura):

    def __init__(self, *args):
        super().__init__(*args)
        self.hp = HP_BARRACAS

    def asignar_atributos_segun_edad(self):
        if self.edad == "Media":
            self.unidades = ["Guerrero", "Mago"]
        else:
            self.unidades = ["Guerrero", "Mago", "MagoGuerrero"]
        super().asignar_atributos_segun_edad()

    def avanzar_edad(self):
        if self.edad == "Media":
            self.edad = "Moderna"
            self.unidades.append("MagoGuerrero")

    def accion(self):
        # No modificar
        elegido = choice(self.unidades)
        suerte = choice((True, False))
        experiencia = choice([1, 2, 3, 4, 5, 6])
        energia = choice([1, 2, 3, 4, 5, 6])
        if elegido == "Guerrero":
            return elegido, Guerrero(suerte, xp=experiencia, stamina=energia)
        elif elegido == "Mago":
            return elegido, Mago(suerte, xp=experiencia, stamina=energia)
        elif elegido == "MagoGuerrero":
            atributos = {"bendito": suerte, "armado": suerte, "xp": experiencia,
                         "stamina": energia}
            return elegido, MagoGuerrero(**atributos)

class Muro(Estructura):

    def __init__(self, *args):
        super().__init__(*args)
        self.hp = HP_MURO

    def asignar_atributos_segun_edad(self):
        if self.edad=="Media":
            self.reparacion = [20, 80]
        else:
            self.reparacion = [40, 100]
        super().asignar_atributos_segun_edad()

    def accion(self):
        reparar = randint(*self.reparacion)
        if random() < PROB_CRITICO_MURO:
            return 2* reparar
        return reparar
  
    def avanzar_edad(self):
        if self.edad == "Media":
            self.edad = "Moderna"
            return self.asignar_atributos_segun_edad()

# Recuerda completar la herencia
class Catapulta(Estructura):

    def __init__(self, *args):
        super().__init__(*args)
        self.hp = HP_CATAPULTA

    def asignar_atributos_segun_edad(self):
        if self.edad == "Media":
            self.ataque = [40, 100]
        else:
            self.ataque = [80, 140]
        super().asignar_atributos_segun_edad()

    def accion(self):
        daño=randint(*self.ataque)
        if random() < PROB_CRITICO_CATAPULTA:
            return 2* daño
        return daño
  
    def avanzar_edad(self):
        if self.edad == "Media":
            self.edad = "Moderna"
            return self.asignar_atributos_segun_edad()


# Recuerda completar la herencia
class MuroCatapulta(Muro, Catapulta):

    def __init__(self, *args):
        super().__init__(*args)
        self.hp = HP_MUROCATAPULTA

    def asignar_atributos_segun_edad(self):
        super().asignar_atributos_segun_edad()
        
    def accion(self):
        reparar = randint(*self.reparacion)
        daño=randint(*self.ataque)
        if random() < PROB_CRITICO_MURO_CATAPULTA:
            daño *= 2.5
            reparar *= 2.5
        return daño,reparar
  
    def avanzar_edad(self):
        if self.edad=="Media":
            self.edad="Moderna"
            return self.asignar_atributos_segun_edad()


if __name__ == "__main__":
    # ---------------
    # En esta sección puedes probar tu codigo
    # ---------------
    pass
