import numpy as np
import math


class Hitbox:
    # X and Y positions
    pos_x = 0
    pos_y = 0

    # it's a zero square.
    size = 0

    # class initialisation
    def __init__(self, pos_x, pos_y, size):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.size = size

    def set_pos_x(self, posx):
        self.pos_x = posx

    def set_pos_y(self, posy):
        self.pos_y = posy

    def set_hitbox_position(self, posx, posy):
        self.pos_x = posx
        self.pos_y = posy

    def get_hitbox_position(self):
        return self.pos_x, self.pos_y

    def set_hitbox_size(self, size):
        self.size = size

    def get_size_hitbox(self):
        return self.size

    # almost works, still buggy though
    def is_touching(self, other_obj: "hitbox"):
        # this is a comparison between a vector normalization and the sum of objects sizes
        if np.linalg.norm(np.array([self.pos_x, self.pos_y]) - np.array([other_obj.pos_x, other_obj.pos_y])) <= (
                self.size + other_obj.size):
            return True
        else:
            return False

##################################################################################################

    def magnitude(self, v):
        return math.sqrt(sum(v[i] * v[i] for i in range(len(v))))

    def add(self, u, v):
        return [u[i] + v[i] for i in range(len(u))]

    def sub(self, u, v):
        return [u[i] - v[i] for i in range(len(u))]

    def normalize(self, v):
        return [v[i] / self.magnitude(v) for i in range(len(v))]

    def check_collide(self, other_obj: "hitbox"):
        vec_h1 = np.array([self.pos_x, self.pos_y])
        vec_h2 = np.array([other_obj.pos_x, other_obj.pos_y])
        print(vec_h1)
        print(vec_h2)

        print("\n")

        print(np.array([self.pos_x, self.pos_y]) - np.array([other_obj.pos_x, other_obj.pos_y]))
        print(str(round(np.linalg.norm(np.array([self.pos_x, self.pos_y]) - np.array([other_obj.pos_x, other_obj.pos_y])),0)))
        print(self.size + other_obj.size)

        if round(np.linalg.norm(np.array([self.pos_x, self.pos_y]) - np.array([other_obj.pos_x, other_obj.pos_y])),0) < (
                self.size + other_obj.size):
            print("true")
        else:
            print("false")

        #norm = self.normalize(vec_h1,vec_h2)

        #print("Normalization: " + str(norm))