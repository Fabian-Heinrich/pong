import pygame


class Wall(pygame.sprite.Sprite):
    def __init__(self, left: int, top: int, width: int, height: int, color: pygame.Color) -> None:
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.Surface((width, height))
        self.image.fill(color)
        self.rect = self.image.get_rect(topleft = (left, top))
        self.mask = pygame.mask.from_surface(self.image)