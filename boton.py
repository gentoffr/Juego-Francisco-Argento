from constantes import *
class Boton:
    def __init__(self, place, size, color_normal, color_activo, mensaje, fuente, color_texto):
        self.rect = pygame.Rect(place, size)
        self.rect.midbottom = place
        self.color_normal = color_normal
        self.color_activo = color_activo
        self.color_actual = color_normal
        self.mensaje = mensaje
        self.fuente = fuente
        self.color_texto = color_texto

    def esta_sobre(self, pos):
        return self.rect.collidepoint(pos)

    def dibujar(self, pantalla, borde=False):
        pygame.draw.rect(pantalla, self.color_actual, self.rect)
        texto = self.fuente.render(self.mensaje, True, self.color_texto)
        texto_rect = texto.get_rect(center=self.rect.center)
        pantalla.blit(texto, texto_rect)
        if self.esta_sobre(pygame.mouse.get_pos()):
            self.color_actual = self.color_activo
        else:
            self.color_actual = self.color_normal
        if borde:
            pygame.draw.rect(pantalla, NEGRO, self.rect, 2)  