import pygame
import random
from circleshape import *
from constants import *

class Asteroid (CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
    
    def split(self):

        self.kill()

        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        
        angle = random.uniform(20, 50)

        velocity1 = self.velocity.rotate(angle)
        velocity2 = self.velocity.rotate(-angle)

        radius = self.radius - ASTEROID_MIN_RADIUS

        asteroid1 = Asteroid(self.position.x, self.position.y, radius)
        asteroid1.velocity = velocity1 * 1.2
        
        asteroid2 = Asteroid(self.position.x, self.position.y, radius)
        asteroid2.velocity = velocity2 * 1.2 

    def draw(self, screen):
        pygame.draw.circle(screen, "white", (int(self.position.x), int(self.position.y)), self.radius, 2)
    
    def update(self, dt):
        self.position += self.velocity * dt