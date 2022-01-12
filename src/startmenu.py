from pyglet.text import Label

from gamescene import GameScene


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
                      batch=self.batch)

        self.game_objects.append(title)

    def update(self, dt):
        pass

    def on_key_press(self, symbol, modifiers):
        pass

    def on_key_release(self, symbol, modifiers):
        pass

    def on_mouse_press(self, x, y, button, modifiers):
        pass
