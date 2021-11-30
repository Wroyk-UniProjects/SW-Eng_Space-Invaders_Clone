from hitbox import Hitbox
from gameobject import GameObject

def spawn(x, y, length, width, direc):
    return Projectiles(x, y, length, width, direc)

class Projectiles(GameObject, Hitbox):
    direction = 0   # 10 is up, -10 is down. Could be implemented differently...

    # Spawn with coordinates, direction(up for player, down for enemy) and hitbox
    def __init__(self, x, y, length, width, direc):
        super(Projectiles, self).__init__(x, y, length, width)
        self.start_moving(direc)

    def start_moving(self, direc):
        self.direction = direc
        while True:
            self.set_hitbox_position(self.pos_x, self.pos_y + self.direction)
            if self.is_touching():
                self.__del__()
                # Also delete hit object

    def draw(self):
        pass

    def update(self, dt):
        pass
