
ALTO_CARTA = 125
ANCHO_CARTA = 100
ANCHO_PANTALLA = 1000
ALTO_PANTALLA = 722
ALTO_BOTONES = 50      # Altura de los botones
Y_BOTONES = 660
# Colores para los botones y textos
NEGRO = (0, 0, 0)
VERDE = (34, 139, 34)
MARRON_CLARO = (205, 133, 63)
BLANCO = (255, 255, 255)

VALORACIONES = (1, 2, 3, 4, 5, 6, 7, 10, 11, 12)
#Al tener parentesis () es una tupla inmutable
PALOS = ('Basto', 'Copa', 'Oro', 'Espada')

contador_posiciones = 0
ancho_botones = ANCHO_PANTALLA // 3
# Contadores de puntos y jugadas
puntos_jugador_1 = 0
puntos_jugador_2 = 0
puntos_maquina = 0
puntos_en_juego = 0
jugadas_realizadas = 0  # Contador de cartas jugadas


botones_principal = [
    {"texto": "Truco", "x": 0, "y": Y_BOTONES, "ancho": ancho_botones, "alto": ALTO_BOTONES},
    {"texto": "Envido", "x": ancho_botones, "y": Y_BOTONES, "ancho": ancho_botones, "alto": ALTO_BOTONES},
    {"texto": "Me voy al mazo", "x": ancho_botones * 2, "y": Y_BOTONES, "ancho": ancho_botones, "alto": ALTO_BOTONES},
]

botones_truco = [
    {"texto": "Truco", "x": 100, "y": 620, "ancho": 115, "alto": 50},
    {"texto": "Retruco", "x": 300, "y": 620, "ancho": 130, "alto": 50},
    {"texto": "Vale Cuatro", "x": 500, "y": 620, "ancho": 180, "alto": 50},
    {"texto": "Volver", "x": 700, "y": 620, "ancho": 115, "alto": 50},
]

botones_envido = [
    {"texto": "Envido", "x": 100, "y": 620, "ancho": 115, "alto": 50},
    {"texto": "Real Envido", "x": 300, "y": 620, "ancho": 185, "alto": 50},
    {"texto": "Falta Envido", "x": 500, "y": 620, "ancho": 185, "alto": 50},
    {"texto": "Volver", "x": 700, "y": 620, "ancho": 115, "alto": 50},
]

movida = False
truco_visible = False  # Controlar si los botones Truco están visibles
envido_visible = False  # Controlar si los botones Envido están visibles

# Variables de control de cartas jugadas y Envido cantado
jugador_1_primera_carta = False
jugador_2_primera_carta = False
envido_cantado = False
jugador_se_fue_al_mazo = True

AUDIOS = {
    "truco": r"c:\Users\nicom\OneDrive\Desktop\TP Truco\audios tp\audio truco.mp3",
    "retruco": r"c:\Users\nicom\OneDrive\Desktop\TP Truco\audios tp\quiero retruco.mp3",
    "vale_cuatro": r"c:\Users\nicom\OneDrive\Desktop\TP Truco\audios tp\quiero vale cuatro.mp3",
    "envido": r"c:\Users\nicom\OneDrive\Desktop\TP Truco\audios tp\audio envido.mp3",
    "real_envido": r"c:\Users\nicom\OneDrive\Desktop\TP Truco\audios tp\real envido.mp3",
    "falta_envido": r"c:\Users\nicom\OneDrive\Desktop\TP Truco\audios tp\Falta envido.mp3",
    "mazo": r"c:\Users\nicom\OneDrive\Desktop\TP Truco\audios tp\me voy al mazo.mp3",
}

#puntos
estado_truco = "sin truco"