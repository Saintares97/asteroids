import pygame
from circleshape import CircleShape


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.x = x
        self.y = y
        self.radius = radius

        pygame.sprite.Sprite.__init__(self, self.containers)

        self.velocity = pygame.Vector2(0, 0)

    def draw(self, screen):
        color = (255, 255, 255)
        width = 2
        pygame.draw.circle(screen, color, (int(self.x), int(self.y)), self.radius, width)

    def update(self, dt):
        self.x += self.velocity.x * dt
        self.y += self.velocity.y * dt




