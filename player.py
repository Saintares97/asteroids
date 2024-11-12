import pygame
from circleshape import CircleShape
from constants import *
from shot import Shot

class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        self.timer = 0

    # in the player class
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    # draw shape for player
    def draw(self, screen):
        pygame.draw.polygon(screen, (255, 255, 255), self.triangle(), 2)
    # add rotation to player
    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt
    # assign keybinds for player movement
    def update(self, dt):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rotate(-dt)
        if keys[pygame.K_d]:
            self.rotate(dt)
        
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(-dt)

        if keys[pygame.K_SPACE]:
            self.shoot()

        if self.timer > 0:
            self.timer -= dt
        
    # player movement method
    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt

    # player shoot method. shoots in the direction the player is facing
    def shoot(self):
        if not self.timer > 0:
            shot = Shot(self.position.x, self.position.y)
            direction = pygame.Vector2(0, 1).rotate(self.rotation)
            shot.velocity = direction * PLAYER_SHOOT_SPEED
            self.timer = PLAYER_SHOOTING_COOLDOWN       # Limits rate of fire
    







    

