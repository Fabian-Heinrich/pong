class Scene:

    def __init__(self) -> None:
        self.next_scene = self
    
    def handle_events(self, events, keys_pressed):
        pass

    def update(self, dt):
        pass

    def render(self):
        pass

    def switch_scene(self, scene):
        self.next_scene = scene
    
    def terminate(self):
        self.next_scene = None