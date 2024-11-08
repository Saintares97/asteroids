import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField


def main():
    pygame.init()
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    
    dt = 0
    asteroids = pygame.sprite.Group()
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)

    AsteroidField.containers = (updatable,)

    asteroid_field = AsteroidField()
    p = Player(x = SCREEN_WIDTH / 2, y = SCREEN_HEIGHT / 2)
    
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

       
        for entity in updatable:
            entity.update(dt)   
 

        screen.fill((0, 0, 0))
        
        
        for entity in drawable:
            entity.draw(screen)

       
        pygame.display.flip()
        dt = clock.tick(60) / 1000
    



if __name__=="__main__":
    main()



