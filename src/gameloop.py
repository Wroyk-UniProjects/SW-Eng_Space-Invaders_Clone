import pyglet


class Gameloop:
    window = None

    def __init__(self, window_width: int, window_height: int):
        self.window = pyglet.window.Window(window_width, window_height)
        self.window.push_handlers(self)

    def setup(self):
        self.label = pyglet.text.Label('Test',
                                       font_name='Times New Roman',
                                       font_size=36,
                                       x=self.window.width // 2, y=self.window.height // 2,
                                       anchor_x='center', anchor_y='center')

    def on_draw(self):
        self.window.clear()
        self.label.draw()

    def run(self):
        pyglet.app.run()
