import pygame
import sys
from funciones.constantes import *
from funciones.menu import menu_principal,seleccionar_maquina
from funciones.funciones import Juego, JugadorAleatorio, JugadorEstrategia
from funciones.grafica import *
from os import system
from funciones.logica import anotador_puntos,actualizar_puntaje_envido,actualizar_puntaje_truco

system("cls")
pygame.init()
pygame.mixer.init()

# Configuración de pantalla
espacio_pantalla = pygame.display.set_mode((ANCHO_PANTALLA, ALTO_PANTALLA))
pygame.display.set_caption('El Truco')
icono = pygame.image.load(r"c:\Users\nicom\OneDrive\Desktop\TP Truco\imagenes1\icono truco.jpg")
icono_escalado = pygame.transform.scale(icono, (32, 32))
pygame.display.set_icon(icono_escalado)

# Cargar la imagen de fondo
fondo_pantalla = pygame.image.load(r"c:\Users\nicom\OneDrive\Desktop\TP Truco\imagenes1\imagenes\Truco fondo.PNG")
fondo = pygame.transform.scale(fondo_pantalla, (ANCHO_PANTALLA, 722))

# Fuentes
pygame.font.init()
fuente_botones = pygame.font.Font(None, 40)

# Inicializar el juego con los valores seleccionados desde el menú
seleccion_puntos, seleccion_maquina = menu_principal(espacio_pantalla)
juego = Juego(seleccion_puntos, seleccion_maquina)

# Variables de control
game = True


while game:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            game = False

        elif evento.type == pygame.MOUSEMOTION:
            manejar_movimiento_mouse(evento, juego)

        elif evento.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()

            # Manejo de botones principales
            if not truco_visible and not envido_visible:
                for boton in botones_principal:
                    rect = pygame.Rect(boton["x"], boton["y"], boton["ancho"], boton["alto"])
                    if rect.collidepoint(mouse_pos):
                        if boton["texto"] == "Truco":
                            truco_visible = True  # Muestra los botones de Truco
                        elif boton["texto"] == "Envido" and not envido_cantado and not jugador_1_primera_carta and not jugador_2_primera_carta:
                            envido_visible = True  # Muestra los botones de Envido
                        elif boton["texto"] == "Me voy al mazo"and not jugador_se_fue_al_mazo:
                            print("Me voy al mazo")
                            sonido = pygame.mixer.Sound(AUDIOS["mazo"]).play()
                            jugador_se_fue_al_mazo = True

            # Manejo de botones de Truco
            elif truco_visible:
                for boton in botones_truco:
                    rect = pygame.Rect(boton["x"], boton["y"], boton["ancho"], boton["alto"])
                    if rect.collidepoint(mouse_pos):
                        if boton["texto"] == "Truco" and estado_truco == "sin truco":
                            estado_truco = "truco_cantado"
                            puntos_truco = 2  # Valor del Truco
                            print("Jugador 1 cantó Truco")
                            pygame.mixer.Sound(AUDIOS["truco"]).play()
                            # Actualiza el puntaje aquí con la función que implementaste
                            actualizar_puntaje_truco(juego, "jugador 1", puntos_truco)

                        elif boton["texto"] == "Retruco" and estado_truco == "truco_cantado":
                            estado_truco = "retruco_habilitado"
                            puntos_truco = 3  # Valor del Retruco
                            print("Jugador 1 cantó Retruco")
                            pygame.mixer.Sound(AUDIOS["retruco"]).play()
                            # Actualiza el puntaje aquí con la función que implementaste
                            actualizar_puntaje_truco(juego, "jugador 1", puntos_truco)

                        elif boton["texto"] == "Vale Cuatro" and estado_truco == "retruco_habilitado":
                            estado_truco = "vale_cuatro_habilitado"
                            puntos_truco = 4  # Valor del Vale Cuatro
                            print("Jugador 1 cantó Vale Cuatro")
                            pygame.mixer.Sound(AUDIOS["vale_cuatro"]).play()
                            # Actualiza el puntaje aquí con la función que implementaste
                            actualizar_puntaje_truco(juego, "jugador 1", puntos_truco)

                        elif boton["texto"] == "Volver":
                                    truco_visible = False  # Oculta los botones de Truco

            # Manejo de botones de Envido
            elif envido_visible:
                for boton in botones_envido:
                    rect = pygame.Rect(boton["x"], boton["y"], boton["ancho"], boton["alto"])
                    if rect.collidepoint(mouse_pos):
                        if boton["texto"] == "Envido" and not envido_cantado:
                            print("Jugador 1 canta Envido")
                            pygame.mixer.Sound(AUDIOS["envido"]).play()
                            puntos_envido = 2
                            envido_cantado = True
                            actualizar_puntaje_envido(juego, "Envido", "jugador 1")

                        elif boton["texto"] == "Real Envido" and not envido_cantado:
                            print("Jugador 1 canta Real Envido")
                            pygame.mixer.Sound(AUDIOS["real_envido"]).play()
                            puntos_envido = 3
                            envido_cantado = True
                            actualizar_puntaje_envido(juego, "Real Envido", "jugador 1")

                        elif boton["texto"] == "Falta Envido" and not envido_cantado:
                            print("Jugador 1 canta Falta Envido")
                            pygame.mixer.Sound(AUDIOS["falta_envido"]).play()
                            puntos_envido = juego.seleccion_puntos - max(juego.puntos_jugador_1, juego.puntos_jugador_2)
                            envido_cantado = True
                            actualizar_puntaje_envido(juego, "Falta Envido", "jugador 1")
                        elif boton["texto"] == "Volver":
                            envido_visible = False  # Oculta los botones de Envido

            # Manejo del clic en las cartas
            contador_posiciones = manejar_click(evento, juego, contador_posiciones)
            if jugador_se_fue_al_mazo:
                puntos_maquina += puntos_en_juego  # Ajustar puntuación
                turno_actual = "maquina"  # Cambiar de turno
                jugador_se_fue_al_mazo = False  # Resetea el estado


             # Jugada del jugador 1
            if turno_actual == "jugador 1":
                turno_actual = "maquina"
                
                # La máquina hace su jugada, dependiendo de su tipo
                if isinstance(jugador_2, JugadorAleatorio):
                    jugador_2.realizar_accion_aleatoria(juego)  # La máquina aleatoria canta o acepta
                elif isinstance(jugador_2, JugadorEstrategia):
                    jugador_2.realizar_accion_estrategica(juego)  # La máquina de estrategia toma su decisión

                    turno_actual = "jugador 1"  # Cambiar el turno de vuelta al jugador
         # Actualizar estado de las cartas jugadas
            if not jugador_1_primera_carta:
                jugador_1_primera_carta = True
            elif not jugador_2_primera_carta:
                jugador_2_primera_carta = True
                
        # Asignar el tipo de jugador según la selección
        seleccion_maquina = seleccionar_maquina(espacio_pantalla)
        if seleccion_maquina == "1":
            jugador_2 = JugadorAleatorio()  # Máquina 1 es aleatoria
        elif seleccion_maquina == "2":
            jugador_2 = JugadorEstrategia()  # Máquina 2 es de estrategia
        # Comprobar si alguien alcanzó el puntaje máximo (15-30)
        if juego.puntos_jugador_1 >= juego.seleccion_puntos:
            print("¡Jugador 1 ha ganado!")
            game = False  
        elif juego.puntos_jugador_2 >= juego.seleccion_puntos:
            print("¡Jugador 2 ha ganado!")
            game = False  # Termina el juego

    # Dibujar fondo, puntajes, y demás elementos gráficos
    espacio_pantalla.blit(fondo, (0, 0))
    anotador_puntos(espacio_pantalla, puntos_jugador_1, puntos_jugador_2)
    juego.mostrar_cartas_por_pantalla(espacio_pantalla)
    juego.mostrar_cartas_maquina(espacio_pantalla)
    dibujar_botones(espacio_pantalla, truco_visible, envido_visible, botones_truco, botones_envido, botones_principal, fuente_botones, MARRON_CLARO, BLANCO)
    dibujar_marcador(espacio_pantalla, truco_visible, envido_visible)

    pygame.display.flip()

pygame.quit()
