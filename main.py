import pygame
from constants import *
from player import Player
def main():
    print("Starting Asteroids!")
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    Player.containers = (updatable,drawable)
    player = Player(SCREEN_WIDTH / 2,SCREEN_HEIGHT / 2)


    # print(f"Screen width: {SCREEN_WIDTH}\nScreen height: {SCREEN_HEIGHT}")
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

        pygame.display.flip()
        
        dt = clock.tick(60)/1000
        # print(dt)

if __name__ == "__main__":
    main()
