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
