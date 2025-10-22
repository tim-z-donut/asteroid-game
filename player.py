from circleshape import CircleShape
from shot import Shot
from constants import *
import pygame
class Player(CircleShape):
    def __init__(self,x,y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        print(f"Player drawn at {self.position}")
        self.cooldown = 0
    
    # in the player class
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    def draw(self, screen):    
        pygame.draw.polygon(screen, "white", self.triangle(), 2)
        print(f"Player drawn at {self.position}")

    def rotate(self, dt):
        self.rotation = self.rotation + (PLAYER_TURN_SPEED * dt)

    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt

    def shoot(self):
        if self.cooldown <= 0:
            Shot(self.position[0], self.position[1], SHOT_RADIUS, self.rotation)
            print("Shot")
            self.cooldown = PLAYER_SHOOT_COOLDOWN


    def update(self, dt):
        keys = pygame.key.get_pressed()
        
        press = {'left' : keys[pygame.K_a] | keys[pygame.K_LEFT],
            'right' : keys[pygame.K_d] | keys[pygame.K_RIGHT],
            'forward' : keys[pygame.K_w] | keys[pygame.K_UP],
            'backward' : keys[pygame.K_s] | keys[pygame.K_DOWN],
            'shoot' : keys[pygame.K_SPACE]
        }

        if press['left']:
            self.rotate(dt*-1)
        if press['right']:
            self.rotate(dt)
        if press['forward']:
            self.move(dt)
        if press['backward']:
            self.move(dt*-1)
        if keys[pygame.K_SPACE]:
            self.shoot()
        self.cooldown -= dt
