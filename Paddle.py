import pygame

from Position import Position


class Paddle(pygame.sprite.Sprite):
    def __init__(self, left: int, top: int, width: int, height: int, color: pygame.Color, directionChangeOnCollision: Position, maxSpeed: int = 13) -> None:
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.Surface((width, height))
        self.image.fill(color)
        self.rect = self.image.get_rect(topleft = (left, top))
        self.mask = pygame.mask.from_surface(self.image)
        self.directionChangeOnCollision = directionChangeOnCollision
        self.movementsInARow = 0
        self.maxSpeed = maxSpeed

    def get_speed(self) -> int:
        speed = 4+(0.05*self.movementsInARow**2)

        if speed > self.maxSpeed:
            return self.maxSpeed

        return speed

    def move_up(self) -> None:
        self.rect.y += self.get_speed() * -1
        self.movementsInARow += 1

    def move_down(self) -> None:
        self.rect.y += self.get_speed()
        self.movementsInARow += 1