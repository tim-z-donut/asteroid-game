import pygame
from circleshape import CircleShape
from constants import *

class Shot(CircleShape):
    def __init__(self, x, y, radius, rotation):
        super().__init__(x,y,radius)
        self.rotation = rotation
        self.velocity = PLAYER_SHOOT_SPEED * pygame.Vector2(0, 1)
        self.forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += self.forward * 30

    def update(self, dt):
        self.position += self.forward * PLAYER_SHOOT_SPEED * dt

    def draw(self, screen):
        pygame.draw.circle(screen,'purple', self.position,self.radius, 2)
    
    def hit(self, asteroid, score):
        if self.is_colliding(asteroid):
            score.score+=SCORE_INCREMENT
            asteroid.split()
            self.kill()

