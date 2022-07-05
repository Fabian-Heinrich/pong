import pygame
from Color import Color
from Scenes.Scene import Scene
from Scenes.Scenes import Scenes

class Start(Scene):
    def __init__(self, screen) -> None:
        super().__init__(screen)
        self.nextScene = Scenes.START

        self.defaultFont = pygame.font.SysFont(pygame.font.get_default_font(), 50)

    def handle_events(self, events, pressedKeys):
        if pressedKeys[pygame.K_SPACE] or pressedKeys[pygame.K_KP_ENTER] or pressedKeys[pygame.K_RETURN]:
            self.switch_scene(Scenes.PLAY)

    def render(self):
        self.screen.fill(Color.BLACK)

        self.draw_start_text()

    def draw_start_text(self):
        startTextRendered = self.defaultFont.render("Press ENTER to start", True, Color.WHITE)

        self.screen.blit(startTextRendered, (self.width/2-startTextRendered.get_width()/2, self.height/2-startTextRendered.get_height()/2))



