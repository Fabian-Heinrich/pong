import pygame
import pygame.gfxdraw

from Position import Position
from Block import Block


class Ball(pygame.sprite.Sprite):

    def __init__(self, radius, color, center: Position, direction: Position) -> None:
        pygame.sprite.Sprite.__init__(self)

        self.center = center
        self.radius = radius
        self.color = color
        self.direction = direction

        self.image = pygame.Surface((radius*4,radius*4))
        pygame.gfxdraw.aacircle(self.image, radius*2, radius*2, radius, color)
        pygame.gfxdraw.filled_circle(self.image, radius*2, radius*2, radius, color)
        self.image.set_colorkey((0,0,0))

        self.rect = self.image.get_rect(center = center.get_pos())
        self.mask = pygame.mask.from_surface(self.image)

    def update(self, dt):
        self.rect.x += round(self.direction.x * dt)
        self.rect.y += round(self.direction.y * dt)

    def draw(self, screen: pygame.Surface):
        screen.blit(self.image, self.rect)