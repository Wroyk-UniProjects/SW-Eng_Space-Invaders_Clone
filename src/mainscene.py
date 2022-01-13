from pyglet.text import Label
from pyglet.window import key

import enemy
import projectile
from enemy import EnemyMesh
from gamescene import GameScene
from gamestate import GAME_STATE, GameStates
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
                                       anchor_y='center',
                                       batch=self.paused_batch)

        # setting up shields
        shields_factory = shieldFactory(self.batch)
        self.shields_list = shields_factory.getShields()
        self.game_objects = self.shields_list + self.game_objects

        # adding multiple Enemies to game_objects
        enemy_mesh = EnemyMesh(6, self.batch)
        self.enemy_list = enemy_mesh.getEnemyMesh()

        self.player = Player(50, 50, '../assets/player.png', self.batch)

        self.game_objects.append(self.player)
        self.game_objects += self.enemy_list

        self.scorecalc = Scorecalc(self.batch, self.player, self.enemy_list)
        self.game_objects.append(self.scorecalc)

    def update(self, dt):
        if not self.paused:
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

        self.enemy_counter()

        enemy.shoot_cooldown -= dt

    def on_key_press(self, symbol, modifiers):
        if symbol == key.P:
            if self.paused:
                self.paused = False
                GAME_STATE.set_game_state(GameStates.ACTIVE)
            else:
                self.paused = True
                GAME_STATE.set_game_state(GameStates.PAUSED)
        elif symbol is key.PAGEUP:
            GAME_STATE.set_game_won()
        elif symbol is key.PAGEDOWN:
            GAME_STATE.set_game_lost()

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

    def enemy_counter(self):
        if len(self.enemy_list) <=0:
            GAME_STATE.set_game_won()

        for enemy in self.enemy_list:
            if not enemy.active:
                self.enemy_list.remove(enemy)
