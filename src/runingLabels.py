import pyglet
from pyglet.sprite import Sprite
from pyglet.text import Label

from gameobject import GameObject, UI, GAMEOBJECTS


class RunningLabels(GameObject):

    def __init__(self, batch):

        self.label = Label('Test: uncorrected for Delta t',
                           font_name='monogramextended',
                           font_size=36,
                           x=600, y=424,
                           anchor_x='right', anchor_y='center', group=UI, batch=batch)
        self.label1 = Label('Test: corrected for Delta t',
                            font_name='monogramextended',
                            font_size=36,
                            x=600, y=296,
                            anchor_x='right', anchor_y='center', group=UI, batch=batch)
        image = pyglet.resource.image('404.png')
        self.s = Sprite(image, x=300, y=300, group=GAMEOBJECTS, batch=batch)
        self.s.update(scale_x=2, scale_y=2)
        # https://pyglet.readthedocs.io/en/latest/programming_guide/graphics.html#batches-and-groups-in-other-modules
        print(f"{self.label.x}:{self.label1.x}")

    def update(self, dt):
        self.label.x += 1  # uncorrected for Delta t
        self.label1.x += 60 * dt  # corrected for Delta t
        print(f"{self.label.x}:{self.label1.x}:{dt}")
