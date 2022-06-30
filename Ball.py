import pygame

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
        pygame.draw.circle(self.image, color, (radius*2,radius*2), radius)
        self.image.set_colorkey((0,0,0))

        self.rect = self.image.get_rect(center = center.get_pos())
        self.mask = pygame.mask.from_surface(self.image)

    def update(self):
        self.rect.x += self.direction.x
        self.rect.y += self.direction.y

    def draw(self, screen: pygame.Surface):
        screen.blit(self.image, self.rect)

    def handle_collisions(self, walls: pygame.sprite.Group):
        for wall in walls:
            if pygame.sprite.collide_mask(self, wall):
                self.direction *= wall.directionChangeOnCollision