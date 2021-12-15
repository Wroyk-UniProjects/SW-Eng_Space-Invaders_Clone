import time

import pyglet
from pyglet import clock
from pyglet.window import Window, FPSDisplay

import enemy
import hitbox
import projectile
from enemy import Enemy, EnemyMesh
from gameobject import GameObject
from hitbox import HitMask
from runingLabels import RunningLabels
from Player import Player


class GameBoard:
    window: Window = None

    game_objects = []

    def __init__(self, window: Window, game_name: str):
        self.batch = pyglet.graphics.Batch()
        self.window = window
        self.window.push_handlers(self)
        self.window.set_caption(game_name)

        self.alive = False

        self.target_ups = 120.0
        self.target_fps = 60.0

        self.fps_display = FPSDisplay(window)

    def setup(self):
        # setup stuff
        #self.game_objects.append(RunningLabels(self.batch))
        self.game_objects.append(Player(50, 50, '../assets/player.png', self.batch))

        #projectile.spawn(self.window.width / 2, 0, HitMask.ENEMY, projectile.Direction.UP, self.batch)

        # adding multiple Enemies to game_objects
        enemyMesh1 = EnemyMesh(6, self.batch)
        enemy_list = enemyMesh1.getEnemyMesh()
        self.game_objects = enemy_list + self.game_objects

    def render(self):
        self.window.clear()

        self.batch.draw()
        hitbox.debug_hitbox_batch.draw()

        self.fps_display.draw()
        self.window.flip()

    def update(self, dt: object):
        # call update() Method from all GameObjects
        for game_object in self.game_objects:
            if hasattr(game_object, "update"):
                game_object.update(dt)

        # process active Projectiles
        for current_projectile in projectile.active_projectiles:
            current_projectile.update(dt)
            for game_object in self.game_objects:

                if hasattr(game_object, "hitbox") and current_projectile.is_colliding(game_object.hitbox):
                    #print(f"{current_projectile}; {game_object}")
                    current_projectile.on_collision()
                    if hasattr(game_object, "on_collision"):
                        game_object.on_collision()
                    break
        enemy.shoot_cooldown -= dt
        hitbox.debug_hitbox_update()

    def run(self):
        # clock.schedule(self.update)
        self.alive = True
        last_scheduled_update = time.time()
        last_scheduled_frame = time.time()
        # pyglet.app.run()
        while self.alive == 1:

            # physics loop
            if time.time() - last_scheduled_update > 1.0 / self.target_ups:
                self.update(time.time() - last_scheduled_update)
                last_scheduled_update = time.time()

            # rendering loop
            if self.target_fps and time.time() - last_scheduled_frame > 1.0 / self.target_fps:
                self.render()
                last_scheduled_frame = time.time()
            elif self.target_fps is None:
                self.render()

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
