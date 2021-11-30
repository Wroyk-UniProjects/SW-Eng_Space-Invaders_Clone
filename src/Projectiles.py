from hitbox import Hitbox
from gameobject import GameObject

def spawn(x, y, length, width, velo):
    return Projectiles(x, y, length, width, velo)

class Projectiles(GameObject, Hitbox):
    velocity = 0

    def __init__(self, x, y, length, width, velo):
        super(Projectiles, self).__init__(x, y, length, width)
        self.start_moving(velo)

    def start_moving(self, velo):
        self.velocity = velo
        while True:
            self.set_hitbox_position(self.pos_x, self.pos_y + self.velocity)
            if self.is_touching():
                self.__del__()
                # Also delete hit object

    def draw(self):
        pass

    def update(self, dt):
        pass
