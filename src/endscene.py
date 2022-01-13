import pyglet
from pyglet.sprite import Sprite
from pyglet.text import Label
from pyglet.window import key

from gameobject import UI, BACKGROUND
from gamescene import GameScene
from gamestate import GAME_STATE, GameStates


class EndScene(GameScene):

    def __init__(self, width, height):
        super(EndScene, self).__init__(width, height)
        self.max_chars = 5
        self.chars_number = self.max_chars
        self.state = None

    def setup(self):
        self.game_over = Label("Game Over",
                               font_name="monogramextended",
                               font_size=72,
                               x=self.width / 2,
                               y=self.height / 2 + 150,
                               anchor_x='center',
                               anchor_y='center',
                               group=UI,
                               batch=self.batch)

        score_text = Label("Your Score",
                           font_name="monogramextended",
                           font_size=40,
                           x=self.width / 2,
                           y=self.height / 2 + 60,
                           anchor_x='center',
                           anchor_y='center',
                           group=UI,
                           batch=self.batch)

        self.score = Label(f"{GAME_STATE.score}",
                      font_name="monogramextended",
                      font_size=54,
                      x=self.width / 2,
                      y=self.height / 2,
                      anchor_x='center',
                      anchor_y='center',
                      group=UI,
                      batch=self.batch)

        text = 'Press ENTER to restart the game or ESC to close the game'
        stuff = Label(text,
                      font_name="monogramextended",
                      font_size=24,
                      x=self.width / 2,
                      y=self.height / 6,
                      anchor_x='center',
                      anchor_y='center',
                      group=UI,
                      batch=self.batch)

        self.input_text = "_" * self.max_chars
        self.input = Label(self.input_text,
                           font_name="monogramextended",
                           font_size=40,
                           x=self.width / 2,
                           y=self.height / 3,
                           anchor_x='center',
                           anchor_y='center',
                           group=UI,
                           batch=self.batch)

        bg_image = pyglet.image.load("../assets/bg.png")
        self.lb_bg = Sprite(bg_image, x=0, y=0, batch=self.paused_batch, group=BACKGROUND)

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

    def show_top10(self):
        names = GAME_STATE.leaderboard.keys()
        scores = GAME_STATE.leaderboard.values()
        for i in range(10):
            if i >= len(GAME_STATE.leaderboard):
                break

            entry = Label(f"{names[i]}:  {scores[i]}",
                       font_name="monogramextended",
                       font_size=40,
                       x=self.width / 2,
                       y=self.height - 200 - 22*i,
                       anchor_y='center',
                       group=UI,
                       batch=self.paused_batch)


    def on_key_press(self, symbol, modifiers):

        if symbol is key.RETURN or symbol is key.ENTER:

            if self.chars_number <= 0:
                GAME_STATE.save_leaderboard(self.input_text)

            GAME_STATE.set_game_state(GameStates.RELAUNCHING)

            self.chars_number = self.max_chars
            self.input_text = "_"*self.max_chars

        elif symbol is key.ESCAPE:

            if self.chars_number <= 0:
                GAME_STATE.save_leaderboard(self.input_text)

            GAME_STATE.set_game_state(GameStates.EXIT)
        elif symbol is key.SPACE and modifiers is key.MOD_CTRL:
            if GAME_STATE.state == GameStates.PAUSED:
                GAME_STATE.set_game_state(self.state)
            else:
                GAME_STATE.set_game_state(GameStates.PAUSED)
                self.show_top10()
        else:
            try:
                if self.chars_number > 0 and not modifiers:
                    char = chr(symbol)
                    index = self.max_chars - self.chars_number

                    if index == 0:
                        self.input_text = char + self.input_text[(index + 1):]

                    elif index == self.max_chars - 1:
                        self.input_text = self.input_text[:index] + char

                    else:
                        self.input_text = self.input_text[:index] + char + self.input_text[(index + 1):]

                    self.input.text = self.input_text
                    self.chars_number = self.chars_number - 1

            except OverflowError:
                pass

    def on_key_release(self, symbol, modifiers):
        pass

    def on_mouse_press(self, x, y, button, modifiers):
        pass

    def show_game_over_text(self, state):
        self.score.text = f"{GAME_STATE.score}"
        if state == GameStates.WON:
            self.game_over.text = "You Won"
            self.state = GameStates.WON
        elif state == GameStates.LOST:
            self.game_over.text = "Game Over"
            self.state = GameStates.LOST

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