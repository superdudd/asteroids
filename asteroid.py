import pygame
import random
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
    
    def split(self, asteroids):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
           angle = random.uniform(20, 50)
           velocity1 = self.velocity.rotate(angle)
           velocity2 = self.velocity.rotate(-angle)
           old_radius = self.radius
           new_radius = old_radius - ASTEROID_MIN_RADIUS
           asteroid1 = Asteroid(self.position.x, self.position.y, new_radius)
           asteroid2 = Asteroid(self.position.x, self.position.y, new_radius)
           asteroid1.velocity = velocity1 * 1.2
           asteroid2.velocity = velocity2 * 1.2
           asteroids.add(asteroid1, asteroid2)

            
        
