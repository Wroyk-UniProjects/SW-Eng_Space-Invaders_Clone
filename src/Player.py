import pyglet
from pyglet.sprite import Sprite
from pyglet.window import key

from Projectiles import Projectiles
from gameobject import GameObject
from hitbox import Hitbox


class Player (GameObject):
    def __init__(self, startx, starty, icon):
        self.startx = startx
        self.starty = starty
        self.icon = icon
        self.velocity = 0

        self.hitbox = Hitbox(self.startx, self.starty, 100, 100)
        self.projectile = Projectiles(self.startx, self.starty, 100, 100, 20)

        image = pyglet.image.load(self.icon)
        self.sprite = Sprite(image, x=100, y=102)
        self.sprite.update(scale_x=.75, scale_y=.75)

    #movement functions
    def moveright(self):
        self.velocity = 400

    def moveleft(self):
        self.velocity = -400

    # shooting
    def shootprojectile(self):
        self.projectile.spawn()

    def on_key_press(self, symbol, modifiers):
        if symbol is key.D or symbol is key.RIGHT:
            self.moveright()
        elif symbol is key.A or symbol is key.LEFT:
            self.moveleft()
        elif symbol is key.SPACE:
            self.shootprojectile()

    def on_key_release(self, symbol, modifier):
        if symbol is key.D or symbol is key.RIGHT:
            self.velocity = 0
        elif symbol is key.A or symbol is key.LEFT:
            self.velocity = 0


    #from gameobject
    def draw(self):
        self.sprite.draw()

    def update(self, dt):
        self.startx += self.velocity*dt
        if self.startx <= -self.sprite.width:
            self.startx = 1280-self.sprite.width
        elif self.startx >= 1280:
            self.startx = 0
        self.sprite.x = self.startx


