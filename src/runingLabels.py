import pyglet
from pyglet.sprite import Sprite
from pyglet.text import Label

from gameobject import GameObject, UI, GAMEOBJECTS


class RunningLabels(GameObject):

    def __init__(self):
        self.label = Label('Test: uncorrected for Delta t',
                           font_name='monogramextended',
                           font_size=36,
                           x=600, y=424,
                           anchor_x='right', anchor_y='center', group=UI)
        self.label1 = Label('Test: corrected for Delta t',
                            font_name='monogramextended',
                            font_size=36,
                            x=600, y=296,
                            anchor_x='right', anchor_y='center', group=UI)
        image = pyglet.image.load('assets/404.png')
        self.s = Sprite(image, x=300, y=300, group=GAMEOBJECTS)
        self.s.update(scale_x=2, scale_y=2)
        # https://pyglet.readthedocs.io/en/latest/programming_guide/graphics.html#batches-and-groups-in-other-modules

    def update(self, dt):
        self.label.x += 1  # uncorrected for Delta t
        self.label1.x += 60 * dt  # corrected for Delta t

    def draw(self):
        self.label.draw()
        self.label1.draw()
        self.s.draw()
