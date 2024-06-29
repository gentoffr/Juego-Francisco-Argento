from Imagenes import *

class Juego:
    def __init__(self):
        self.ventana = ventana
        self.fps = FPS
        self.reloj = pygame.time.Clock()
        self.corriendo = True
        self.titulo = "Juego bien malandro"
        self.flag_menu = True
        self.flag_transicion = False
        self.flag_juego = False
        self.monedas = 0
        self.record_monedas = 0
        self.doomguy = Sprites(pygame.image.load("src\Doomguy_fijandose.png"))
        self.doomguy_ay_1 = Sprites(pygame.image.load("src\Doomguy_fijandose_lastimado_1.png"))
        self.doomguy_ay_2 = Sprites(pygame.image.load("src\Doomguy_fijandose_lastimado_2.png"))
        self.doomguy_ay_3 = Sprites(pygame.image.load("src\Doomguy_fijandose_lastimado_3.png"))
        self.doomguy_ay_4 = Sprites(pygame.image.load("src\Doomguy_fijandose_lastimado_4.png"))
        self.doomguy_aciertos = Sprites(pygame.image.load("src\Aciertos.png"))
        self.doomguy_errores = Sprites(pygame.image.load("src\Errores.png"))
        self.imagen_moneda = Sprites(pygame.image.load("src\Moneda.png"))
        self.cortinas = Sprites(pygame.image.load("src\Cortinas_149_89.png"))
        self.lista_total = crear_lista("src\Imagenes")
        self.adidas = self.lista_total["Adidas"]
        self.apple = self.lista_total["Apple"]
        self.boca = self.lista_total["Boca"]
        self.coca = self.lista_total["Coca"]
        self.facebook = self.lista_total["Facebook"]
        self.ferrari = self.lista_total["Ferrari"]
        self.google = self.lista_total["Google"]
        self.instagram = self.lista_total["Instagram"]
        self.mcdonalds = self.lista_total["Mcdonalds"]
        self.nike = self.lista_total["Nike"]
        self.pepsi = self.lista_total["Pepsi"]
        self.twitter = self.lista_total["Twitter"]
        self.whatsapp = self.lista_total["Whatsapp"]
        self.windows = self.lista_total["Windows"]
        self.youtube = self.lista_total["Youtube"]
        self.correctas = [self.lista_total[key][0] for key in self.lista_total]
        self.x_doomguy = ANCHO // 2 - 60
        self.x_cortina = ANCHO
        self.posiciones = [i * 250 for i in range(len(self.correctas))]

    def gestor_eventos(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.corriendo = False

    def boton_salir(self, place, size, color_normal, color_activo, mensaje, fuente, color_texto):
        boton_salir = Boton(place, size, color_normal, color_activo, mensaje, fuente, color_texto)
        if boton_salir.esta_sobre(pygame.mouse.get_pos()):
            boton_salir.color_actual = ROJO
            boton_salir.dibujar(self.ventana, True)
            if pygame.mouse.get_pressed()[0]:
                self.corriendo = False
        boton_salir.dibujar(self.ventana, True)

    def boton_jugar(self, place, size, color_normal, color_activo, mensaje, fuente, color_texto):
        boton_jugar = Boton(place, size, color_normal, color_activo, mensaje, fuente, color_texto)
        if boton_jugar.esta_sobre(pygame.mouse.get_pos()):
            boton_jugar.color_actual = VERDE
            boton_jugar.dibujar(self.ventana, True)
            if pygame.mouse.get_pressed()[0]:
                self.flag_menu = False
                self.flag_juego = True
                self.flag_transicion = True
        boton_jugar.dibujar(self.ventana, True)
        
    def gestion_botones(self):
        if self.flag_menu:
            self.menu_principal()
        elif self.flag_transicion:
            self.transicion()
        elif self.flag_juego:
            self.jugando()
                
    def menu_principal(self):
        self.ventana.fill(COLOR_FONDO)
        self.info()
        self.ventana.blit(self.doomguy.loop_idle(120, 3, 24, 29, 5, 200), (ANCHO // 2 -60, ALTO // 2-200))
        self.boton_salir((ANCHO // 2 + 100, ALTO // 2 +100), (100, 100), BLANCO, ROJO, "SALIR", fuente, NEGRO)
        self.boton_jugar((ANCHO // 2 - 100, ALTO // 2+100), (100, 100), BLANCO, VERDE, "JUGAR", fuente, NEGRO)
        self.tira_imagenes()

    def transicion(self):
        self.ventana.fill(COLOR_FONDO)
        if self.x_doomguy > 200:
            self.x_doomguy -= 2
        if self.x_cortina > (ANCHO // 2) - 100:
            self.x_cortina -= 2
        else:
            self.flag_transicion = False
        self.ventana.blit(self.doomguy_aciertos.transformar_imagen(0, 24, 29, 5), (self.x_doomguy, ALTO // 2-200))
        self.ventana.blit(self.cortinas.transformar_imagen(0, 149, 89, 3), (self.x_cortina, ALTO // 2-200))
        self.info()
        self.boton_salir((ANCHO - 50, 100), (100, 100), BLANCO, ROJO, "SALIR", fuente, NEGRO)

    def info(self):
        panel = pygame.Rect(0, 0, ANCHO, 60)
        pygame.draw.rect(self.ventana, NARANJA, panel)
        recuadro_monedas = pygame.surface.Surface((100, 60))
        recuadro_monedas.fill(VERDE_AQUAMARINA)
        pygame.draw.rect(recuadro_monedas, (0, 0, 0), recuadro_monedas.get_rect(), 5)
        self.ventana.blit(recuadro_monedas, (0, 0))
        titulo_render = fuente.render(self.titulo, True, BLANCO)
        self.ventana.blit(titulo_render, (ANCHO // 2 - titulo_render.get_width() // 2, 100))
        monedas_render = fuente.render(f"{self.monedas}", True, BLANCO)
        self.ventana.blit(monedas_render, (60, 11))
        self.ventana.blit(self.imagen_moneda.loop_idle(10, 8, 47, 47, 1), (5, 7))
    
    def tira_imagenes(self):
        altura_imagen = 200 
        espacio_entre_imagenes = 250  
        for i in range(len(self.correctas)):
            self.posiciones[i] -= 1
            if self.posiciones[i] < - 200:
                self.posiciones[i] = max(self.posiciones) + espacio_entre_imagenes
            ventana.blit(self.correctas[i], (self.posiciones[i], ALTO - altura_imagen - 10))
    
    def jugando(self):
        self.ventana.fill(COLOR_FONDO)
        cuadrado = pygame.Surface((140 * 3, 80 * 3))
        cuadrado.fill(BLANCO)
        self.ventana.blit(cuadrado, (self.x_cortina + 9, ALTO // 2-200))
        self.ventana.blit(self.doomguy.loop_idle(120, 3, 24, 29, 5, 200), (self.x_doomguy, ALTO // 2-200))
        self.ventana.blit(self.cortinas.loop_idle(10, 15, 149, 89, 3, 0, True), (self.x_cortina, ALTO // 2-200))
        self.info()
        self.boton_salir((ANCHO - 50, 100), (100, 100), BLANCO, ROJO, "SALIR", fuente, NEGRO)
