# Hitbox ( position_x, position_y, width, height)
from enum import Enum

import pyglet
from pyglet import shapes
from pyglet.text import Label

debug_hitbox_batch = pyglet.graphics.Batch()
debug_hitboxs = []


def debug_hitbox_update():
    global debug_hitbox_batch
    debug_hitbox_batch = pyglet.graphics.Batch()
    for debug_hitbox in debug_hitboxs:
        debug_hitbox.debug()


# active_hitboxes: list = []

# add new masks as needed
class HitMask(Enum):
    ALL = 0
    PLAYER = 1
    ENEMY = 2


class Hitbox:
    # X and Y positions
    x = 0
    y = 0

    # Hitbox sizes
    width = 0
    height = 0

    # class initialisation
    def __init__(self, pos_x: int, pos_y: int, width: int, height: int, mask: HitMask = HitMask.ALL):
        self.x = pos_x
        self.y = pos_y
        self.height = height
        self.width = width
        self.mask = mask
        # active_hitboxes.append(self)
        debug_hitboxs.append(self)

    # def __del__(self):
    # if self in active_hitboxes:
    # active_hitboxes.remove(self)

    def set_pos_x(self, x):
        self.x = x

    def set_pos_y(self, y):
        self.y = y

    def set_hitbox_position(self, x, y):
        self.x = x
        self.y = y

    def set_hitbox_size(self, width, height):
        self.width = width
        self.height = height

    def get_hitbox_position(self):
        return self.x, self.y  # returns array of (x, y)

    def get_size_hitbox(self):
        return self.width, self.height  # returns array of (width, height)

    def is_colliding(self, other_hitbox: "Hitbox"):

        if self.mask != other_hitbox.mask and other_hitbox.mask != HitMask.ALL and self.mask != HitMask.ALL:
            return False

        if (self.x < other_hitbox.x + other_hitbox.width) \
                and (self.x + self.width > other_hitbox.x) \
                and (self.y < other_hitbox.y + other_hitbox.height) \
                and (self.height + self.y > other_hitbox.y):
            return True
        else:
            return False

    def debug(self):
        start = (self.x, self.y)
        height = (self.x, self.y + self.height)
        width = (self.x + self.width, self.y)
        end = (self.x + self.width, self.y + self.height)
        #print(f"{start} :: {end}; {width} :: {height}; {self}")

        #self.lable = Label(f"{self}", x=start[0], y=start[1]+10, batch=debug_hitbox_batch)

        self.line1 = shapes.Line(start[0], start[1], width[0], width[1], 1, color=(255, 0, 0), batch=debug_hitbox_batch)
        self.line2 = shapes.Line(start[0], start[1], height[0], height[1], 1, color=(0, 255, 0), batch=debug_hitbox_batch)

        self.line3 = shapes.Line(height[0], height[1], end[0], end[1], 1, color=(0, 0, 255), batch=debug_hitbox_batch)
        self.line4 = shapes.Line(width[0], width[1], end[0], end[1], 1, color=(0, 0, 255), batch=debug_hitbox_batch)

        self.rec1 = shapes.Rectangle(start[0], start[1], 5, 5, color=(255, 255, 0), batch=debug_hitbox_batch)
        self.rec2 = shapes.Rectangle(end[0]-5, end[1]-5, 5, 5, color=(0, 0, 255), batch=debug_hitbox_batch)