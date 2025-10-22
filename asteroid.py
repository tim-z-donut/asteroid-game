import pygame
from circleshape import CircleShape
from constants import *
import random

class Asteroid(CircleShape):
    instance = 1
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.instance = self.instance
        Asteroid.instance+=1
        self.radius = radius
        self.color = 'red'
    
    def draw(self, screen):
        pygame.draw.circle(screen,self.color, self.position,self.radius, 2)
        # print(f"asteroid {self.instance} at {self.position} with size of {self.radius}")
    def update(self, dt):
        self.position += self.velocity * dt


    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return

        # New asteroids rotations and size
        original_position = self.position
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        angle = random.uniform(20,50)
        for count in range(0,2):
            if count == 1:
                angle *= -1
            vector = self.velocity.rotate(angle)
            # print(f"Angle used {angle}")
            asteroid = Asteroid(self.position[0], self.position[1], new_radius)
            asteroid.position.rotate(angle)
            asteroid.color = 'blue'
            asteroid.velocity = vector * 1.2
            # print(f"Split Asteroid at: {asteroid.position} with speed: {asteroid.velocity}")
            # print(f"Original position: {original_position}\n Original Velocity {self.velocity}")
            asteroid = None

