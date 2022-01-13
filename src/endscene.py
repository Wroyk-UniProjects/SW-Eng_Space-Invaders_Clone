from pyglet.text import Label
from pyglet.window import key

from gameobject import UI
from gamescene import GameScene
from gamestate import GAME_STATE, GameStates


class EndScene(GameScene):

    def __init__(self, width, height):
        super(EndScene, self).__init__(width, height)

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

        score = Label(f"{GAME_STATE.score}",
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

    def update(self, dt):
        pass

    def on_key_press(self, symbol, modifiers):
        if symbol is key.RETURN or symbol is key.ENTER:
            GAME_STATE.set_game_state(GameStates.RELAUNCHING)
        elif symbol is key.ESCAPE:
            GAME_STATE.set_game_state(GameStates.EXIT)

    def on_key_release(self, symbol, modifiers):
        pass

    def on_mouse_press(self, x, y, button, modifiers):
        pass

    def show_game_over_text(self, state):
        if state == GameStates.WON:
            self.game_over.text = "You Won"
        elif state == GameStates.LOST:
            self.game_over.text = "Game Over"
