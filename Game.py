import sys
import pygame

from Ball import Ball
from Player import Player
from Position import Position
from Block import Block


class Game:

    WHITE = pygame.Color(255,255,255)
    BLACK = pygame.Color(0,0,0)
    RED = pygame.Color(255,0,0)
    GREEN = pygame.Color(0,255,0)
    BLUE = pygame.Color(0,0,255)

    PADDLE_SPEED = 6

    def __init__(self, width, height, FPS) -> None:
        pygame.init()

        self.FPS = FPS

        self.clock = pygame.time.Clock()
        self.defaultFont = pygame.font.SysFont(pygame.font.get_default_font(), 50)

        self.size = self.width, self.height = width, height
        self.screen = pygame.display.set_mode(self.size)

        self.ball = Ball(25, self.RED, Position(self.width/2, self.height/2), Position(7, 7))

        border_bottom = Block(-100, self.height - 10, self.width + 100, 100, self.BLUE, Position(1,-1))
        border_top = Block(-100, -100, self.width + 100, 110, self.BLUE, Position(1,-1))
        border_left = Block(-100, -100, 110, self.height+100, self.GREEN, Position(0, 0))
        border_right = Block(self.width-10, -100, 100, self.height+100, self.RED, Position(0, 0))

        self.walls = pygame.sprite.Group()
        self.walls.add(border_bottom)
        self.walls.add(border_top)
        self.walls.add(border_left)
        self.walls.add(border_right)
        
        self.players = []
        self.players.append(Player(3, "Player 1", self.GREEN, Block(20, (self.height/2-(self.height/9)), 5, (self.height/9), self.GREEN, Position(-1, 1)), pygame.K_w, pygame.K_s))
        self.players.append(Player(3, "Player 2", self.RED, Block((self.width-25), (self.height/2-(self.height/9)), 5, (self.height/9), self.RED, Position(-1, 1)), pygame.K_UP, pygame.K_DOWN))

        self.paddles = pygame.sprite.Group()
        for player in self.players:
            self.paddles.add(player.paddle)
        
        self.allBlocks = pygame.sprite.Group()
        self.allBlocks.add(self.walls)
        self.allBlocks.add(self.paddles)


    def run(self):
        while True:
            self.clock.tick_busy_loop(self.FPS)

            self.handle_events()
            self.handel_game_objects()

            self.draw_screen()


    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        
        pressedKeys = pygame.key.get_pressed()
        for player in self.players:
            if pressedKeys[player.upKey]:
                player.paddle.rect.y -= self.PADDLE_SPEED
            if pressedKeys[player.downKey]:
                player.paddle.rect.y += self.PADDLE_SPEED


    def handel_game_objects(self):
        self.ball.handle_collisions(self.allBlocks)
        self.ball.update()

    def draw_screen(self):
        self.screen.fill(self.BLACK)

        self.draw_fps()
        self.draw_game_objects()

        pygame.display.flip()

    def draw_fps(self):
        fpsRoundedText = str(round(self.clock.get_fps()))
        fpsTextRendered = self.defaultFont.render("FPS: " + fpsRoundedText, True, self.WHITE)

        self.screen.blit(fpsTextRendered, (10,10))

    def draw_game_objects(self):
        self.ball.draw(self.screen)
        self.allBlocks.draw(self.screen)