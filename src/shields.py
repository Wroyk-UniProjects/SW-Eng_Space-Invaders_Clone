import pyglet
import gameobject
import projectile
from gameobject import GameObject
import hitbox

class shield(GameObject):

    def __init__(self, positionX, positionY, lives, batch):

        self.active = True
        self.batch = batch

        self.positionX = positionX
        self.positionY = positionY
        self.lives = lives

        shieldImage1 = pyglet.image.load('../assets/Shield1.png')


        self.sprite = pyglet.sprite.Sprite(shieldImage1, x=self.positionX, y=self.positionY, group=gameobject.GAMEOBJECTS, batch=self.batch)
        self.sprite.update(scale_x=0.1, scale_y=0.1)

        self.shieldWidth = self.sprite.width
        self.shieldHeight = self.sprite.height


        self.hitbox = hitbox.Hitbox(self.positionX, self.positionY, self.shieldWidth, self.shieldHeight, hitbox.HitMask.ALL)

    def update(self, dt):
        if self.active == True:
            self.sprite.update()
            #print(self.lives)

    def on_collision(self):

        self.lives -= 1

        if (self.lives == 3):
            shieldImage2 = pyglet.image.load('../assets/Shield2.png')
            self.sprite = pyglet.sprite.Sprite(shieldImage2, x=self.positionX, y=self.positionY, group=gameobject.GAMEOBJECTS, batch=self.batch)
            self.sprite.update(scale_x=0.1, scale_y=0.1)

        elif (self.lives == 2):

            shieldImage3 = pyglet.image.load('../assets/Shield3.png')
            self.sprite = pyglet.sprite.Sprite(shieldImage3, x=self.positionX, y=self.positionY, group=gameobject.GAMEOBJECTS, batch=self.batch)
            self.sprite.update(scale_x=0.1, scale_y=0.1)

        elif (self.lives == 1):

            shieldImage4 = pyglet.image.load('../assets/Shield4.png')
            self.sprite = pyglet.sprite.Sprite(shieldImage4, x=self.positionX, y=self.positionY, group=gameobject.GAMEOBJECTS, batch=self.batch)
            self.sprite.update(scale_x=0.1, scale_y=0.1)
        elif(self.lives == 0):
            self.active = False
            self.shield_destroyed()


    def shield_destroyed(self):
        hitbox.debug_hitboxs.remove(self.hitbox)
        del self.sprite
        del self.hitbox


class shieldFactory(GameObject):

    def __init__(self, batch):

        self.shields = []

        self.shields.append(shield(200, 200, 4,batch))
        self.shields.append(shield(400,200, 4, batch))
        self.shields.append(shield(600, 200, 4, batch))
        self.shields.append(shield(800, 200, 4, batch))
        self.shields.append(shield(1000, 200, 4, batch))



    def getShields(self):
        return self.shields

    def update(self, dt):
        for shield in self.shields:
            shield.update()