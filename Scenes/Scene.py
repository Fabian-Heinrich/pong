import pygame
from Position import Position


class Scene:

    def __init__(self, screen: pygame.surface.Surface) -> None:
        self.nextScene = self
        self.screen = screen

        self.width = screen.get_width()
        self.height = screen.get_height()
        self.center = Position(self.screen.get_width()/2, self.screen.get_height()/2)
    
    def handle_events(self, events, pressedKeys):
        pass

    def update(self, dt):
        pass

    def render(self):
        pass

    def switch_scene(self, scene: int):
        self.nextScene = scene
    
    def terminate(self):
        self.nextScene = None