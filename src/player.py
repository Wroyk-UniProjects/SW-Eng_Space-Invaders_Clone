import pyglet
from pyglet.sprite import Sprite
from pyglet.window import key

import gamestate
import hitbox
import projectile
from gameobject import GameObject, GAMEOBJECTS
from hitbox import Hitbox, HitMask

import time
from pyglet.text import Label
from gameobject import UI


class Player(GameObject):

    def __init__(self, startx, starty, icon, batch):
        self.startx = startx
        self.starty = starty
        self.icon = icon
        self.velocity = 0
        self.num_of_lives = 3
        self.batch = batch

        self.last_shot = 0

        image = pyglet.image.load(self.icon)
        self.sprite = Sprite(image, x=self.startx, y=self.starty, group=GAMEOBJECTS, batch=batch)
        self.sprite.update(scale_x=.75, scale_y=.75)

        self.hitbox = Hitbox(self.startx, self.starty, self.sprite.width, self.sprite.height, HitMask.PLAYER)

        self.active = True

        self.lives_left_label = Label('Lives left: ' + str(self.num_of_lives), font_name='monogramextended', font_size= 20, x=10, y=700, batch=self.batch,
                                      group=UI)

    # movement functions
    def moveright(self):
        self.velocity = 400

    def moveleft(self):
        self.velocity = -400

    # shooting
    def shootprojectile(self):
        if self.active:
            projectile.spawn(self.startx + self.sprite.width/2 - 10, self.starty + 10, HitMask.ENEMY, projectile.Direction.UP, self.batch)

    def on_key_press(self, symbol, modifiers):
        if symbol is key.D or symbol is key.RIGHT:
            self.moveright()
        elif symbol is key.A or symbol is key.LEFT:
            self.moveleft()

    def on_key_release(self, symbol, modifier):
        if symbol is key.D or symbol is key.RIGHT:
            self.velocity = 0
        elif symbol is key.A or symbol is key.LEFT:
            self.velocity = 0
        elif symbol is key.SPACE:
            if (time.time() - self.last_shot) > 2:
                self.last_shot = time.time()
                self.shootprojectile()

    def on_collision(self):
        self.num_of_lives -= 1
        if self.num_of_lives < 1:
            hitbox.debug_hitboxs.remove(self.hitbox)
            self.active = False
            gamestate.set_game_lost()
            del self.sprite
            del self.hitbox

    def update(self, dt):
        if self.active:
            self.startx += self.velocity * dt
            if self.startx <= -self.sprite.width:
                self.startx = 1280 - self.sprite.width
            elif self.startx >= 1280:
                self.startx = 0
            self.sprite.x = self.startx
            self.hitbox.x = self.startx

        self.lives_left_label.text = 'Lives left: ' + str(self.num_of_lives)