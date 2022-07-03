import pygame

from Paddle import Paddle


class Player:
    def __init__(self, healthpoints: int, name: str, color: pygame.Color, paddle: Paddle, upKey, downKey) -> None:
        self.healthpoints = healthpoints
        self.name = name
        self.paddle = paddle
        self.upKey = upKey
        self.downKey = downKey