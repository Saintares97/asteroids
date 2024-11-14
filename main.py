import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot
import sys


def main():
    pygame.init()
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    # set the screen size
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    # initialize delta time to 0
    dt = 0
    # create sprite groups
    asteroids = pygame.sprite.Group()
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    # add all instances of a class to assigned groups via containers
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable,)
    Shot.containers = (shots, updatable, drawable)

    asteroid_field = AsteroidField()
    p = Player(x = SCREEN_WIDTH / 2, y = SCREEN_HEIGHT / 2)
    
    # Game loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        # update game state
        for entity in updatable:
            entity.update(dt)

        # check for collision between asteroids and player object
        for entity in asteroids:
            if entity.is_colliding(p):
                print("Game over!")
                sys.exit()

        # check for collision between bullets and asteroids, kills both objects if true
        for asteroid in asteroids:
            for shot in shots:
                if shot.is_colliding(asteroid):
                    shot.kill()
                    asteroid.split()
 
        # fill the screen black
        screen.fill((0, 0, 0))
        
        # draw objects
        for entity in drawable:
            entity.draw(screen)


        pygame.display.flip()
        # Cap framerate to 60fps
        dt = clock.tick(60) / 1000
    



if __name__=="__main__":
    main()



