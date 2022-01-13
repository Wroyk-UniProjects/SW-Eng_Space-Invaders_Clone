from pyglet import resource
from pyglet.gui import PushButton, WidgetBase
from pyglet.input import Button
from pyglet.text import Label
from pyglet.window import key

from gameobject import UI
from gamescene import GameScene
import tkinter as tk

from gamestate import GAME_STATE, GameStates


class StartMenu(GameScene):

    def __init__(self, width, height, title):
        super(StartMenu, self).__init__(width, height)
        self.title = title

    def setup(self):
        title = Label(self.title,
                      font_name="monogramextended",
                      font_size=64,
                      x=self.width / 2,
                      y=self.height - 100,
                      anchor_x='center',
                      anchor_y='center',
                      group=UI,
                      batch=self.batch)

        text = 'Press ENTER to start the Game or ESC to close the game'
        stuff = Label(text,
                      font_name="monogramextended",
                      font_size=24,
                      x=self.width / 2,
                      y=self.height / 2,
                      anchor_x='center',
                      anchor_y='center',
                      group=UI,
                      batch=self.batch)

    def update(self, dt):
        pass

    def on_key_press(self, symbol, modifiers):
        if symbol is key.RETURN or symbol is key.ENTER:
            GAME_STATE.set_game_state(GameStates.ACTIVE)
        elif symbol is key.ESCAPE:
            GAME_STATE.set_game_state(GameStates.EXIT)

    def on_key_release(self, symbol, modifiers):
        pass

    def on_mouse_press(self, x, y, button, modifiers):
        pass
    