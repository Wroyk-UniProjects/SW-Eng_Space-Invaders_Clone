class Player:
    def __init__(self, hitbox, startx, starty, projectile, icon):
        self.hitbox = hitbox
        self.startx = startx
        self.starty = starty
        self.projectile = projectile
        self.icon = icon

    #movement functions
    def moveright(self):
        self.startx += 1

    def moveleft(self):
        self.startx -= 1

    #shooting
    def shootprojectile(self):
        #do something
        self.projectile