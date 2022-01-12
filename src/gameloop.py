import time
from threading import Thread

import pyglet
from pyglet import clock
from pyglet.text import Label
from pyglet.window import Window, FPSDisplay, key

import enemy
import hitbox
import projectile
from enemy import Enemy, EnemyMesh
from gameobject import GameObject
from gamescene import GameScene
from hitbox import HitMask
from centeredLabels import CenteredLabel
from pyglet.window import key

from mainscene import MainScene
from player import Player
from shields import shield
from shields import shieldFactory
from gamestate import gamestate
from time import sleep

from scorecalc import Scorecalc


class GameBoard:
    window: Window = None

    game_objects = []

    active_scene: GameScene = None

    gamestate = None
    StartingLabel: CenteredLabel = None
    StopLabel: CenteredLabel = None
    LoseLabel: CenteredLabel = None
    StatsLabel: CenteredLabel = None

    def __init__(self, window: Window, game_name: str):

        self.batch = pyglet.graphics.Batch()
        self.batch_startScreen = pyglet.graphics.Batch()
        self.batch_stopScreen = pyglet.graphics.Batch()
        self.batch_loseScreen = pyglet.graphics.Batch()
        self.window = window
        self.window.push_handlers(self)
        self.window.set_caption(game_name)
        self.alive = False
        self.paused = False

        self.target_ups = 120.0
        self.target_fps = 60.0

        self.main_scene = MainScene(self.window.width, self.window.height)

        self.fps_display = FPSDisplay(window)


    def setup(self):
        # setup stuff
        #self.game_objects.append(RunningLabels(self.batch))

        self.main_scene.setup()

        self.active_scene = self.main_scene

        #self.gamestate = gamestate(player, enemy_list)
        #self.game_objects.append(self.gamestate)

        self.StartingLabel = CenteredLabel(self.batch_startScreen)
        self.game_objects.append(self.StartingLabel)

        self.StopLabel = CenteredLabel(self.batch_stopScreen)
        self.game_objects.append(self.StopLabel)

        self.LoseLabel = CenteredLabel(self.batch_loseScreen)
        self.game_objects.append(self.LoseLabel)

        #self.game_objects.append(player)
        #self.game_objects += enemy_list
        # projectile.spawn(self.window.width / 2, 0, HitMask.ENEMY, projectile.Direction.UP, self.batch)

    def render(self):
        self.window.clear()

        self.active_scene.batch.draw()
        #self.batch.draw()
        #hitbox.debug_hitbox_batch.draw()

        if self.paused:
            self.lable_game_paused.draw()

        self.fps_display.draw()
        self.window.flip()


    def renderStartScene(self):
        self.window.clear()
        self.StartingLabel.createLabel('Press ENTER to start the game...')
        self.batch_startScreen.draw()
        self.window.flip()

    def renderStopScene(self):
        self.window.clear()
        self.StopLabel.createLabel('The game has been stopped...')
        self.batch_stopScreen.draw()
        self.window.flip()

    def renderLoseScene(self):
        self.window.clear()
        self.LoseLabel.createLabel('The player has died... Game over!')
        self.batch_loseScreen.draw()
        self.window.flip()

    def update(self, dt: float):


        self.gamestate.update(dt)

        enemy.shoot_cooldown -= dt
        #hitbox.debug_hitbox_update()

    def remove_not_alive_enemies(self):
        while self.alive == 1:
            if not self.paused:
                for game_object in self.game_objects:
                    if hasattr(game_object, "active") and not game_object.active:
                        self.game_objects.remove(game_object)
            sleep(1.0 / self.target_ups)

    def run(self):
        # clock.schedule(self.update)
        self.alive = True
        last_scheduled_update = time.time()
        last_scheduled_frame = time.time()
        garbage_collector = Thread(target=self.remove_not_alive_enemies)

        garbage_collector.start()
        # pyglet.app.run()
        while self.alive == 1:
            try:
                if self.gamestate.checkIfGameStarted() and not self.gamestate.checkIfGameStopped() and not self.gamestate.getLoseStatus():

                    # physics loop
                    if time.time() - last_scheduled_update > 1.0 / self.target_ups:
                        if not self.paused:
                            self.update(time.time() - last_scheduled_update)
                        last_scheduled_update = time.time()
                    # rendering loop
                    if self.target_fps and time.time() - last_scheduled_frame > 1.0 / self.target_fps:
                        self.render()
                        last_scheduled_frame = time.time()
                    elif self.target_fps is None:
                        self.render()

                elif self.gamestate.checkIfGameStopped():

                    self.renderStopScene()
                    sleep(2)
                    self.alive = False

                elif not self.gamestate.player.active:  # <--

                    self.renderLoseScene()
                    sleep(3)
                    self.alive = False

                elif self.gamestate.gameWon:  # <--
                    pass

                else:
                    self.renderStartScene()

                event = self.window.dispatch_events()

            except KeyboardInterrupt:
                self.on_close()
                sleep(0.001)
        garbage_collector.join()

    def on_close(self):
        self.alive = False

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
