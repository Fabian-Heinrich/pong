import random
import pygame

from Ball import Ball
from Color import Color
from Paddle import Paddle
from Player import Player
from Position import Position
from Block import Block
from Scenes.End import End
from Scenes.Play import Play
from Scenes.Start import Start

class Game:
    def __init__(self, width, height, FPS) -> None:
        pygame.init()

        self.FPS = FPS

        self.clock = pygame.time.Clock()
        self.defaultFont = pygame.font.SysFont(pygame.font.get_default_font(), 50)

        self.size = self.width, self.height = width, height
        self.screen = pygame.display.set_mode(self.size)

        self.activeScene = Start(self.screen)


    def run(self):
        while self.activeScene != None:
            dt = self.clock.tick(self.FPS)/1000

            self.handle_events()
            self.activeScene.update(dt)
            self.activeScene.render()
            self.draw_fps_text()

            pygame.display.update()

            self.activeScene = self.activeScene.nextScene

    def handle_events(self):
        
        events = []
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.activeScene.terminate()
            else:
                events.append(event)

        pressedKeys = pygame.key.get_pressed()

        self.activeScene.handle_events(events, pressedKeys)

    def draw_fps_text(self):
        fpsRoundedText = "FPS: " + str(round(self.clock.get_fps()))
        fpsTextRendered = self.defaultFont.render(fpsRoundedText, True, Color.WHITE)

        self.screen.blit(fpsTextRendered, (10,10))