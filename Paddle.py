import pygame

from Position import Position


class Paddle(pygame.sprite.Sprite):
    def __init__(self, left: int, top: int, width: int, height: int, color: pygame.Color, directionChangeOnCollision: Position, maxSpeed: int = 800) -> None:
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.Surface((width, height))
        self.image.fill(color)
        self.rect = self.image.get_rect(topleft = (left, top))
        self.mask = pygame.mask.from_surface(self.image)
        self.directionChangeOnCollision = directionChangeOnCollision
        self.movementsInARow = 0
        self.maxSpeed = maxSpeed
        self.moveUp = False
        self.moveDown = False

    def get_speed(self) -> int:
        speed = 300+(0.5*self.movementsInARow**2)

        if speed > self.maxSpeed:
            return self.maxSpeed
        return speed

    def move_up(self) -> None:
        self.moveUp = True

    def move_down(self) -> None:
        self.moveDown = True

    def update(self, dt):
        if self.moveUp or self.moveDown:
            self.movementsInARow += 1
        if self.moveUp:
            self.rect.y += round(self.get_speed() * -1 * dt)
            self.moveUp = False
        if self.moveDown:
            self.rect.y += round(self.get_speed() * dt)
            self.moveDown = False