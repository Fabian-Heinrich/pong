import pygame
from Block import Block

from Paddle import Paddle


class Player:
    def __init__(self, healthpoints: int, name: str, color: pygame.Color, paddle: Paddle, upKey, downKey, wall: Block) -> None:
        self.healthpoints = healthpoints
        self.name = name
        self.paddle = paddle
        self.upKey = upKey
        self.downKey = downKey
        self.wall = wall
    
    def lose_hp(self):
        if self.healthpoints > 0:
            self.healthpoints -= 1
            return self.healthpoints 

        return 0