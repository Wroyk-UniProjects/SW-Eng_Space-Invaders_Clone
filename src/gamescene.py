from abc import ABC, abstractmethod

import pyglet


class GameScene(ABC):
    batch = None
    game_object = []

    width: int = 0
    height: int = 0

    def __init__(self, width, height):
        self.batch = pyglet.graphics.Batch()

    @abstractmethod
    def setup(self):
        pass

    @abstractmethod
    def update(self, dt):
        pass

    @abstractmethod
    def on_key_press(self, symbol, modifiers):
        pass

    @abstractmethod
    def on_key_release(self, symbol, modifiers):
        pass

    @abstractmethod
    def on_mouse_press(self, x, y, button, modifiers):
        pass