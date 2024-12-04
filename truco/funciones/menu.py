import pygame
import sys
from funciones.constantes import *


pygame.font.init()
fuente_titulo = pygame.font.Font(None, 100)
fuente_botones = pygame.font.Font(None, 40)


def dibujar_boton(pantalla, texto, x, y, ancho, alto):
    """Dibuja un botón con texto centrado."""
    rect = pygame.Rect(x, y, ancho, alto)
    pygame.draw.rect(pantalla, MARRON_CLARO, rect, border_radius=10)
    texto_renderizado = fuente_botones.render(texto, True, BLANCO)
    texto_rect = texto_renderizado.get_rect(center=rect.center)
    pantalla.blit(texto_renderizado, texto_rect)
    return rect


def menu_principal(pantalla):
    """Menú principal del juego."""
    seleccion_puntos = None
    seleccion_maquina = None

   
    titulo = fuente_titulo.render("TRUCO", True, MARRON_CLARO)
    pos_titulo = ((pantalla.get_width() - titulo.get_width()) // 2, 50)

    
    botones = [
        {"texto": "15 o 30 Puntos", "x": 400, "y": 250, "ancho": 200, "alto": 60},
        {"texto": "Contra Máquina", "x": 400, "y": 350, "ancho": 200, "alto": 60},
        {"texto": "Jugar", "x": 400, "y": 450, "ancho": 200, "alto": 60},
        {"texto": "Salir", "x": 400, "y": 550, "ancho": 200, "alto": 60},
    ]

    corriendo = True
    while corriendo:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if evento.type == pygame.MOUSEBUTTONDOWN:
                x, y = evento.pos
                for boton in botones:
                    rect = pygame.Rect(boton["x"], boton["y"], boton["ancho"], boton["alto"])
                    if rect.collidepoint(x, y):
                        if boton["texto"] == "15 o 30 Puntos":
                            seleccion_puntos = seleccionar_puntos(pantalla)
                        elif boton["texto"] == "Contra Máquina":
                            seleccion_maquina = seleccionar_maquina(pantalla)
                        elif boton["texto"] == "Jugar":
                            if seleccion_puntos and seleccion_maquina:
                                return seleccion_puntos, seleccion_maquina
                        elif boton["texto"] == "Salir":
                            pygame.quit()
                            sys.exit()

        # Dibujar fondo y elementos
        pantalla.fill(VERDE)
        pantalla.blit(titulo, pos_titulo)
        for boton in botones:
            dibujar_boton(
                pantalla,
                boton["texto"],
                boton["x"],
                boton["y"],
                boton["ancho"],
                boton["alto"],
            )
        pygame.display.flip()
    return seleccion_puntos, seleccion_maquina
# botones de selección de puntos
def seleccionar_puntos(pantalla):
    """Permite seleccionar entre 15 o 30 puntos."""
    opciones = [
        {"texto": "15 Puntos", "x": 400, "y": 250, "ancho": 200, "alto": 60},
        {"texto": "30 Puntos", "x": 400, "y": 350, "ancho": 200, "alto": 60},
    ]
    
    while True:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if evento.type == pygame.MOUSEBUTTONDOWN:
                x, y = evento.pos
                for opcion in opciones:
                    rect = pygame.Rect(opcion["x"], opcion["y"], opcion["ancho"], opcion["alto"])
                    if rect.collidepoint(x, y):
                        puntos = opcion["texto"].split()[0]  # Devuelve "15" o "30"
                        return puntos  # regresa al menu 

        pantalla.fill(VERDE)
        for opcion in opciones:
            dibujar_boton(
                pantalla,
                opcion["texto"],
                opcion["x"],
                opcion["y"],
                opcion["ancho"],
                opcion["alto"],
            )
        pygame.display.flip()

seleccion_maquina = None

def seleccionar_maquina(pantalla):
    """Permite seleccionar entre Máquina 1 o Máquina 2."""
    global seleccion_maquina  # Usar la variable global

    if seleccion_maquina is not None:
        return seleccion_maquina  # Si se seleccionó devuelve la máquina seleccionada

    opciones = [
        {"texto": "Máquina 1", "x": 400, "y": 250, "ancho": 200, "alto": 60},
        {"texto": "Máquina 2", "x": 400, "y": 350, "ancho": 200, "alto": 60},
    ]

    while True:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if evento.type == pygame.MOUSEBUTTONDOWN:
                x, y = evento.pos
                for opcion in opciones:
                    rect = pygame.Rect(opcion["x"], opcion["y"], opcion["ancho"], opcion["alto"])
                    if rect.collidepoint(x, y):
                        seleccion_maquina = opcion["texto"].split()[1]  # Devuelve "1" o "2"
                        return seleccion_maquina  # Regresa la selección

        pantalla.fill(VERDE)
        for opcion in opciones:
            dibujar_boton(
                pantalla,
                opcion["texto"],
                opcion["x"],
                opcion["y"],
                opcion["ancho"],
                opcion["alto"],
            )
        pygame.display.flip()
