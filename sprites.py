from boton import *

class Sprites:
    def __init__(self, image):
        self.sheet = image
    def transformar_imagen(self, frame, width, height, escala, color):
        image = pygame.Surface((width, height)).convert_alpha()
        image.blit(self.sheet, (0, 0), ((frame * width), 0, width, height))
        image = pygame.transform.scale(image, (width * escala, height * escala))
        image.set_colorkey(color)   

        return image

doom_sprite_pensando = Sprites(pygame.image.load("src\Doomguy_fijandose.png"))
doom_sprite_pensando_izquierda = doom_sprite_pensando.transformar_imagen(2, 24, 29, 3, NEGRO)
doom_sprite_pensando_medio = doom_sprite_pensando.transformar_imagen(0, 24, 29, 3, NEGRO)
doom_sprite_pensando_derecha = doom_sprite_pensando.transformar_imagen(1, 24, 29, 3, NEGRO)