import pygame
import os

class Background:
    def __init__(self, w, h):
        self.w, self.h = w, h
        self.scroll = 0
        self.image = self.load_background()

    def load_background(self):
        path = os.path.join('assets', 'images', 'najaf_street.png')
        if os.path.exists(path):
            return pygame.transform.scale(pygame.image.load(path), (self.w, self.h))
        return None

    def update(self, v, dt):
        self.scroll = (self.scroll + v * dt * 10) % self.w

    def draw(self, surf):
        if self.image:
            surf.blit(self.image, (-self.scroll, 0))
            surf.blit(self.image, (self.w - self.scroll, 0))
        else:
            surf.fill((100, 100, 100))
            # Draw road
            pygame.draw.rect(surf, (50, 50, 50), (0, self.h // 2, self.w, self.h // 2))
