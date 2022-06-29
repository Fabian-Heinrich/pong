import pygame

from Position import Position
from Wall import Wall


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

    def handle_collisions(self, border_bottom: Wall, border_top: Wall, border_left: Wall, border_right: Wall):
        if pygame.sprite.collide_mask(self, border_bottom):
            self.direction *= Position(1, -1)
        if pygame.sprite.collide_mask(self, border_top):
            self.direction *= Position(1, -1)
        if pygame.sprite.collide_mask(self, border_left):
            self.direction *= Position(-1, 1)
        if pygame.sprite.collide_mask(self, border_right):
            self.direction *= Position(-1, 1)