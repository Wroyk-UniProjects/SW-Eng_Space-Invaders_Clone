import pyglet

from gameobject import GameObject


class Enemy(GameObject):

    def __init__(self, x, y, speed, image):

        self.x = x
        self.y = y

        self.speed = speed
        image = pyglet.image.load(image)
        self.sprite = pyglet.sprite.Sprite(image, x=self.x, y=self.y)
        self.sprite.update(scale_x=0.1, scale_y=0.1)
        self.direction = False

    def getEnemySpeed(self):
        return self.speed

    def getEnemyX(self):
        return self.x

    def getEnemyY(self):
        return self.y

    def getEnemyImage(self):
        return self.image

    def update(self,dt):


        if(self.direction):
            self.x += self.speed * dt
            self.sprite.update(x=self.x)
            print(self.direction)
            if(self.x >= 1000):
                self.direction = False
        else:
            self.x -= self.speed * dt
            self.sprite.update(x=self.x)
            print(self.direction)
            if (self.x <= 100):
                self.direction = True

    def spawnEnemy(self):
        print('spawn')

    def draw(self):
        self.sprite.draw()

    def despawnEnemie(self):
        print("todo")