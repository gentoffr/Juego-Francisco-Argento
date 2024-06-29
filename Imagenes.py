from sprites import *
import os

def crear_lista(carpeta):
    dicc_imagenes = {}
    carpetas_logos = []
    for i in os.listdir(carpeta):
        if os.path.isdir(os.path.join(carpeta, i)):
            carpetas_logos.append(i)
    
    for i in carpetas_logos:
        ruta = os.path.join(carpeta, i)
        imagenes = []
        archivos = sorted(os.listdir(ruta))
        for j in archivos:
            ruta_imagen = os.path.join(ruta, j)
            imagen = pygame.image.load(ruta_imagen)
            imagen = normalizar_imagen(imagen, (200, 200))
            imagenes.append(imagen)

        dicc_imagenes[i] = imagenes
    return dicc_imagenes

def normalizar_imagen(imagen, tamaño):
    tamaño_con_borde = (tamaño[0] + 2 * 5, tamaño[1] + 2 * 5)
    fondo_con_borde = pygame.Surface(tamaño_con_borde)
    fondo_con_borde.fill(NARANJA)
    fondo = pygame.Surface(tamaño)
    fondo.fill(BLANCO)
    ancho, alto = imagen.get_size()
    if ancho > alto:
        escala = tamaño[0] / float(ancho)
        nuevo_ancho = tamaño[0]
        nuevo_alto = int(alto * escala)
    else:
        escala = tamaño[1] / float(alto)
        nuevo_alto = tamaño[1]
        nuevo_ancho = int(ancho * escala)
    imagen = pygame.transform.scale(imagen, (nuevo_ancho, nuevo_alto))
    posicion_x = (tamaño[0] - nuevo_ancho) // 2
    posicion_y = (tamaño[1] - nuevo_alto) // 2
    fondo.blit(imagen, (posicion_x, posicion_y))
    fondo_con_borde.blit(fondo, (5, 5))
    return fondo_con_borde