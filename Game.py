import sys
import pygame

from Ball import Ball
from Position import Position
from Wall import Wall


class Game:

    WHITE = pygame.Color(255,255,255)
    BLACK = pygame.Color(0,0,0)
    RED = pygame.Color(255,0,0)
    GREEN = pygame.Color(0,255,0)
    BLUE = pygame.Color(0,0,255)

    def __init__(self, width, height, FPS) -> None:
        pygame.init()

        self.FPS = FPS

        self.clock = pygame.time.Clock()
        self.defaultFont = pygame.font.SysFont(pygame.font.get_default_font(), 50)

        self.size = self.width, self.height = width, height
        self.screen = pygame.display.set_mode(self.size)
        self.ball = Ball(25, self.RED, Position(self.width/2, self.height/2), Position(5, 5))

        self.border_bottom = Wall(-100, self.height - 10, self.width + 100, 100, self.BLUE)
        self.border_top = Wall(-100, -100, self.width + 100, 110, self.RED)
        self.border_left = Wall(-100, -100, 110, self.height+100, self.GREEN)
        self.border_right = Wall(self.width-10, -100, 100, self.height+100, self.WHITE)

        self.walls = pygame.sprite.Group()
        self.walls.add(self.border_bottom)
        self.walls.add(self.border_top)
        self.walls.add(self.border_left)
        self.walls.add(self.border_right)



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

    def handel_game_objects(self):
        self.ball.handle_collisions(self.border_bottom, self.border_top, self.border_left, self.border_right)
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
        self.walls.draw(self.screen)