import pyglet
from pyglet.sprite import Sprite
from pyglet.text import Label

from gameobject import GameObject, UI, GAMEOBJECTS
from hitbox import Hitbox


class RunningLabels(GameObject):
    batch: pyglet.graphics.Batch() = None

    def __init__(self, batch):
        self.batch = batch

        # image = pyglet.resource.image('404.png')
        # self.s = Sprite(image, x=300, y=300, group=GAMEOBJECTS, batch=batch)
        # self.s.update(scale_x=2, scale_y=2)
        # self.hitbox = Hitbox(300, 300, self.s.width, self.s.height)
        # https://pyglet.readthedocs.io/en/latest/programming_guide/graphics.html#batches-and-groups-in-other-modules
        # print(f"{self.label.x}:{self.label1.x}")

    def update(self, dt):
        pass
        # self.labelOnStart.x += 60 * dt  # corrected for Delta t

    def createLabel(self, text):
        label = Label(text,
                           font_name='monogramextended',
                           font_size=36,
                           x=1280 // 2,
                           y=720 // 2, anchor_x='center', anchor_y='center', group=UI, batch=self.batch)
        return label
