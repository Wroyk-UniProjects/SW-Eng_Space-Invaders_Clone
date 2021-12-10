import hitbox


class Lives:
    num_of_lives = 3

    def __init__(self, num_of_lives):
        # loop to check num of lives
        while num_of_lives > 0:
            self.active = True
        else:
            self.die()

        # loop to decrement lives if hit

    # death
    def die(self):
        self.active = False
        # todo: add game over functions
