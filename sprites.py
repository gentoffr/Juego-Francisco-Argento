from boton import *

class Sprites:
    def __init__(self, image):
        self.sheet = image
        self.tiempo = 0

    def transformar_imagen(self, frame, width, height, escala):
        rect = pygame.Rect((frame * width, 0, width, height))
        image = self.sheet.subsurface(rect).copy()
        image = pygame.transform.scale(image, (width * escala, height * escala))
        return image
    
    def loop_idle(self, frame_duration, total_frames, width, height, escala, delay=0, stay_last_frame=False):
        self.tiempo += 1
        if self.tiempo <= delay:
            current_frame = 0
        else:
            if self.tiempo >= delay + frame_duration * total_frames:
                if stay_last_frame:
                    current_frame = total_frames - 1
                else:
                    self.tiempo = 0
                    current_frame = 0
            else:
                current_frame = ((self.tiempo - delay) // frame_duration) % total_frames
        return self.transformar_imagen(current_frame, width, height, escala)