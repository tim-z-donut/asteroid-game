import pygame
from circleshape import CircleShape

class Asteroid(CircleShape):
    instance = 1
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.instance = self.instance
        Asteroid.instance+=1
        self.radius = radius
    
    def draw(self, screen):
        pygame.draw.circle(screen,'red', self.position,self.radius, 2)
        print(f"asteroid {self.instance} at {self.position} with size of {self.radius}")
    def update(self, dt):
        self.position = self.position + self.velocity * dt