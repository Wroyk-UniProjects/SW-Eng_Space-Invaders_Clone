import pyglet

from gameobject import GameObject
import hitbox


distanceMoveInFront = 10
speedIncrementMovinginFront = 10

class Enemy(GameObject):

    #Constructor
    def __init__(self, x, y, startSpeed, image, positionInMesh):

        #Location
        self.x = x
        self.y = y

        #EnemySpeed at the start
        self.speed = startSpeed

        #Sprite setup
        image = pyglet.image.load(image)
        self.sprite = pyglet.sprite.Sprite(image, x=self.x, y=self.y)
        self.sprite.update(scale_x=0.05, scale_y=0.05)

        #Size of enemy
        self.enemyWidth = self.sprite.width
        self.enemyHeight = self.sprite.height
        self.direction = False

        #We need this Parameter, to synchronise the movement of multiple Enemies in a Mesh
        self.positionInMesh = positionInMesh

        self.rightBoorder = self.enemyWidth * 10 - self.enemyWidth + self.enemyWidth * self.positionInMesh
        self.leftBoorder =  40 + self.enemyWidth * self.positionInMesh

        #is the Enemy alive?
        self.active = True

        #create hitbox for the enemy
        self.hitbox = hitbox.Hitbox(self.x, self.y, self.enemyWidth, self.enemyHeight)


    def getEnemySpeed(self):
        return self.speed

    def getSprite(self):
        return self.sprite

    def getEnemyX(self):
        return self.x

    def getEnemyY(self):
        return self.y

    def update(self,dt):
        if(self.active):
            if(self.direction):
                self.x += self.speed * dt
                self.sprite.update(x=self.x)
                if(self.x >= self.rightBoorder):
                    self.direction = False
                    self.y = self.y - distanceMoveInFront
                    self.speed = self.speed + speedIncrementMovinginFront
                    self.sprite.update(y=self.y - distanceMoveInFront)
            else:
                self.x -= self.speed * dt
                self.sprite.update(x=self.x)
                if (self.x <= self.leftBoorder):
                    self.direction = True
                    self.y = self.y - distanceMoveInFront
                    self.speed = self.speed + speedIncrementMovinginFront
                    self.sprite.update(y=self.y - distanceMoveInFront)

                if(self.y <= 200):
                    self.enemyDie()

    def draw(self):
        if(self.active):
            self.sprite.draw()

    #deleting all the attributes. There is no way for an object to delete itslelf
    def enemyDie(self):
        self.active = False
        del self.sprite
        del self.enemyHeight
        del self.enemyWidth
        del self.speed
        del self.x
        del self.y
        del self.positionInMesh
        del self.rightBoorder
        del self.leftBoorder

    def on_collision(self):
        self.enemyDie()

#Mesh creates multiple Enemies
#maybe make them smaller?!

class EnemyMesh:


    # Three rows of Enemies right now. Enemies are still a bit big but i will channge them
    # Movement still not working right.
    def __init__(self, enemyCount):

        #get enemie height and width
        pseudoEnemie = Enemy(0, 0, 0, '../assets/enemy_updated.png', 0)
        enemieWidth = pseudoEnemie.sprite.width
        enemieHeight = pseudoEnemie.sprite.height
        hitbox.debug_hitboxs.remove(pseudoEnemie.hitbox)
        del pseudoEnemie



        self.enemies = []
        for i in range(enemyCount):
            self.enemies.append(Enemy(i * enemieWidth + 200, 620, 50, '../assets/enemy_updated.png', i))
            self.enemies.append(Enemy(i * enemieWidth + 200, 620 - enemieHeight, 50, '../assets/enemy_updated.png', i))
            self.enemies.append(Enemy(i * enemieWidth + 200, 620 - enemieHeight * 2, 50, '../assets/enemy_updated.png', i))

    def getEnemyMesh(self):
        return self.enemies

    def update(self, dt):
        for enemy in self.enemies:
            enemy.update(dt)
