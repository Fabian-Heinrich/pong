import pygame
from Color import Color
from Scenes.Scene import Scene
from Scenes.Scenes import Scenes

class End(Scene):
    def __init__(self, screen) -> None:
        super().__init__(screen)
        self.nextScene = Scenes.END

        self.defaultFont = pygame.font.SysFont(pygame.font.get_default_font(), 50)

    def handle_events(self, events, pressedKeys):
        if pressedKeys[pygame.K_SPACE] or pressedKeys[pygame.K_KP_ENTER] or pressedKeys[pygame.K_RETURN]:
            self.switch_scene(Scenes.PLAY)

    def render(self):
        self.screen.fill(Color.BLACK)
        self.draw_game_over_text()

    def draw_game_over_text(self):
        gameOverText = self.defaultFont.render("Game over", True, Color.WHITE)
        playAgainText = self.defaultFont.render("Press ENTER or SPACE to play again", True, Color.WHITE)
        self.screen.blit(gameOverText, (self.width/2-gameOverText.get_width()/2, self.height/2-gameOverText.get_height()/2))
        self.screen.blit(playAgainText, (self.width/2-playAgainText.get_width()/2, self.height/2-gameOverText.get_height()/2 + gameOverText.get_height() + 5))


