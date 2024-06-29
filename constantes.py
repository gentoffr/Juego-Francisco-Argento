import pygame
pygame.init()
FPS = 60

ANCHO = 1024
ALTO = 720

BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0)
ROJO = (255, 0, 0)
VERDE = (0, 255, 0)
AZUL = (0, 0, 255)
MARRON = (153, 76, 0)
COLOR_FONDO = (231, 111, 81)
NARANJA = (244, 162, 97)
AMARILLITO = (233, 196, 106)
VERDE_AQUAMARINA = (54, 186, 152)

ventana = pygame.display.set_mode((ANCHO, ALTO))

fuente = pygame.font.SysFont("Arial", 30)