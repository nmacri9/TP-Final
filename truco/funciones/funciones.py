import random
import pygame
from funciones.constantes import *
from funciones.cartas import cargar_cartas_desde_txt
from funciones.menu import *
from funciones.logica import calcular_puntos_envido, mezclar_cartas, repartir_manos
pygame.init()
import sys
from os import system
system("cls")

class Carta: 
    def __init__(self, valoracion, palo) -> None:
        self.valoracion = valoracion
        self.palo = palo
    def __repr__(self)-> str:
        return f'{self.valoracion} de {self.palo}' # devuelve valor y carta ejemplo ( "1" de "basto")



def cargar_imagenes_cartas(palos:list, valoraciones:list)-> dict:
    imagenes_cartas = {}
    carpeta_imagenes = r"c:\Users\nicom\OneDrive\Desktop\TP Truco\imagenes1"
    """carga las imágenes de las cartas , asociándolas a su valoración y palo
    si alguna imagen no se puede cargar, devuelve un diccionario con las imagenes."""
    for palo in palos:
        for valoracion in valoraciones:
            nombres_imagenes = f'{valoracion} de {palo}.jpg'
            ubicacion_imagen = fr"{carpeta_imagenes}\{nombres_imagenes}"
            imagenes_cartas[f'{valoracion} de {palo}'] = pygame.image.load(ubicacion_imagen)
            
    return imagenes_cartas


class Juego:
    def __init__(self, seleccion_puntos, seleccion_maquina) :
        self.seleccion_puntos = int(seleccion_puntos)
        self.seleccion_maquina = seleccion_maquina
        self.puntos_jugador_1 = 0
        self.puntos_jugador_2 = 0
        self.puntos_ronda_actual_ = 0  # Puntos acumulados en la ronda de 
        self.puntos_ronda_actual_envido = 0  # Puntos acumulados en el Envido
        self.boton_ = pygame.Rect(ANCHO_PANTALLA / 2 - 235, ALTO_PANTALLA / 2 + 270, 150, 70)
        self.boton_envido = pygame.Rect(ANCHO_PANTALLA / 2 - 75, ALTO_PANTALLA / 2 + 270, 150, 70)
        self.boton_mazo = pygame.Rect(ANCHO_PANTALLA / 2 + 85, ALTO_PANTALLA / 2 + 270, 150, 70)
        # Otros botones si es necesario
        self.boton_volver = pygame.Rect(ANCHO_PANTALLA / 2 + 160, ALTO_PANTALLA / 2 + 270, 150, 70)
        # Fuentes y colores
        self.texto_truco = pygame.font.Font(None, 40).render("Truco", True, (255, 255, 255))
        self.texto_envido = pygame.font.Font(None, 40).render("Envido", True, (255, 255, 255))
        self.texto_mazo = pygame.font.Font(None, 40).render("Mazo", True, (255, 255, 255))

        # Variables del juegos
        self.jugadores = ['jugador 1', 'jugador 2']
        #cargar cartas y repartir
        mazo_cartas = cargar_cartas_desde_txt()
        mazo_cartas = mezclar_cartas(mazo_cartas)  
        manos, mazo_restante = repartir_manos(mazo_cartas, jugadores=2)
        self.cartas = manos  # Ahora esto es un diccionario con las manos
        self.mazo_restante = mazo_restante  # Guarda las cartas restantes del mazoS
        # carga imagenes de las cartas
        self.imagenes = cargar_imagenes_cartas(PALOS, VALORACIONES)  # Cargar imágenes de las cartas
        #posiciones de las cartas
        self.cartas_posiciones = []  # Inicializar una vez
        self.cartas_maquina_posiciones = []
        #asignar cartas a jugador y maquina
        self.cartas_maquina = self.cartas['jugador 2']  # Acceso correcto al diccionario
        self.cartas_jugador = self.cartas ['jugador 1']
        if self.seleccion_maquina == '1':
            self.maquina = JugadorAleatorio()  # Máquina 1 con estrategia aleatoria
        elif self.seleccion_maquina == '2':
            self.maquina = JugadorEstrategia() 
        self.contador_maquina = 0
        # Posiciones iniciales de las cartas del jugador 1
        jugador_cartas = self.cartas['jugador 1']
        for j, carta in enumerate(jugador_cartas):
            x = 325 + j * 110
            y = 450
            carta_rect = pygame.Rect(x, y, ANCHO_CARTA, ALTO_CARTA)
            self.cartas_posiciones.append((carta_rect, carta, False, (x, y)))

    def mostrar_cartas_por_pantalla(self, pantalla) -> None:
        """ muestra cartas por pantalla"""
        for carta_rect, carta, movida, base_pos in self.cartas_posiciones:
            carta_str = f'{carta.valoracion} de {carta.palo}'
            if carta_str in self.imagenes:
                imagen = self.imagenes[carta_str]
                imagen_dimensionada = pygame.transform.scale(imagen, (ANCHO_CARTA, ALTO_CARTA))
                pantalla.blit(imagen_dimensionada, carta_rect.topleft)  


    def jugar_maquina(self):
        """Logica de la maquina para jugar una carta aleatoria"""
        if self.cartas_maquina and self.contador_maquina < 3:
            carta = random.choice(self.cartas_maquina) #elije carta aleatoria
            self.cartas_maquina.remove(carta) #elimina la carta recien utilizada
            
            destino_x = 230 + self.contador_maquina * 250
            destino_y = 120
            carta_rect = pygame.Rect(destino_x, destino_y, ANCHO_CARTA, ALTO_CARTA)
            self.cartas_maquina_posiciones.append((carta_rect, carta, True))
            self.contador_maquina += 1

    def mostrar_cartas_maquina(self, pantalla):
        """Muestra las cartas jugadas por la máquina."""
        for carta_rect, carta, movida in self.cartas_maquina_posiciones: #recorre cartas
            carta_str = f'{carta.valoracion} de {carta.palo}'
            if carta_str in self.imagenes: #verifica que la carta este para que no de error en caso de no estar
                imagen = self.imagenes[carta_str]
                imagen_dimensionada = pygame.transform.scale(imagen, (ANCHO_CARTA, ALTO_CARTA))
                pantalla.blit(imagen_dimensionada, carta_rect.topleft)
    
    
    def dibujar__envido_mazo(self, pantalla, botones:list, textos:list)-> None:
        for i, boton in enumerate(botones):
            # Dibuja el rectángulo del botón
            pygame.draw.rect(pantalla, (0, 153, 76), boton)
            
            
            texto = textos[i]
            
            # Centra el texto 
            texto_rect = texto.get_rect(center=boton.center)
            
            # escribe el texto
            pantalla.blit(texto, texto_rect)


    def obtener_puntos(self)-> tuple[int,int]:
        """Devuelve los puntos de ambos jugadores."""
        return self.puntos_jugador_1, self.puntos_jugador_2
    
    def ganador_ronda(self, cartas_jugador_1:list, cartas_jugador_2:list)->str:
        """Determina el ganador de la ronda basándose en las cartas jugadas."""
        if not cartas_jugador_1 or not cartas_jugador_2:
            raise ValueError("No se puede determinar el ganador: una de las listas de cartas está vacía.")

        valor_jugador_1 = max([carta.obtener_valor_() for carta in cartas_jugador_1])
        valor_jugador_2 = max([carta.obtener_valor_() for carta in cartas_jugador_2])

        if valor_jugador_1 > valor_jugador_2:
            return 'jugador 1'
        elif valor_jugador_2 > valor_jugador_1:
            return 'jugador 2'
        else:
            return 'empate'

    
    

class JugadorAleatorio:
    def __init__(self):
        pass

    def elegir_carta_aleatoria(self, cartas:list):
        """Elige una carta aleatoria de la mano."""
        return random.choice(cartas)

    def cantar_envido(self, cartas:list)-> bool:
        """El jugador aleatorio no canta envido, solo acepta si el jugador 1 lo canta."""
        return False  # El jugador aleatorio no canta envido

    def aceptar_envido(self, puntos:int, envido_cantado:bool)->bool:
        """Acepta el envido solo si el jugador 1 cantó el envido y tiene más de 27 puntos."""
        if envido_cantado:
            if puntos > 27:
                print(f"Jugador Aleatorio acepta el Envido con {puntos} puntos.")
                return True  # Acepta el envido
            else:
                print("Jugador Aleatorio no acepta el Envido, no tiene suficientes puntos.")
                return False  # No acepta el envido
        return False  # Si no se cantó envido, no acepta nada

    def cantar_falta_envido(self, puntos:int)->bool:
        """Canta Falta Envido si tiene más de 30 puntos."""
        if puntos > 30:
            print(f"Jugador Aleatorio canta Falta Envido con {puntos} puntos.")
            return True
        return False

    def manejar_truco(self, jugador_1_canto_truco:bool, puntos:int)->bool:
        """Si el jugador 1 canta truco, el jugador aleatorio decide si lo acepta."""
        if jugador_1_canto_truco:
            if puntos > 30:  # Si tiene más de 30 puntos, canta Falta Envido
                print("Jugador Aleatorio acepta el Truco con Falta Envido.")
                return True
            else:
                print("Jugador Aleatorio no acepta el Truco.")
                return False
        return False  # Si no se canta truco, no hace nada

class JugadorEstrategia:
    def __init__(self):
        pass

    def realizar_accion_estrategica(self, juego)->None:
        """La máquina de estrategia decide cantar Truco o Envido basado en condiciones."""
        if juego.puntos_jugador_2 > 27 and random.choice([True, False]):  # Solo canta si tiene más de 27 puntos
            print("La máquina canta Envido")
            juego.cantar_envido("jugador 2")
        elif random.choice([True, False]):  # También puede cantar Truco, pero de manera estratégica
            print("La máquina canta Truco")
            juego.cantar_truco("jugador 2")
        else:
            print("La máquina no hace nada en este turno")















    