from abc import ABC, abstractmethod
from enum import Enum

import pyglet

BACKGROUND = pyglet.graphics.OrderedGroup(0)
GAMEOBJECTS = pyglet.graphics.OrderedGroup(1)
PROJECTILES = pyglet.graphics.OrderedGroup(2)
UI = pyglet.graphics.OrderedGroup(3)

game_objects = []

class GameObject(ABC):
    @abstractmethod
    def update(self, dt):
        pass

    def __init__(self, batch):
        self.batch = batch
        #game_objects.append(self)
