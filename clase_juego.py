from Imagenes import *
import random
import json
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
        self.flag_correcta = False
        self.monedas = 0
        self.record_monedas = 0
        self.record_tiempo = 0
        self.doomguy = Sprites(pygame.image.load("src\Doomguy_fijandose.png"))
        self.doomguy_ay_1 = Sprites(pygame.image.load("src\Doomguy_fijandose_lastimado_1.png"))
        self.doomguy_ay_2 = Sprites(pygame.image.load("src\Doomguy_fijandose_lastimado_2.png"))
        self.doomguy_ay_3 = Sprites(pygame.image.load("src\Doomguy_fijandose_lastimado_3.png"))
        self.doomguy_ay_4 = Sprites(pygame.image.load("src\Doomguy_fijandose_lastimado_4.png"))
        self.doomguy_aciertos = Sprites(pygame.image.load("src\Aciertos.png"))
        self.doomguy_errores = Sprites(pygame.image.load("src\Errores.png"))
        self.imagen_moneda = Sprites(pygame.image.load("src\Moneda.png"))
        self.cortinas = Sprites(pygame.image.load("src\Cortinas_149_89.png"))
        self.cortinas_cerrandose = Sprites(pygame.image.load("src\Cortinas_cerrandose.png"))
        self.cero_vidas = Sprites(pygame.image.load(r"src\0_vidas.png"))
        self.una_vida = Sprites(pygame.image.load(r"src\1_vida.png"))
        self.dos_vidas = Sprites(pygame.image.load(r"src\2_vidas.png"))
        self.tres_vidas = Sprites(pygame.image.load(r"src\3_vidas.png"))
        self.cuatro_vidas = Sprites(pygame.image.load(r"src\4_vidas.png"))
        self.cinco_vidas = Sprites(pygame.image.load(r"src\5_vidas.png"))
        self.over = Sprites(pygame.image.load(r"src\Over.png"))
        self.UHHHHH = Sprites(pygame.image.load(r"src\UHHHHHH.png"))
        self.doomGOD = Sprites(pygame.image.load("src\DoomGOD.png"))
        self.vidas = 5
        self.lista_total = crear_lista("src\Imagenes")
        self.adidas = self.lista_total["Adidas"]
        self.apple = self.lista_total["Apple"]
        self.boca = self.lista_total["Boca Juniors"]
        self.coca = self.lista_total["Coca-Cola"]
        self.facebook = self.lista_total["Facebook"]
        self.ferrari = self.lista_total["Ferrari"]
        self.google = self.lista_total["Google"]
        self.instagram = self.lista_total["Instagram"]
        self.mcdonalds = self.lista_total["McDonalds"]
        self.nike = self.lista_total["Nike"]
        self.pepsi = self.lista_total["Pepsi"]
        self.twitter = self.lista_total["Twitter"]
        self.whatsapp = self.lista_total["WhatsApp"]
        self.windows = self.lista_total["Windows"]
        self.youtube = self.lista_total["YouTube"]
        self.lista_indices_disponibles = list(range(len(self.lista_total)))
        self.usadas = set()
        self.lista_para_resetear = self.lista_total
        self.correctas = [self.lista_total[key][0] for key in self.lista_total]
        self.x_doomguy = ANCHO // 2 - 60
        self.x_cortina = ANCHO
        self.posiciones = [i * 250 for i in range(len(self.correctas))]
        self.activar_rng = True
        self.sep = 60
        self.pos_inicial_imagen_x = (ANCHO - (4 * 200 + 3 * self.sep)) // 2
        self.logo_en_juego = None
        self.correcta_en_juego = None
        self.nombre_correcta = None
        self.pos_inicial_imagen_y = ALTO - 200 - 10
        self.pos_correcta = None
        self.tiempo = 0
        self.flag_incorrecta = False
        self.flag_ganar = False
        self.tiempo_ronda = 0
        self.tiempos = []
        self.tiempo_aux = 0
        self.monedas_obtenidas = 0
        self.contador_aciertos = 0
        self.flag_perder = False
        self.flag_vida_bajando = False
        self.cargar_records()
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
                self.flag_transicion = True
        boton_jugar.dibujar(self.ventana, True)
        
    def gestion_botones(self):
        if self.flag_menu:
            self.menu_principal()
        elif self.flag_transicion:
            self.transicion()
        elif self.flag_juego:
            self.jugando()
        elif self.flag_correcta:
            self.acertar()
        elif self.flag_perder:
            self.its_over(self.UHHHHH.transformar_imagen(0, 24, 31, 5), self.over.transformar_imagen(0, 24, 31, 5), "ITS OVER", ROJO)
        elif self.flag_ganar:
            self.its_over(self.correcto(), self.doomGOD.transformar_imagen(0, 24, 29, 5), "YOU WIN", AMARILLITO)
                
    def menu_principal(self):
        self.ventana.fill(COLOR_FONDO)
        self.info()
        self.ventana.blit(self.doomguy.loop_idle(120, 3, 24, 29, 5, 200), (ANCHO // 2 -60, ALTO // 2-200))
        self.boton_salir((ANCHO // 2 + 100, ALTO // 2 +100), (100, 100), BLANCO, ROJO, "SALIR", fuente, NEGRO)
        self.boton_jugar((ANCHO // 2 - 100, ALTO // 2+100), (100, 100), BLANCO, VERDE, "JUGAR", fuente, NEGRO)
        titulo_render = fuente_nombres.render(self.titulo, True, BLANCO)
        self.ventana.blit(titulo_render, (ANCHO // 2 - titulo_render.get_width() // 2, 100))
        self.tira_imagenes()

    def transicion(self):
        self.ventana.fill(COLOR_FONDO)
        if self.x_doomguy > 200:
            self.x_doomguy -= 2
            print(self.x_doomguy)
        if self.x_cortina > (ANCHO // 2) - 100:
            self.x_cortina -= 2
        else:
            self.encontrar_logo()
            self.flag_transicion = False
            self.flag_juego = True
        self.ventana.blit(self.doomguy_aciertos.transformar_imagen(0, 24, 29, 5), (self.x_doomguy, ALTO // 2-200))
        self.ventana.blit(self.cortinas.transformar_imagen(0, 149, 89, 3), (self.x_cortina, ALTO // 2-200))
        self.info()
        self.boton_salir((ANCHO - 50, 100), (100, 100), BLANCO, ROJO, "SALIR", fuente, NEGRO)

    def info(self):
        panel = pygame.Rect(0, 0, ANCHO, 60)
        pygame.draw.rect(self.ventana, NARANJA, panel)
        recuadro_monedas = pygame.surface.Surface((120, 60))
        recuadro_monedas.fill(VERDE_AQUAMARINA)
        pygame.draw.rect(recuadro_monedas, (0, 0, 0), recuadro_monedas.get_rect(), 5)
        self.ventana.blit(recuadro_monedas, (0, 0))
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
        texto = fuente_nombres.render(self.nombre_correcta, True, NEGRO)
        pos_texto = texto.get_rect(center=(self.x_cortina + 223, ALTO // 2 - 50))
        self.ventana.blit(texto, pos_texto)
        self.ventana.blit(self.cortinas.loop_idle(10, 15, 149, 89, 3, 0, True), (self.x_cortina, ALTO // 2-200))
        if self.tiempo < 120:
            self.tiempo += 1
            self.info()
        else:
            self.generar_ronda()
        self.boton_salir((ANCHO - 50, 100), (100, 100), BLANCO, ROJO, "SALIR", fuente, NEGRO)

    def encontrar_logo(self):
        if self.activar_rng:
            if not self.lista_indices_disponibles:
                pass
            else:
                self.rng = random.choice(self.lista_indices_disponibles)
                self.nombre_correcta = self.reconocer_logo(self.rng)[1]
                self.usadas.add(self.nombre_correcta)
                self.lista_indices_disponibles.remove(self.rng)
                self.activar_rng = False
                self.logo_en_juego = self.reconocer_logo(self.rng)[0]
                self.correcta_en_juego = self.logo_en_juego[0]
                random.shuffle(self.logo_en_juego)
        
    def generar_ronda(self):
        if self.vidas == 0:
            self.flag_juego = False
            self.flag_perder = True
            self.tiempo = 0
        elif self.contador_aciertos >= 15:
            self.flag_juego = False
            self.flag_ganar = True
        else:
            self.tiempo_ronda += 1
            self.info()
            self.ventana.blit(self.vidas_actuales(self.vidas), (120, 0))
            self.ventana.blit(fuente.render(str(self.tiempo_ronda // 60), True, (BLANCO)), (100,100))
            if self.flag_incorrecta:
                self.tiempo_aux += 1
                if self.tiempo_aux < 60:
                    self.ventana.blit(self.incorrecto(), (self.x_doomguy, ALTO // 2-200))
                else:
                    self.tiempo_aux = 0
                    self.flag_incorrecta = False
            if not hasattr(self, 'mouse_button_down'):
                self.mouse_button_down = False
            for i in range(len(self.logo_en_juego)):
                pos_x = self.pos_inicial_imagen_x + i * (200 + self.sep)
                imagen = self.logo_en_juego[i]
                if imagen is not None:
                    self.ventana.blit(imagen, (pos_x, self.pos_inicial_imagen_y))
                    rect_imagen = imagen.get_rect(topleft=(pos_x, self.pos_inicial_imagen_y))
                    colision = rect_imagen.collidepoint(pygame.mouse.get_pos())
                    if pygame.mouse.get_pressed()[0]:
                        if colision and not self.mouse_button_down:
                            self.mouse_button_down = True
                            if self.logo_en_juego[i] in self.correctas:
                                self.pos_correcta = rect_imagen
                                self.monedas += 20
                                self.monedas_obtenidas += 20
                                self.contador_aciertos += 1
                                self.tiempos.append(self.tiempo_ronda / 60)
                                self.tiempo = 0
                                self.tiempo_ronda = 0
                                self.flag_correcta = True
                                self.flag_juego = False
                            else:
                                self.logo_en_juego[i] = None
                                self.vidas -= 1
                                self.monedas -= 10
                                if self.monedas < 0:
                                    self.monedas = 0
                                self.monedas_obtenidas -= 10
                                self.flag_vida_bajando = True
                                self.flag_incorrecta = True
            else:
                self.mouse_button_down = False


    def acertar(self):
        self.tiempo += 1
        self.boton_salir((ANCHO - 50, 100), (100, 100), BLANCO, ROJO, "SALIR", fuente, NEGRO)
        self.ventana.blit(self.imagen_moneda.loop_idle(10, 8, 47, 47, 1), (5, 7))
        cuadrado = pygame.Surface((50, 40))
        cuadrado.fill(VERDE_AQUAMARINA)
        self.ventana.blit(cuadrado, (60, 11))
        monedas_render = fuente.render(f"{self.monedas}", True, BLANCO)
        self.ventana.blit(monedas_render, (60, 11))
        if self.tiempo < 180:
            pygame.draw.rect(self.ventana, (VERDE), self.pos_correcta, 5)
            self.ventana.blit(self.correcto(), (self.x_doomguy, ALTO // 2-200))
            self.ventana.blit(self.cortinas_cerrandose.loop_idle(10, 15, 149, 89, 3, 0, True), (self.x_cortina, ALTO // 2-200))
        elif self.tiempo < 360:
            tapon = pygame.Surface((1024, 250))
            tapon.fill(COLOR_FONDO)
            ventana.blit(tapon, (0, ALTO - 250))
        else:
            self.flag_correcta = False
            self.activar_rng = True
            self.flag_juego = True
            self.encontrar_logo()


    def reconocer_logo(self, numero):
        match numero:
            case 0:
                return self.adidas, "Adidas"
            case 1:
                return self.apple, "Apple"
            case 2:
                return self.boca, "Boca Juniors"
            case 3:
                return self.coca, "Coca-Cola"
            case 4:
                return self.facebook, "Facebook"
            case 5:
                return self.ferrari, "Ferrari"
            case 6:
                return self.google, "Google"
            case 7:
                return self.instagram, "Instagram"
            case 8:
                return self.mcdonalds, "McDonalds"
            case 9:
                return self.nike, "Nike"
            case 10:
                return self.pepsi, "Pepsi"
            case 11:
                return self.twitter, "Twitter"
            case 12:
                return self.whatsapp, "WhatsApp"
            case 13:
                return self.windows, "Windows"  
            case 14:
                return self.youtube, "YouTube"
    
    def vidas_actuales(self, numero):
        match numero:
            case 0:
                return self.cero_vidas.transformar_imagen(0, 1685, 291, 0.2)
            case 1:
                if self.flag_vida_bajando:
                    self.flag_vida_bajando = False
                    self.doomguy = Sprites(pygame.image.load("src\Doomguy_fijandose_lastimado_4.png"))
                return self.una_vida.transformar_imagen(0, 1685, 291, 0.2)
            case 2:
                if self.flag_vida_bajando:
                    self.flag_vida_bajando = False
                    self.doomguy = Sprites(pygame.image.load("src\Doomguy_fijandose_lastimado_3.png"))
                return self.dos_vidas.transformar_imagen(0, 1685, 291, 0.2)
            case 3:
                if self.flag_vida_bajando:
                    self.flag_vida_bajando = False
                    self.doomguy = Sprites(pygame.image.load("src\Doomguy_fijandose_lastimado_2.png"))
                return self.tres_vidas.transformar_imagen(0, 1685, 291, 0.2)
            case 4:
                if self.flag_vida_bajando:
                    self.flag_vida_bajando = False
                    self.doomguy = Sprites(pygame.image.load("src\Doomguy_fijandose_lastimado_1.png"))
                return self.cuatro_vidas.transformar_imagen(0, 1685, 291, 0.2)
            case 5:
                return self.cinco_vidas.transformar_imagen(0, 1685, 291, 0.2)

    def correcto(self):
        match self.vidas:
            case 1:
                return self.doomguy_aciertos.transformar_imagen(4, 24, 29, 5)
            case 2:
                return self.doomguy_aciertos.transformar_imagen(3, 24, 29, 5)
            case 3:
                return self.doomguy_aciertos.transformar_imagen(2, 24, 29, 5)
            case 4:
                return self.doomguy_aciertos.transformar_imagen(1, 24, 29, 5)
            case 5:
                return self.doomguy_aciertos.transformar_imagen(0, 24, 29, 5)
            
    def incorrecto(self):
        match self.vidas:
            case 0:
                return self.over.transformar_imagen(0, 24, 31, 5)
            case 1:
                return self.doomguy_errores.transformar_imagen(4, 24, 29, 5)
            case 2:
                return self.doomguy_errores.transformar_imagen(3, 24, 29, 5)
            case 3:
                return self.doomguy_errores.transformar_imagen(2, 24, 29, 5)
            case 4:
                return self.doomguy_errores.transformar_imagen(1, 24, 29, 5)
            case 5:
                return self.doomguy_errores.transformar_imagen(0, 24, 29, 5)
    
    def its_over(self, imagen, imagen2, texto, color):
        self.ventana.fill(COLOR_FONDO)
        self.info()
        self.tiempo_aux += 1
        if self.tiempo_aux < 120:
            self.calcular_stats()
            self.guardar_records()
            self.ventana.blit(imagen, (self.x_doomguy, ALTO // 2 - 200))
        elif self.tiempo_aux < 360:
            if self.x_doomguy < ANCHO // 2 - 60:
                self.x_doomguy += 2
            self.ventana.blit(imagen, (self.x_doomguy, ALTO // 2 - 200))
        elif self.tiempo_aux < 480:
            self.ventana.blit(imagen2, (self.x_doomguy, ALTO // 2 - 200))
            # self.ventana.blit(self.monedas_obtenidas, (ANCHO // 2, ALTO // 2))
        elif self.tiempo_aux < 1080:
            self.ventana.blit(imagen2, (self.x_doomguy, ALTO // 2 - 200))
            self.ventana.blit(fuente.render(f"Monedas obtenidas esta partida: {self.monedas}", True, BLANCO), (ANCHO // 2, ALTO // 2))
            self.ventana.blit(fuente.render(f"Record de monedas obtenidas: {self.record_monedas}", True, BLANCO), (ANCHO // 2, ALTO // 2 + 40))
            if self.calcular_stats() == float('inf'):
                self.ventana.blit(fuente.render(f"Promedio de tiempo por ronda: N/A", True, BLANCO), (ANCHO // 2, ALTO // 2 + 80))
            else:
                self.ventana.blit(fuente.render(f"Promedio de tiempo por ronda: {self.calcular_stats()}s", True, BLANCO), (ANCHO // 2, ALTO // 2 + 80))
            self.ventana.blit(fuente.render(f"Promedio record por ronda: {self.record_tiempo}s", True, BLANCO), (ANCHO // 2, ALTO // 2 + 120))
        else:
            self.fade_in_out_text(texto, color)
            
    
    def calcular_stats(self):
        if self.contador_aciertos:
            promedio_tiempo = sum(self.tiempos) / self.contador_aciertos
            promedio_tiempo = round(promedio_tiempo, 2)
        else:
            promedio_tiempo = float('inf')
        if promedio_tiempo < self.record_tiempo:
            self.record_tiempo = promedio_tiempo
        if self.monedas_obtenidas > self.record_monedas:
            self.record_monedas = self.monedas_obtenidas
        return promedio_tiempo
    def cargar_records(self):
        try:
            with open('records.json', 'r') as file:
                data = json.load(file)
                self.record_monedas = data.get('record_monedas', 0)
                self.record_tiempo = data.get('record_tiempo', 0)
                self.monedas = data.get('monedas', 0)
        except Exception:
            pass

    def guardar_records(self):
        data = {
            'record_monedas': self.record_monedas,
            'record_tiempo': self.record_tiempo,
            'monedas': self.monedas
        }
        with open('records.json', 'w') as file:
            json.dump(data, file, indent=4)
        
    def fade_in_out_text(self, text, color):
        fade_duration = 2000  # Duración de fade en milisegundos
        text_duration = 3000  # Duración del texto en pantalla en milisegundos
        
        # Aumentar el tiempo en cada llamada al método
        self.tiempo += 1
        
        # Calcular la duración total en frames
        fade_frames = fade_duration // (1000 // 60)  # Conversión a frames considerando FPS
        text_frames = text_duration // (1000 // 60)  # Conversión a frames considerando FPS

        # Crear superficies para el fade y el texto
        fade_surface = pygame.Surface((ANCHO, ALTO))
        fade_surface.fill(NEGRO)
        text_surface = fuente_nombres.render(text, True, color)

        # Si el tiempo es menor que la duración del fade, hacer fade out
        if self.tiempo < fade_frames:
            alpha = (self.tiempo * 255) // fade_frames
            fade_surface.set_alpha(alpha)
            self.ventana.blit(fade_surface, (0, 0))
        # Si el tiempo está entre el fade y la duración del texto, mostrar el texto
        elif self.tiempo < fade_frames + text_frames: 
            fade_surface.set_alpha(0)
            self.ventana.fill(NEGRO)
            text_alpha = ((self.tiempo - fade_frames) * 255) // text_frames
            text_surface.set_alpha(text_alpha)
            self.ventana.blit(text_surface, (ANCHO // 2 - text_surface.get_width() // 2, ALTO // 2 - text_surface.get_height() // 2))
            self.ventana.blit(fade_surface, (0, 0))
            
        # Cuando se superan las duraciones de fade y texto, resetear y cambiar flags
        else:
            print("Entrando al último else...")
            self.reiniciar_juego()

        # Debugging: Mostrar el valor actual de self.tiempo
        print("Tiempo actual:", self.tiempo)
    # ... [código existente] ...

    def reiniciar_juego(self):
        self.flag_menu = True
        self.flag_transicion = False
        self.flag_juego = False
        self.flag_correcta = False
        self.vidas = 5
        self.x_doomguy = ANCHO // 2 - 60
        self.x_cortina = ANCHO
        self.tiempo = 0
        self.flag_incorrecta = False
        self.flag_ganar = False
        self.doomguy = Sprites(pygame.image.load("src\Doomguy_fijandose.png"))
        self.lista_total = self.lista_para_resetear
        self.tiempo_ronda = 0
        self.tiempos = []
        self.tiempo_aux = 0
        self.monedas_obtenidas = 0
        self.contador_aciertos = 0
        self.flag_perder = False
        self.flag_vida_bajando = False
        self.activar_rng = True
        self.lista_indices_disponibles = list(range(len(self.lista_total)))
        self.usadas = set()
        self.logo_en_juego = None
        self.correcta_en_juego = None
        self.nombre_correcta = None
        self.pos_correcta = None
        self.adidas = self.lista_total["Adidas"]
        self.apple = self.lista_total["Apple"]
        self.boca = self.lista_total["Boca Juniors"]
        self.coca = self.lista_total["Coca-Cola"]
        self.facebook = self.lista_total["Facebook"]
        self.ferrari = self.lista_total["Ferrari"]
        self.google = self.lista_total["Google"]
        self.instagram = self.lista_total["Instagram"]
        self.mcdonalds = self.lista_total["McDonalds"]
        self.nike = self.lista_total["Nike"]
        self.pepsi = self.lista_total["Pepsi"]
        self.twitter = self.lista_total["Twitter"]
        self.whatsapp = self.lista_total["WhatsApp"]
        self.windows = self.lista_total["Windows"]
        self.youtube = self.lista_total["YouTube"]
        self.encontrar_logo()


