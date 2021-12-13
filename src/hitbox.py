# Hitbox ( position_x, position_y, width, height)
from enum import Enum


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
