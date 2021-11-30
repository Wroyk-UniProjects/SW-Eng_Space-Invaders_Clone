from hitbox import Hitbox


class Projectiles(Hitbox):
    direction = 0   # 10 is up, -10 is down. Could be implemented differently...

    # Spawn with coordinates, direction(up for player, down for enemy) and hitbox
    def spawn(self, x, y, size, direc):
        self.__init__(x, y, size)
        self.start_moving(direc)

    def start_moving(self, direc):
        self.direction = direc
        while True:
            self.set_hitbox_position(self.pos_x, self.pos_y + self.direction)
            if self.is_touching():
                self.__del__()
                # Also delete hit object
