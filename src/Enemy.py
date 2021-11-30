import pyglet

from gameobject import GameObject


class Enemy(GameObject):

    def __init__(self, x, y, speed, image):

        self.x = x
        self.y = y

        self.speed = speed
        image = pyglet.image.load(image)
        self.sprite = pyglet.sprite.Sprite(image, x=self.x, y=self.y)
        self.sprite.update(scale_x=0.075, scale_y=0.075)
        self.enemyWidth = self.sprite.width
        self.direction = False
        print(self.enemyWidth)

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
            if(self.x >= 1280/20*19-self.enemyWidth):
                self.direction = False
        else:
            self.x -= self.speed * dt
            self.sprite.update(x=self.x)
            if (self.x <= 1280/20):
                self.direction = True

    def spawnEnemy(self):
        print('spawn')

    def draw(self):
        self.sprite.draw()

    def despawnEnemie(self):
        print("todo")

#Mesh creates multiple Enemies
#Todo: get them to move together
#maybe make them smaller?!

class EnemyMesh:

    def __init__(self, enemyCount):
        self.enemies = []
        for i in range(enemyCount):
            self.enemies.append(Enemy(i*100+200, 600, 150, '../assets/Enemy.jpeg'))

    def getEnemyMesh(self):
        return self.enemies

    def update(self,dt):
        for Enemy in self.enemies:
            Enemy.update(dt)
