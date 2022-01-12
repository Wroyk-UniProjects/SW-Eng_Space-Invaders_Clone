import pyglet
import gameobject
import projectile
from gameobject import GameObject
import hitbox

class shield(GameObject):

    def __init__(self, positionX, positionY, lives, batch):

        self.batch = batch

        self.positionX = positionX
        self.positionY = positionY
        self.lives = lives

        image = pyglet.image.load('../assets/shield.png')
        self.sprite = pyglet.sprite.Sprite(image, x=self.positionX, y=self.positionY, group=gameobject.GAMEOBJECTS, batch=self.batch)
        self.sprite.update(scale_x=0.1, scale_y=0.1)

        self.shieldWidth = self.sprite.width
        self.shieldHeight = self.sprite.height


        self.hitbox = hitbox.Hitbox(self.positionX, self.positionY, self.shieldWidth, self.shieldHeight, hitbox.HitMask.ENEMY)

    def update(self, dt):
        self.sprite.update()

class shieldFactory(GameObject):

    def __init__(self, batch):

        self.shields = []

        self.shields.append(shield(400,200, 2, batch))
        self.shields.append(shield(600, 200, 2, batch))
        self.shields.append(shield(800, 200, 2, batch))
        self.shields.append(shield(1000, 200, 2, batch))



    def getShields(self):
        return self.shields

    def update(self, dt):
        for shield in self.shields:
            shield.update()