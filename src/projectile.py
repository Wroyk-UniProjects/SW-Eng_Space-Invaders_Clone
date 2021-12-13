from enum import Enum

import pyglet.resource
from pyglet.sprite import Sprite

from hitbox import Hitbox, HitMask
from gameobject import GameObject, PROJECTILES

active_projectiles = []


class Direction(Enum):
    UP = 1
    DOWN = -1


def spawn(x, y, mask: HitMask, direction: Direction, batch, velocity: float = 100, image: str = "player_projectile.png"):
    active_projectiles.append(Projectile(x, y, batch, mask, direction, velocity, image))


class Projectile(GameObject, Hitbox):

    def __init__(self, x, y, batch, mask: HitMask = HitMask.ALL, direction: Direction = Direction.UP,
                 velocity: float = 100, image: str = "player_projectile.png"):
        self.x = x
        self.y = y

        imag = pyglet.resource.image(image)
        self.sprite = Sprite(imag, x, y, group=PROJECTILES, batch=batch)
        self.sprite.update(scale=0.02)
        self.width = self.sprite.width
        self.height = self.sprite.height

        self.mask = mask
        self.direction = direction
        if self.direction == Direction.DOWN:
            self.sprite.rotation(180)
            self.sprite.x -= self.width
            self.sprite.y -= self.height

        self.velocity = velocity

    def update(self, dt):
        self.x = self.velocity * dt
        if self.direction == Direction.DOWN:
            self.sprite.x += self.x - self.width
        else:
            self.sprite.x = self.x

    def on_collision(self):
        active_projectiles.remove(self)
        del self.sprite
