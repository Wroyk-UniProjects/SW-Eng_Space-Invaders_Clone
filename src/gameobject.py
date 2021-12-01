from abc import ABC, abstractmethod
from enum import Enum

import pyglet

# TODO find better solution
# https://pyglet.readthedocs.io/en/latest/programming_guide/graphics.html#batches-and-groups-in-other-modules

BACKGROUND = pyglet.graphics.OrderedGroup(0)
GAMEOBJECTS = pyglet.graphics.OrderedGroup(1)
UI = pyglet.graphics.OrderedGroup(2)


class GameObject(ABC):
    @abstractmethod
    def update(self, dt):
        pass

    def draw(self):
        pass

    def __init__(self, batch):
        self.batch = batch

