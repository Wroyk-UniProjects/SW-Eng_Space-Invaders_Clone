import pyglet

from gameobject import GameObject


class Enemy(GameObject):

    def __init__(self, x, y, speed, image):

        self.x = x
        self.y = y

        self.speed = speed
        image = pyglet.image.load(image)
        self.sprite = pyglet.sprite.Sprite(image, x=50, y=50)

    def getEnemySpeed(self):
        return self.speed

    def getEnemyX(self):
        return self.x

    def getEnemyY(self):
        return self.y

    def getEnemyImage(self):
        return self.image

    def update(self,dt):
        print("todo")

    def spawnEnemy(self):
        print('spawn')

    def draw(self):
        self.sprite.draw()

    def despawnEnemie(self):
        print("todo")