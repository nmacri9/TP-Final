import pygame
from funciones.constantes import *


def manejar_movimiento_mouse(evento, juego)-> None:
    """Maneja el movimiento del mouse sobre las cartas"""
    mouse_pos = evento.pos
    for i, (carta_rect, carta, movida, base_pos) in enumerate(juego.cartas_posiciones):
        if carta_rect.collidepoint(mouse_pos) and not movida:
            # Mover temporalmente hacia arriba
            carta_rect.topleft = (base_pos[0], base_pos[1] - 10)
        else:
            # Restaurar la posición original
            carta_rect.topleft = base_pos

def manejar_click(evento, juego, contador_posiciones)-> int:
    """Maneja los clicks del mouse para mover una carta"""
    mouse_pos = evento.pos
    for i, (carta_rect, carta, movida, base_pos) in enumerate(juego.cartas_posiciones):
        if carta_rect.collidepoint(mouse_pos) and not movida:
            # Determinar la posición de destino con el contador
            if contador_posiciones == 0:
                destino = (200, 190)
                contador_posiciones += 1
            elif contador_posiciones == 1:
                destino = (450, 190)
                contador_posiciones += 1
            elif contador_posiciones == 2:
                destino = (700, 190)
                contador_posiciones += 1

            # Mover la carta a la posición de destino
            carta_rect.topleft = destino
            juego.cartas_posiciones[i] = (carta_rect, carta, True, destino)

            # Acción de la máquina
            juego.jugar_maquina()

            break

    return contador_posiciones


#BOTONES MARCADOR


# Configuración de fuentes y colores
fuente_botones = pygame.font.Font(None, 36)


def dibujar_marcador(pantalla, truco_visible, envido_visible)-> None:
    fuente = pygame.font.Font(None, 40)

    # Dibuja los botones siempre
    texto_truco = fuente.render("Truco", True, BLANCO)
    texto_envido = fuente.render("Envido", True, BLANCO)
    texto_mazo = fuente.render("Mazo", True, BLANCO)

    truco_rect = pygame.Rect(150, 620, 200, 50)
    envido_rect = pygame.Rect(350, 620, 200, 50)
    mazo_rect = pygame.Rect(550, 620, 200, 50)



def manejar_click_truco_envido(evento, truco_visible, envido_visible, juego)-> bool:
    mouse_pos = evento.pos
    
    # Definir las áreas de los botones
    truco_boton = pygame.Rect(150, 620, 200, 50)
    envido_boton = pygame.Rect(350, 620, 200, 50)
    
    # Manejo del botón Truco
    if truco_boton.collidepoint(mouse_pos):
        if not truco_visible:
            truco_visible = True
            envido_visible = False
    
    # Manejo del botón Envido
    elif envido_boton.collidepoint(mouse_pos):
        if not envido_visible:
            envido_visible = True
            truco_visible = False
    
    # Manejo del botón Mazo 
    mazo_boton = pygame.Rect(550, 620, 200, 50)
    if mazo_boton.collidepoint(mouse_pos):
        truco_visible = False
        envido_visible = False

    return truco_visible, envido_visible



def dibujar_botones (espacio_pantalla, truco_visible, envido_visible, botones_truco, botones_envido, botones_principal, fuente_botones, COLOR_BOTON, COLOR_TEXTO)-> None:
    if truco_visible:
        # Solo dibuja los botones de Truco
        for boton in botones_truco:
            pygame.draw.rect(espacio_pantalla, COLOR_BOTON, pygame.Rect(boton["x"], boton["y"], boton["ancho"], boton["alto"]))
            texto = fuente_botones.render(boton["texto"], True, COLOR_TEXTO)
            espacio_pantalla.blit(texto, (boton["x"] + 10, boton["y"] + 10))
    elif envido_visible:
        # Solo dibuja los botones de Envido
        for boton in botones_envido:
            pygame.draw.rect(espacio_pantalla, COLOR_BOTON, pygame.Rect(boton["x"], boton["y"], boton["ancho"], boton["alto"]))
            texto = fuente_botones.render(boton["texto"], True, COLOR_TEXTO)
            espacio_pantalla.blit(texto, (boton["x"] + 10, boton["y"] + 10))
    else:
        # Dibuja solo los botones principales cuando no se ve Truco ni Envido
        for boton in botones_principal:
            pygame.draw.rect(espacio_pantalla, COLOR_BOTON, pygame.Rect(boton["x"], boton["y"], boton["ancho"], boton["alto"]))
            texto = fuente_botones.render(boton["texto"], True, COLOR_TEXTO)
            espacio_pantalla.blit(texto, (boton["x"] + 10, boton["y"] + 10))