import projectile


class Lives:
    num_of_lives = 3

    def __init__(self, num_of_lives):
        # loop to check num of lives
        while num_of_lives > 0:
            self.active = True
        else:
            self.die()

        # loop to decrement lives if hit
        if projectile.is_touching(other_obj="hitbox"):
            num_of_lives - 1

    # death
    def die(self):
        self.active = False
        # todo: add game over functions
