from random import uniform
import os

TIEMPO_TERMINATOR_DOG = 3000  # ms
VELOCIDAD_ALIEN = (3, 3)  # px/ms
DURACION_NIVEL_INICIAL = 60 # s
PONDERADOR_TUTORIAL = uniform(0.9, 1)
PONDERADOR_ENTRENAMIENTO = uniform(0.8, 0.9)
PONDERADOR_INVASION = uniform(0.7, 0.8)
TASA_ACTUALIZACION = 10  # ms

TASA_EVENTO = 1000  # ms
MAX_X_VENTANA = 1500 # px
MAX_Y_VENTANA = 1000 # px
ALTO_MENU = 200 # px

# TECLAS
TECLA_ARRIBA = "w"
TECLA_IZQUIERDA = "a"
TECLA_ABAJO = "s"
TECLA_DERECHA = "d"
TECLA_PAUSA = "p"
TECLA_DISPARO = " "
CHEAT = ["ovni", "cia"]

# DIMENSIONES SPRITES
ALTO_MIRA = 200 # px
ANCHO_MIRA = 300 # px
RAPIDEZ_MIRA = 10 # px/ms


ANCHO_ALIENV = 92 # px
ALTO_ALIENV = 100 # px
ANCHO_ALIENR = 90 # px 
ALTO_ALIENR = 100 # px 
ANCHO_ALIENA = 166 # px 
ALTO_ALIENA = 100 #px

# RUTAS DE ARCHIVOS
RUTA_UI_VENTANA_PRINCIPAL = os.path.join('Sprites', 'Ventana_Principal.ui')
RUTA_LOGO = os.path.join('Sprites', 'Logo', 'logo.png')
RUTA_PUNTAJES = os.path.join('puntajes.txt')

RUTA_LUNA = os.path.join('Sprites', 'Fondos', 'Luna.png')
RUTA_JUPITER = os.path.join('Sprites', 'Fondos', 'Jupiter.png')
RUTA_INVASION = os.path.join('Sprites', 'Fondos', 'Galaxia.png')

RUTA_ALIENV = os.path.join('Sprites', 'Aliens', 'Alien1.png')
RUTA_ALIENR = os.path.join('Sprites', 'Aliens', 'Alien2.png')
RUTA_ALIENA = os.path.join('Sprites', 'Aliens', 'Alien3.png')
RUTA_ALIENV_MUERTO = os.path.join('Sprites', 'Aliens', 'Alien1_dead.png')
RUTA_ALIENR_MUERTO = os.path.join('Sprites', 'Aliens', 'Alien2_dead.png')
RUTA_ALIENA_MUERTO = os.path.join('Sprites', 'Aliens', 'Alien3_dead.png')

RUTA_PERRO_RIENDO = os.path.join('Sprites', 'Terminator-Dog', 'Dog1.png')
RUTA_TERMINATOR_DOG_ALIENV = os.path.join('Sprites', 'Terminator-Dog', 'Perro_y_alien1.png')
RUTA_TERMINATOR_DOG_ALIENR = os.path.join('Sprites', 'Terminator-Dog', 'Perro_y_alien2.png')
RUTA_TERMINATOR_DOG_ALIENA = os.path.join('Sprites', 'Terminator-Dog', 'Perro_y_alien3.png')
RUTA_RISA = os.path.join("Sonidos", "risa_robotica.wav")

RUTA_EXPLOSION_1 = os.path.join('Sprites', 'Elementos juego', 'Disparo_f1.png')
RUTA_EXPLOSION_2 = os.path.join('Sprites', 'Elementos juego', 'Disparo_f2.png')
RUTA_EXPLOSION_3 = os.path.join('Sprites', 'Elementos juego', 'Disparo_f3.png')
RUTA_MIRA = os.path.join('Sprites', 'Elementos juego', 'Disparador_negro.png')
RUTA_MIRA_DISPARO = os.path.join('Sprites', 'Elementos juego', 'Disparador_rojo.png')
RUTA_DISPARO = os.path.join("Sonidos", "disparo.wav")
RUTA_BALA = os.path.join('Sprites', 'Elementos juego', 'Bala.png')

# BONUS
TIEMPO_ESTRELLA = 5000  # ms
TIEMPO_PERDIDO = 5  # s
TIEMPO_BOMBA = 5000  # ms
TIEMPO_CONGELAMIENTO = 3000  # ms
TIEMPO_BALA = 5000  # ms
PROBABILIDAD_EVENTO_BONUS = 0.2
EVENTOS = ["estrella", "bomba", "bala"]
RUTA_BALA_EXTRA = os.path.join('Sprites', 'Bonus', 'Bala_extra.png')
RUTA_BOMBA = os.path.join('Sprites', 'Bonus', 'Bomba_hielo.png')
RUTA_ESTRELLA = os.path.join('Sprites', 'Bonus', 'Estrella_muerte.png')
