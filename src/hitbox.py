
# Hitbox ( position_x, position_y, width, length )
class Hitbox:
    # X and Y positions
    pos_x = 0
    pos_y = 0

    # Hitbox sizes
    width = 0
    length = 0

    # class initialisation
    def __init__(self, pos_x, pos_y, l, w):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.length = l
        self.width = w

    def set_pos_x(self, x):
        self.pos_x = x

    def set_pos_y(self, y):
        self.pos_y = y

    def set_hitbox_position(self, x, y):
        self.pos_x = x
        self.pos_y = y

    def set_hitbox_size(self, length, width):
        self.width = width
        self.length = length

    def get_hitbox_position(self):
        return self.pos_x, self.pos_y  # returns array of (x, y)

    def get_size_hitbox(self):
        return self.width, self.length  # returns array of (width, length)

    def is_touching(self, other_obj: "hitbox"):
        if (self.pos_x < other_obj.pos_x + other_obj.width) and (self.pos_x + self.width > other_obj.pos_x) and (self.pos_y < other_obj.pos_y + other_obj.length) and (self.length + self.pos_y > other_obj.pos_y):
            return True
        else:
            return False
