from sprites import *
import os
import csv
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
# PROBAR ESTA FUNC
def crear_lista_desde_csv(archivo_csv):
    dicc_imagenes = {}
    rutas = cargar_rutas_desde_csv(archivo_csv)
    for key, archivos in rutas.items():
        imagenes = []
        for ruta_imagen in archivos:
            imagen = pygame.image.load(ruta_imagen)
            imagen = normalizar_imagen(imagen, (200, 200))
            imagenes.append(imagen)
        dicc_imagenes[key] = imagenes
    
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

def crear_matriz_rutas(carpeta):
    matriz_rutas = [[None for _ in range(4)] for _ in range(15)]
    carpetas_logos = []
    for i in os.listdir(carpeta):
        if os.path.isdir(os.path.join(carpeta, i)):
            carpetas_logos.append(i)
    fila = 0
    col = 0
    for i in carpetas_logos:
        ruta = os.path.join(carpeta, i)
        archivos = sorted(os.listdir(ruta))
        for j in archivos:
            ruta_imagen = os.path.join(ruta, j)
            matriz_rutas[fila][col] = ruta_imagen
            col += 1
            if col == 4:
                col = 0
                fila += 1
                if fila == 15:
                    return matriz_rutas
    
    return matriz_rutas

def guardar_matriz_csv(matriz, archivo_csv):
    with open(archivo_csv, mode='w', newline='') as file:
        escribir = csv.writer(file)
        escribir.writerows(matriz)

def cargar_rutas_desde_csv(archivo_csv):
    rutas = {}
    with open(archivo_csv, mode='r') as file:
        lector = csv.reader(file)
        for row in lector:
            if row:
                key = os.path.basename(os.path.dirname(row[0]))
                if key not in rutas:
                    rutas[key] = []
                rutas[key].extend(row)
    return rutas

print(crear_lista("src\Imagenes"))

print(crear_lista_desde_csv("rutas.csv"))