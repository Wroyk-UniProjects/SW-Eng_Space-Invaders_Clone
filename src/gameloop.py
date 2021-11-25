import pyglet
from pyglet import font, clock
from pyglet.window import Window


class Gameloop:
    window = None

    def __init__(self, window_width: int, window_height: int):
        self.window = Window(window_width, window_height)
        self.window.push_handlers(self)

    def setup(self, game_name: str):
        self.window.set_caption(game_name)
        font.add_file('assets/monogram-extended.ttf')

        clock.schedule_interval(self.update, 1 / 60)

        self.label = pyglet.text.Label('Test a lot more',
                                       font_name='monogramextended',
                                       font_size=36,
                                       x=self.window.width // 2, y=self.window.height // 2,
                                       anchor_x='center', anchor_y='center')
        self.fps_label = pyglet.text.Label('0',
                                           font_name='monogramextended',
                                           font_size=16,
                                           x=self.window.width - 29, y=self.window.height - 20,
                                           anchor_x='center', anchor_y='center')

    def on_draw(self):
        self.window.clear()
        self.label.draw()
        self.fps_label.draw()

    def update(self, dt):
        #self.label.x += 1
        self.fps_label.text = str(int(1/dt))

    def run(self):
        pyglet.app.run()
