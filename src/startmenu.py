import pyglet
from pyglet import resource
from pyglet.gui import PushButton, WidgetBase
from pyglet.input import Button
from pyglet.shapes import Rectangle
from pyglet.sprite import Sprite
from pyglet.text import Label
from pyglet.window import key

from gameobject import UI, BACKGROUND
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

        bg_image = pyglet.image.load("../assets/bg.png")
        self.lb_bg = Sprite(bg_image, x=0, y=0, batch=self.paused_batch, group=BACKGROUND)

        #self.lb_bg = PushButton(0, 0, bg_image, bg_image, batch=self.batch)
        #self.lb_bg.set_handler('on_press', self.on_press())

        lb = Label("Leaderboard",
                      font_name="monogramextended",
                      font_size=64,
                      x=self.width / 2,
                      y=self.height - 50,
                      anchor_x='center',
                      anchor_y='center',
                      group=UI,
                      batch=self.paused_batch)


    def update(self, dt):
        pass

    def on_key_press(self, symbol, modifiers):
        if symbol is key.RETURN or symbol is key.ENTER:
            GAME_STATE.set_game_state(GameStates.ACTIVE)
        elif symbol is key.ESCAPE:
            GAME_STATE.set_game_state(GameStates.EXIT)
        elif symbol is key.SPACE:
            if GAME_STATE.state == GameStates.PAUSED:
                GAME_STATE.set_game_state(GameStates.LAUNCHING)
            else:
                GAME_STATE.set_game_state(GameStates.PAUSED)
                self.show_top10()

    def show_top10(self):
        names = list(GAME_STATE.leaderboard.keys())
        scores = list(GAME_STATE.leaderboard.values())
        for i in range(10):
            if i >= len(GAME_STATE.leaderboard):
                break

            entry = Label(f"{names[i]}:  {scores[i]}",
                          font_name="monogramextended",
                          font_size=32,
                          x=self.width / 2 - 150,
                          y=self.height - 200 - 36 * i,
                          anchor_y='center',
                          group=UI,
                          batch=self.paused_batch)

    def on_key_release(self, symbol, modifiers):
        pass

    def on_mouse_press(self, x, y, button, modifiers):
        pass

    def on_press(self):
        print("testasd")