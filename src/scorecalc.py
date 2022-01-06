from gameobject import UI
from gameobject import GameObject
from pyglet.text import Label

class Scorecalc (GameObject):



    def __init__(self, batch, player, enemy_list):
        self.batch = batch
        self.player = player
        self.player_lives = player.num_of_lives
        self.num_of_enemies = len(enemy_list)
        self.enemy_list = enemy_list
        self.score = 0
        self.score_label = Label('Score: '+str(self.score), font_name='monogramextended',
                                 font_size=20, x=1100, y=700, batch=self.batch, group=UI)

    def calc_points_earned_from_enemy_hit(self):
        #calc the points earned off of how far the user hits it off the center
        #center = enemy.enemyWidth/2
        #self.score += abs(center - point_hit)
        self.score += 150

    def calc_points_lost_from_death(self):
        self.score = round(self.score/2)

    def add_points_for_level_complete(self):
        #might need to update this based on what the scores look like
        self.score += 10000

    def subtract_points_for_broken_shield(self):
        #also need to update this probably
        self.score -= 500

    def update(self, dt):
        if self.player.num_of_lives < self.player_lives:
            self.calc_points_lost_from_death()
            self.player_lives = self.player.num_of_lives

        if self.num_of_enemies > len(self.enemy_list):
            self.calc_points_earned_from_enemy_hit()
            self.num_of_enemies = len(self.enemy_list)

        self.score_label.text = 'Score: '+str(self.score)