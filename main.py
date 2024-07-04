from clase_juego import *

juego = Juego()

while juego.corriendo:
    juego.reloj.tick(juego.fps)
    juego.gestor_eventos()
    juego.gestion_botones()
    pygame.display.flip()
    