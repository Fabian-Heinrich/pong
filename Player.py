import pygame

from Block import Block


class Player:
    def __init__(self, healthpoints: int, name: str, color: pygame.Color, paddle: Block, upKey: pygame.key, downKey: pygame.key) -> None:
        self.healthpoints = healthpoints
        self.name = name
        self.paddle = paddle
        self.upKey = upKey
        self.downKey = downKey