class scorecalc:

    def __init(self):
        self.player
        self.enemy
        self.score = 0

    def calc_points_earned_from_enemy_hit(self, enemy, point_hit):

        #calc the points earned off of how far the user hits it off the center
        center = enemy.enemyWidth/2
        self.score += abs(center - point_hit)

    def calc_points_lost_from_death(self):
        self.score = round(self.score/2)

    def add_points_for_level_complete(self):
        self.score += 10000