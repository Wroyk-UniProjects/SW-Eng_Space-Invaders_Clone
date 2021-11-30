from abc import ABC, abstractmethod
from enum import Enum

import pyglet

# TODO find better solution
# https://pyglet.readthedocs.io/en/latest/programming_guide/graphics.html#batches-and-groups-in-other-modules

BACKGROUND = pyglet.graphics.OrderedGroup(2)
GAMEOBJECTS = pyglet.graphics.OrderedGroup(1)
UI = pyglet.graphics.OrderedGroup(0)


class GameObject(ABC):
    @abstractmethod
    def update(self, dt):
        pass

    @abstractmethod
    def draw(self):
        pass
