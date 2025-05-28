import pygame
from circleshape import *
from constants import *
from player import *
class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        
    def draw(self, screen, color, line_width):
        pygame.draw.circle(screen, color, self.position, self.radius, line_width)
    def update(self, dt):
        self.position += self.velocity * dt