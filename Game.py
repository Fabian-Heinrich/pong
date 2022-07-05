import random
import sys
import pygame

from Ball import Ball
from Color import Color
from GameScene import GameScene
from Paddle import Paddle
from Player import Player
from Position import Position
from Block import Block

class Game:
    def __init__(self, width, height, FPS) -> None:
        pygame.init()

        self.FPS = FPS
        self.running = True
        self.defaultBallSpeed = 600
        self.gameScene = GameScene.play

        self.clock = pygame.time.Clock()
        self.defaultFont = pygame.font.SysFont(pygame.font.get_default_font(), 50)

        self.collisionSound = pygame.mixer.Sound("sounds/ping-pong-ball-hit.wav")

        self.size = self.width, self.height = width, height
        self.screen = pygame.display.set_mode(self.size)
        self.center = Position(self.width/2, self.height/2)

        self.ball = Ball(25, Color.RED, self.center, Position(self.defaultBallSpeed , self.defaultBallSpeed))

        wall_bottom = Block(-100, self.height - 10, self.width + 100, 100, Color.BLUE, Position(1,-1))
        wall_top = Block(-100, -100, self.width + 100, 110, Color.BLUE, Position(1,-1))
        wall_left = Block(-100, -100, 110, self.height+100, Color.GREEN, Position(0, 0))
        wall_right = Block(self.width-10, -100, 100, self.height+100, Color.RED, Position(0, 0))

        self.walls = pygame.sprite.Group()
        self.walls.add(wall_bottom)
        self.walls.add(wall_top)
        self.walls.add(wall_left)
        self.walls.add(wall_right)
        
        self.players = []
        self.players.append(Player(3, "Player 1", Color.GREEN, Paddle(20, (self.height/2-(self.height/7)), 5, (self.height/7), Color.GREEN, Position(-1, 1)), pygame.K_w, pygame.K_s, wall_left))
        self.players.append(Player(3, "Player 2", Color.RED, Paddle((self.width-25), (self.height/2-(self.height/7)), 5, (self.height/7), Color.RED, Position(-1, 1)), pygame.K_UP, pygame.K_DOWN, wall_right))

        self.paddles = pygame.sprite.Group()
        for player in self.players:
            self.paddles.add(player.paddle)
        
        self.allBlocks = pygame.sprite.Group()
        self.allBlocks.add(self.walls)
        self.allBlocks.add(self.paddles)

        self.gameSprites = pygame.sprite.Group()
        self.gameSprites.add(self.allBlocks)
        self.gameSprites.add(self.ball)


    def run(self):
        while self.running:
            dt = self.clock.tick(self.FPS)/1000

            if self.gameScene == GameScene.play:
                self.handle_events()
                self.handel_game_objects(dt)
                self.draw_play_screen()

            if self.gameScene == GameScene.end:
                self.handle_events()
                self.draw_game_over_screen()

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

        pressedKeys = pygame.key.get_pressed()

        if pressedKeys[pygame.K_ESCAPE]:
            self.reset_ball()

        for player in self.players:
            if pressedKeys[player.upKey] and player.paddle.rect.y >= 0:
                player.paddle.move_up()
            if pressedKeys[player.downKey] and player.paddle.rect.y <= (self.height-player.paddle.rect.height):
                player.paddle.move_down()
            if not pressedKeys[player.upKey] and not pressedKeys[player.downKey]:
                player.paddle.movementsInARow = 0

    def handel_game_objects(self, dt):

        self.check_ball_collision(dt)
        self.gameSprites.update(dt)

    def draw_play_screen(self):
        self.screen.fill(Color.BLACK)

        self.draw_fps_text()
        self.draw_players_hp_text()
        self.draw_game_objects()

        pygame.display.update()
    
    def draw_game_over_screen(self):
        self.screen.fill(Color.BLACK)

        self.draw_players_hp_text()
        self.draw_game_over_text()

        pygame.display.update()

    def draw_fps_text(self):
        fpsRoundedText = "FPS: " + str(round(self.clock.get_fps()))
        fpsTextRendered = self.defaultFont.render(fpsRoundedText, True, Color.WHITE)

        self.screen.blit(fpsTextRendered, (10,10))

    def draw_players_hp_text(self):
        for i in range (0, len(self.players)):
            player = self.players[i]
            playerHpText = player.name + ": " + str(player.healthpoints)
            playerHpTextRendered = self.defaultFont.render(playerHpText, True, Color.WHITE)

            self.screen.blit(playerHpTextRendered, (self.width/2-playerHpTextRendered.get_width()/2, 10+(playerHpTextRendered.get_height()*i+5)))
    
    def draw_game_over_text(self):
        gameOverTextRendered = self.defaultFont.render("Game over", True, Color.WHITE)

        self.screen.blit(gameOverTextRendered, (self.width/2-gameOverTextRendered.get_width()/2, self.height/2-gameOverTextRendered.get_height()/2))

    def draw_game_objects(self):
        self.ball.draw(self.screen)
        self.allBlocks.draw(self.screen)

    def reset_ball(self):
        self.ball.rect.center = self.center.get_pos()
        self.ball.direction = Position(random.choice([self.defaultBallSpeed , -self.defaultBallSpeed ]), random.choice([self.defaultBallSpeed , -self.defaultBallSpeed ]))


    def check_ball_collision(self, dt):
        for block in self.allBlocks:
            if pygame.sprite.collide_mask(self.ball, block):
                self.ball.direction *= block.directionChangeOnCollision
                self.ball.update(dt)
                self.collisionSound.play()

                for player in self.players:
                    if block == player.wall:
                        self.reset_ball()
                        if player.lose_hp() == 0:
                            self.gameScene = GameScene.end