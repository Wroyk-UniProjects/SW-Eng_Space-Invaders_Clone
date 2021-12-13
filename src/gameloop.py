import time

import pyglet
from pyglet import clock
from pyglet.window import Window, FPSDisplay

import projectile
from Enemy import Enemy, EnemyMesh
from gameobject import GameObject
from hitbox import HitMask
from runingLabels import RunningLabels
from Player import Player


class GameBoard:
    window: Window = None
    moving_labels: GameObject = None
    game_objects = []

    def __init__(self, window: Window, game_name: str):
        self.batch = pyglet.graphics.Batch()
        self.window = window
        self.window.push_handlers(self)
        self.window.set_caption(game_name)

        self.alive = False

        self.physics_fps = 120
        self.draw_fps = 60
        self.last_scheduled_update = time.time()
        self.last_scheduled_draw = time.time()

        self.fps_display = FPSDisplay(window)

    def setup(self):
        # setup stuff
        # self.game_objects.append(RunningLabels(self.batch))
        self.game_objects.append(Player(50, 50, '../assets/player.png'))

        projectile.spawn(self.window.width / 2, 0, HitMask.ENEMY, projectile.Direction.UP, self.batch)

        # adding multiple Enemies to game_objects
        enemyMesh1 = EnemyMesh(6)
        enemy_list = enemyMesh1.getEnemyMesh()
        self.game_objects = enemy_list + self.game_objects

    def on_draw(self):
        self.window.clear()
        self.batch.draw()

        # !!!deprecated will be remove!!
        # call draw() Method from all GameObjects
        for game_object in self.game_objects:
            if hasattr(game_object, "draw"):
                game_object.draw()

        self.fps_display.draw()
        self.window.flip()

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
                    current_projectile.on_collision()
                    if hasattr(game_object, "on_collision"):
                        game_object.on_on_collision()
                    break

    def run(self):
        # clock.schedule(self.update)
        self.alive = True

        # pyglet.app.run()
        while self.alive == 1:
            if time.time() - self.last_scheduled_update > 1 / self.physics_fps:
                self.update(time.time() - self.last_scheduled_update)
                self.last_scheduled_update = time.time()

            if self.draw_fps and time.time() - self.last_scheduled_draw > 1 / self.draw_fps:
                self.on_draw()
                self.last_scheduled_draw = time.time()
            elif self.draw_fps is None:
                self.on_draw()

            event = self.window.dispatch_events()

    def on_close(self):
        self.alive = False

    def on_key_press(self, symbol, modifiers):
        for game_object in self.game_objects:
            if hasattr(game_object, "on_key_press"):
                game_object.on_key_press(symbol, modifiers)

    def on_key_release(self, symbol, modifiers):
        for game_object in self.game_objects:
            if hasattr(game_object, "on_key_release"):
                game_object.on_key_release(symbol, modifiers)

    def on_mouse_press(self, x, y, button, modifiers):
        for game_object in self.game_objects:
            if hasattr(game_object, "on_mouse_press"):
                game_object.on_mouse_press(x, y, button, modifiers)
