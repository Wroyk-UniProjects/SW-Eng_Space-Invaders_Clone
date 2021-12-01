from hitbox import Hitbox
from gameobject import GameObject


def spawn(x, y, length, width, velo):
    return Projectiles(x, y, length, width, velo)


class Projectiles(GameObject, Hitbox):
    velocity = 0

    def __init__(self, x, y, length, width, velo):
        super(Projectiles, self).__init__(x, y, length, width)
        self.sprite = None
        self.velocity = velo

    def draw(self):
        self.sprite.draw()

    def update(self, dt):
        self.set_hitbox_position(self.pos_x, self.pos_y + self.velocity * dt)
        if self.is_touching(other_obj="hitbox"):
            # self.__del__()
            pass
