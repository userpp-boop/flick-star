import pygame
from physics import calculate_acceleration

class Car:
    def __init__(self, x, y):
        self.position = pygame.Vector2(x, y)
        self.velocity = 0.0
        self.mass = 1500.0
        self.max_engine_force = 8000.0
        self.drag_coeff = 0.4
        self.friction_coeff = 0.015
        self.width = 100
        self.height = 40

    def update(self, dt, throttle):
        engine_force = throttle * self.max_engine_force
        accel = calculate_acceleration(engine_force, self.velocity, self.mass, self.drag_coeff, self.friction_coeff)
        self.velocity += accel * dt
        self.position.x += self.velocity * dt * 10

    def draw(self, surface):
        rect = pygame.Rect(surface.get_width() // 4, self.position.y - self.height // 2, self.width, self.height)
        pygame.draw.rect(surface, (200, 0, 0), rect)
