import pyglet
from pyglet import clock
from pyglet.window import Window, FPSDisplay

from gameobject import GameObject
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

        clock.schedule(self.update)

        self.fps_display = FPSDisplay(window)

    def setup(self):
        # setup stuff
        self.game_objects.append(RunningLabels(self.batch))
        self.game_objects.append(Player(50, 50, '../assets/player.png'))

    def on_draw(self):
        self.window.clear()
        self.batch.draw()

        # call draw() Method from all GameObjects
        # for game_object in self.game_objects:
        #   if hasattr(game_object, "draw"):
        #      game_object.draw()

        self.fps_display.draw()

    def update(self, dt):
        # call update() Method from all GameObjects
        for game_object in self.game_objects:
            if hasattr(game_object, "update"):
                game_object.update(dt)

    def run(self):
        pyglet.app.run()

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
