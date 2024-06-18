from sprites import *

class Juego:
    def __init__(self):
        self.ventana = ventana
        self.fps = FPS
        self.reloj = pygame.time.Clock()
        self.corriendo = True
        self.titulo = "Juego bien malandro"
        self.flag_menu = True
        self.flag_juego = False

    def gestor_eventos(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.corriendo = False

    def boton_salir(self):
        boton_salir = Boton((ANCHO // 2, 300), (100, 50), BLANCO, ROJO, "SALIR", fuente, NEGRO)
        if boton_salir.esta_sobre(pygame.mouse.get_pos()):
            boton_salir.color_actual = ROJO
            boton_salir.dibujar(self.ventana)
            if pygame.mouse.get_pressed()[0]:
                self.corriendo = False
        boton_salir.dibujar(self.ventana)

    def boton_jugar(self):
        boton_jugar = Boton((ANCHO // 2, 200), (100, 50), BLANCO, VERDE, "JUGAR", fuente, NEGRO)
        if boton_jugar.esta_sobre(pygame.mouse.get_pos()):
            boton_jugar.color_actual = VERDE
            boton_jugar.dibujar(self.ventana)
            if pygame.mouse.get_pressed()[0]:
                self.flag_menu = False
                self.flag_juego = True
        boton_jugar.dibujar(self.ventana)
        
    def gestion_botones(self):
        if self.flag_menu:
            self.menu_principal()
        elif self.flag_juego:
            self.nivel_1()
            
                
    def menu_principal(self):
        self.ventana.fill(MARRON)
        titulo_render = fuente.render(self.titulo, True, BLANCO)
        self.ventana.blit(titulo_render, (ANCHO // 2 - titulo_render.get_width() // 2, 100))
        self.ventana.blit(doom_sprite_pensando_derecha, (200, 150))
        self.boton_salir()
        self.boton_jugar()

    def nivel_1(self):
        self.ventana.fill(MARRON)
        self.ventana.blit(doom_sprite_pensando_medio, (200, 150))
        self.boton_salir()