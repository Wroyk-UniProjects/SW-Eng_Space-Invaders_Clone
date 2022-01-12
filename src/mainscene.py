from pyglet.text import Label
from pyglet.window import key

import projectile
from enemy import EnemyMesh
from gamescene import GameScene
from player import Player
from scorecalc import Scorecalc
from shields import shieldFactory


class MainScene(GameScene):
    active = False
    paused = False

    game_objects = None

    def __init__(self, width, height):
        super(MainScene, self).__init__(width, height)

        self.active = True

        self.game_objects = []

    def setup(self):
        self.lable_game_paused = Label("Game Paused",
                                       font_name="monogramextended",
                                       font_size=64,
                                       x=self.width / 2,
                                       y=self.height / 2,
                                       anchor_x='center',
                                       anchor_y='center')

        # setting up shields
        shields_factory = shieldFactory(self.batch)
        shields_list = shields_factory.getShields()
        self.game_objects = shields_list + self.game_objects

        # adding multiple Enemies to game_objects
        enemy_mesh = EnemyMesh(6, self.batch)
        enemy_list = enemy_mesh.getEnemyMesh()

        player = Player(50, 50, '../assets/player.png', self.batch)

        self.game_objects.append(player)
        self.game_objects += enemy_list

        self.scorecalc = Scorecalc(self.batch, player, enemy_list.copy())
        self.game_objects.append(self.scorecalc)


    def update(self, dt):
        # call update() Method from all GameObjects
        for game_object in self.game_objects:
            if hasattr(game_object, "update"):
                game_object.update(dt)

        # process active Projectiles
        for current_projectile in projectile.active_projectiles:
            current_projectile.update(dt)
            for game_object in self.game_objects:

                if hasattr(game_object, "hitbox") and current_projectile.is_colliding(game_object.hitbox):
                    # print(f"{current_projectile}; {game_object}")
                    current_projectile.on_collision()
                    if hasattr(game_object, "on_collision"):
                        game_object.on_collision()
                    break

    def on_key_press(self, symbol, modifiers):

        if symbol == key.P:
            if self.paused:
                self.paused = False
            else:
                self.paused = True

        if not self.paused:
            for game_object in self.game_objects:
                if hasattr(game_object, "on_key_press"):
                    game_object.on_key_press(symbol, modifiers)

    def on_key_release(self, symbol, modifiers):
        if not self.paused:
            for game_object in self.game_objects:
                if hasattr(game_object, "on_key_release"):
                    game_object.on_key_release(symbol, modifiers)

    def on_mouse_press(self, x, y, button, modifiers):
        if not self.paused:
            for game_object in self.game_objects:
                if hasattr(game_object, "on_mouse_press"):
                    game_object.on_mouse_press(x, y, button, modifiers)

