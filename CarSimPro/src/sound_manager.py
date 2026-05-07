import pygame
import os

class SoundManager:
    def __init__(self):
        try:
            pygame.mixer.init()
        except pygame.error:
            print("Warning: Mixer could not be initialized.")

        self.engine_sound = None
        self.load_sounds()

    def load_sounds(self):
        path = os.path.join('assets', 'sounds', 'engine_v8.wav')
        if os.path.exists(path):
            try:
                self.engine_sound = pygame.mixer.Sound(path)
                self.engine_sound.play(-1)
            except pygame.error:
                print("Warning: Could not play engine sound.")

    def update(self, velocity):
        if self.engine_sound:
            try:
                volume = min(0.1 + (abs(velocity) / 100.0), 1.0)
                self.engine_sound.set_volume(volume)
            except pygame.error:
                pass
