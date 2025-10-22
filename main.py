import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
def main():
    print("Starting Asteroids!")
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    Player.containers = (updatable,drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    player = Player(SCREEN_WIDTH / 2,SCREEN_HEIGHT / 2)
    asteroidfield = AsteroidField()

    clock = pygame.time.Clock()
    dt = 0

    while True:
        for event in pygame.event.get():
            # print(event)
            if event.type == pygame.QUIT:
                return
        screen.fill("black")

        updatable.update(dt)
        for obj in drawable:
            obj.draw(screen)
        print(f"Asteroid count: {len(asteroids)}")
        pygame.display.flip()
        
        dt = clock.tick(60)/1000

if __name__ == "__main__":
    main()
