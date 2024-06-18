import pygame
pygame.init()
FPS = 60

ANCHO = 800
ALTO = 600

BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0)
ROJO = (255, 0, 0)
VERDE = (0, 255, 0)
AZUL = (0, 0, 255)
MARRON = (153, 76, 0)
ventana = pygame.display.set_mode((ANCHO, ALTO))

fuente = pygame.font.SysFont("Arial", 30)