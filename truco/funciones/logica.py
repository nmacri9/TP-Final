import random
from funciones.cartas import Carta, cargar_cartas_desde_txt
import pygame
from funciones.constantes import *

pygame.init()
espacio_pantalla = pygame.display.set_mode((ANCHO_PANTALLA, ALTO_PANTALLA))

def mezclar_cartas(cartas:list)-> list: 
    """Se mezclan las cartas en esta funcion"""
    random.shuffle(cartas) 
    return cartas

def repartir_manos(cartas: list, jugadores=2):
    """Se crean 'sublistas o diccionarios para repartir' y no modifica el mazo original."""
    manos = {f'jugador {i + 1}': [] for i in range(jugadores)}  # Crear un diccionario vacío para cada jugador
    for i in range(3):  # Repartir 3 cartas a cada jugador
        for j in range(jugadores):
            manos[f'jugador {j + 1}'].append(cartas.pop(0))  # Saca la carta del mazo y asigna al jugador
    mazo_restante = cartas  # Lo que queda es el mazo restante
    print(manos)  
    return manos, mazo_restante
def obtener_combinaciones_envido(self)-> list:
        """Busca todas las combinaciones de 2 cartas del mismo palo y devuelve sus puntos de envido."""
        combinaciones = []
        # Agrupamos las cartas por palo
        cartas_por_palo = {}
        for carta in self.cartas:
            if carta.palo not in cartas_por_palo:
                cartas_por_palo[carta.palo] = []
            cartas_por_palo[carta.palo].append(carta)

        # Calculamos el puntaje para cada par de cartas del mismo palo
        for palo, cartas in cartas_por_palo.items():
            if len(cartas) >= 2:  # Solo si hay al menos dos cartas del mismo palo
                for i in range(len(cartas)):
                    for j in range(i+1, len(cartas)):
                        carta1, carta2 = cartas[i], cartas[j]
                        puntos = self.calcular_puntos_envido(carta1, carta2)
                        combinaciones.append(puntos)
        
        return combinaciones

def calcular_puntos_envido(self, carta1, carta2)-> int:
        """Calcula los puntos del envido para un par de cartas."""
        valor1 = self.valor_envido(carta1)
        valor2 = self.valor_envido(carta2)
        
        # Si ambas cartas son del 10, 11 o 12, suman 20 puntos
        if valor1 == 0 and valor2 == 0:
            return 20
        
        # Si no son cartas 10, 11, 12, sumamos el valor de las cartas
        return 20 + valor1 + valor2

def valor_envido(self, carta)-> int:
        """Devuelve el valor de envido de una carta. Las cartas 10, 11, 12 valen 0."""
        if carta.valoracion in ['10', '11', '12']:
            return 0
        return int(carta.valoracion)

def cantar_envido(self)-> tuple[str, int]:
    combinaciones = self.obtener_combinaciones_envido()
    max_puntos = max(combinaciones) if combinaciones else 0
    resultado = "No canta Envido"
    
    if max_puntos > 27:
        resultado = "Canta Envido"
        agregar_puntos(1, max_puntos)  # Si el jugador 1 canta Envido y gana
    elif sum([min(int(carta.valoracion), 10) for carta in self.cartas]) > 30:
        resultado = "Canta Falta Envido"
        agregar_puntos(1, max_puntos)  # Si el jugador 1 canta Falta Envido y gana
    
    return resultado, max_puntos


def cantar_envido_aleatorio(cartas) -> tuple[str,int]:
    """Canta Envido si tiene dos cartas del mismo palo y si es posible."""
    combinaciones = obtener_combinaciones_envido(cartas)
    max_puntos = max(combinaciones) if combinaciones else 0
    if max_puntos > 27:
        return "Canta Envido", max_puntos
    elif sum([min(int(carta.valoracion), 10) for carta in cartas]) > 30:
        return "Canta Falta Envido", max_puntos
    return "No canta Envido", max_puntos

def obtener_combinaciones_envido(cartas: list) -> list:
    """Busca todas las combinaciones de 2 cartas del mismo palo y devuelve sus puntos de envido."""
    combinaciones = []
    cartas_por_palo = {}

    # Agrupamos las cartas por palo
    for carta in cartas:
        if carta.palo not in cartas_por_palo:
            cartas_por_palo[carta.palo] = []
        cartas_por_palo[carta.palo].append(carta)

    # Calculamos el puntaje para cada par de cartas del mismo palo
    for palo, cartas_palo in cartas_por_palo.items():
        if len(cartas_palo) >= 2:  # Solo si hay al menos dos cartas del mismo palo
            for i in range(len(cartas_palo)):
                for j in range(i + 1, len(cartas_palo)):
                    carta1, carta2 = cartas_palo[i], cartas_palo[j]
                    puntos = calcular_puntos_envido(carta1, carta2)
                    combinaciones.append(puntos)

    return combinaciones


def cantar_envido_estrategia(cartas: list ) -> tuple:
    """Canta Envido si tiene más de 27 puntos."""
    combinaciones = obtener_combinaciones_envido(cartas)
    max_puntos = max(combinaciones) if combinaciones else 0
    if max_puntos > 27:
        return "Canta Envido", max_puntos
    return "No canta Envido", max_puntos

def agregar_puntos(jugador: int, puntos: int):
    """Agrega puntos al jugador correspondiente."""
    global puntos_jugador_1, puntos_jugador_2
    if jugador == 1:
        puntos_jugador_1 += puntos
    elif jugador == 2:
        puntos_jugador_2 += puntos


def resetear_puntos()-> None:
    """Resetea los puntos de ambos jugadores al comenzar una nueva ronda."""
    global puntos_jugador_1, puntos_jugador_2
    puntos_jugador_1 = 0
    puntos_jugador_2 = 0

def anotador_puntos(espacio_pantalla, puntos_jugador_1:int, puntos_jugador_2: int) -> None:
    """ Dibuja los puntos de los jugadores en la pantalla."""

    texto_j1 = f"Jugador 1: {puntos_jugador_1}"
    texto_j2 = f"Jugador 2: {puntos_jugador_2}"

    font = pygame.font.Font(None, 28)
    texto_j1_renderizado = font.render(texto_j1, True, (BLANCO))
    texto_j2_renderizado = font.render(texto_j2, True, (BLANCO))  

    espacio_pantalla.blit(texto_j1_renderizado, (20, 20))  # Jugador 1 en la parte superior
    espacio_pantalla.blit(texto_j2_renderizado, (20, 60))  # Jugador 2 debajo del Jugador 1


### PUNTAJES Y TANTOS

def sumar_puntos_envido(self, tipo_envido:str, ganador:str)-> None:
        """Suma los puntos del envido basado en el tipo cantado."""
        if tipo_envido == "Envido":
            puntos = 2
        elif tipo_envido == "Real Envido":
            puntos = 3
        elif tipo_envido == "Falta Envido":
            puntos = self.max_puntos - max(self.puntos_jugador_1, self.puntos_jugador_2)
        else:
            puntos = 0

        # Asigna los puntos al ganador del envido
        if ganador == "jugador 1":
            self.puntos_jugador_1 += puntos
        elif ganador == "jugador 2":
            self.puntos_jugador_2 += puntos
def actualizar_puntaje_envido(juego: object, tipo_envido:str, ganador: str)->bool:
    """
    Actualiza los puntos del envido según el tipo cantado y el ganador.
    """
    if tipo_envido == "Envido":
        puntos_envido = 2
    elif tipo_envido == "Real Envido":
        puntos_envido = 3
    elif tipo_envido == "Falta Envido":
        puntos_envido = juego.seleccion_puntos - max(juego.puntos_jugador_1, juego.puntos_jugador_2)
    else:
        puntos_envido = 0  # Por seguridad, si no se reconoce el tipo

    # Actualiza el puntaje del ganador
    if ganador == 'jugador 1':
        juego.puntos_jugador_1 += puntos_envido
    elif ganador == 'jugador 2':
        juego.puntos_jugador_2 += puntos_envido

    # Verifica si alguien ganó el juego
    if juego.puntos_jugador_1 >= juego.seleccion_puntos:
        print("Jugador 1 ha ganado el juego.")
        return True  # Juego terminado
    elif juego.puntos_jugador_2 >= juego.seleccion_puntos:
        print("Jugador 2 ha ganado el juego.")
        return True  # Juego terminado

    return False  # El juego continúa



def sumar_puntos_truco(self, tipo_:str, ganador:str)-> None:
        """Suma los puntos del  basado en el tipo cantado."""
        if tipo_ == "Truco":
            puntos = 2
        elif tipo_ == "Retruco":
            puntos = 3
        elif tipo_ == "Vale Cuatro":
            puntos = 4
        else:
            puntos = 0  

        
        if ganador == 'jugador 1':
            self.puntos_jugador_1 += puntos
        elif ganador == 'jugador 2':
            self.puntos_jugador_2 += puntos
        self.puntos_ronda_actual_ = 0  

def actualizar_puntaje(jugador_ganador:int, puntos_ronda:int, juego:object)->None:
    """Actualiza los puntos del jugador ganador después de cada ronda."""
    if jugador_ganador == 1:
        juego.puntos_jugador_1 += puntos_ronda
    elif jugador_ganador == 2:
        juego.puntos_jugador_2 += puntos_ronda


def determinar_ganador(cartas_jugador_1:list, cartas_jugador_2:list)-> str:
    """Determina el ganador de la ronda basándose en las cartas jugadas."""
    if not cartas_jugador_1 or not cartas_jugador_2:
        raise ValueError("No se puede determinar el ganador: una de las listas de cartas está vacía.")

    valor_jugador_1 = max([carta.obtener_valor_() for carta in cartas_jugador_1])
    valor_jugador_2 = max([carta.obtener_valor_() for carta in cartas_jugador_2])

    if valor_jugador_1 > valor_jugador_2:
        return 'jugador 1'
    elif valor_jugador_2 > valor_jugador_1:
        return 'jugador 2'

def actualizar_puntaje_truco(juego, ganador:str, puntos_truco:int)-> bool:
    """ Actualiza los puntos del jugador ganador y verifica si alguien ha ganado el juego. """
    if ganador == 'jugador 1':
        juego.puntos_jugador_1 += puntos_truco
    elif ganador == 'jugador 2':
        juego.puntos_jugador_2 += puntos_truco

    if juego.puntos_jugador_1 >= juego.seleccion_puntos:
        print("Jugador 1 ha ganado el juego.")
        return True 
    elif juego.puntos_jugador_2 >= juego.seleccion_puntos:
        print("Jugador 2 ha ganado el juego.")
        return True  

    return False  

def repartir_cartas(juego):
    """ Reparte las cartas al finalizar el turno según el puntaje establecido (15 o 30). """
    if juego.puntos_jugador_1 >= 15 or juego.puntos_jugador_2 >= 15:
        print("Repartiendo cartas nuevamente...")
        mazo_cartas = cargar_cartas_desde_txt()
        mazo_cartas = mezclar_cartas(mazo_cartas)
        manos, mazo_restante = repartir_manos(mazo_cartas, jugadores=2)
        juego.cartas = manos
        juego.mazo_restante = mazo_restante

def ranking_partidas(juego):
    """ Muestra el ranking de las partidas jugadas. """
    if juego.puntos_jugador_1 > juego.puntos_jugador_2:
        print("Jugador 1 ha ganado la partida!")
    elif juego.puntos_jugador_2 > juego.puntos_jugador_1:
        print("Jugador 2 ha ganado la partida!")
    else:
        print("¡Empate!")
    
def determinar_turno(juego):
    """ Determina qué jugador tira primero en cada ronda."""
    if juego.puntos_jugador_1 % 2 == 0:
        print("Es el turno del Jugador 1")
    else:
        print("Es el turno de la Máquina")