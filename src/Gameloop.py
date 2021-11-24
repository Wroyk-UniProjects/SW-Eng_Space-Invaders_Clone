import pyglet


class Gameloop:

    def __init__(self):
        pass

    def setup(self, window_width: int, window_height: int):
        self.window = pyglet.window.Window(window_width, window_height)
        self.label = pyglet.text.Label('Hello, world',
                                       font_name='Times New Roman',
                                       font_size=36,
                                       x=self.window.width // 2, y=self.window.height // 2,
                                       anchor_x='center', anchor_y='center')

    def draw(self):
        self.window.clear()
        self.label.draw()

    def run(self):
        while True:
            self.draw()

