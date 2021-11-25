class Hitbox:
    pos_x = 0
    pos_y = 0
    x_width = 25
    y_height = 25

    def set_pos_x(self, posx):
        self.pos_x = posx

    def set_pos_y(self, posy):
        self.pos_y = posy

    def set_position(self, posx, posy):
        self.pos_x = posx
        self.pos_y = posy

    def get_position(self):
        return self.pos_x,self.pos_y

    def set_size_hitbox(self, length, height):
        self.x_width = length
        self.y_height = height

    def get_size_hitbox(self):
        return self.x_width,self.y_height

    # not functional yet
    def detect_collision(self, other_obj: "Hitbox"):
        if self.pos_x == other_obj.pos_x and self.pos_y == other_obj.pos_x:
            print("collision detected!")
        elif self.pos_x + self.x_width == other_obj.pos_x + other_obj.x_width and self.pos_y + self.y_height == other_obj.pos_x + other_obj.y_height:
            print("collision detected!")