import pyglet
from pyglet.sprite import Sprite

from Projectiles import Projectiles
from gameobject import GameObject
from hitbox import Hitbox


class Player (GameObject):
    def __init__(self, startx, starty, icon):
        self.startx = startx
        self.starty = starty
        self.icon = icon

        self.hitbox = Hitbox(self.startx, self.starty, 100, 100)
        self.projectile = Projectiles(self.startx, self.starty, 100, 100, 20)

        image = pyglet.image.load(self.icon)
        self.sprite = Sprite(image, x=100, y=102)
        self.sprite.update(scale_x=.75, scale_y=.75)

    #movement functions
    def moveright(self):
        self.startx += 1

    def moveleft(self):
        self.startx -= 1

    #shooting
    def shootprojectile(self):
        #do something
        self.projectile.spawn()

    #from gameobject
    def draw(self):
        self.sprite.draw()

    def update(self, dt):
        pass
