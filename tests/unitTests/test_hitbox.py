import pytest

from hitbox import Hitbox
from src import hitbox


class TestHitbox:

    def test__init__(self):
        hitbox = None
        hitbox = Hitbox(1, 8, 2, 5)
        assert hitbox is not None

    def test_set_hitbox_size(self):
        hitbox = Hitbox(0, 0, 0, 0)
        hitbox.set_hitbox_size(6, 5)  # (length, width)
        assert hitbox.width == 5 and hitbox.length == 6

    def test_set_hitbox_position(self):
        hitbox = Hitbox(0, 0, 0, 0)
        hitbox.set_hitbox_position(9, 7)
        assert hitbox.pos_x == 9 and hitbox.pos_y == 7

    def test_get_hitbox_position(self):
        hitbox = Hitbox(3, 4, 0, 0)
        pos = hitbox.get_hitbox_position()
        assert pos[0] == 3 and pos[1] == 4 and len(pos) == 2

    def test_get_size_hitbox(self):
        hitbox = Hitbox(0, 0, 8, 1)  # ( position_x, position_y, length, width)
        pos = hitbox.get_size_hitbox()
        assert pos[0] == 1 and pos[1] == 8 and len(pos) == 2

    def test_is_touching_collides(self):
        hitbox1 = hitbox.Hitbox(0, 0, 5, 5)
        hitbox2 = hitbox.Hitbox(4, 4, 5, 5)
        assert hitbox1.is_touching(hitbox2)

    def test_is_touching_doesnt_collides(self):
        hitbox1 = hitbox.Hitbox(0, 0, 5, 5)
        hitbox2 = hitbox.Hitbox(5, 5, 5, 5)
        assert not hitbox1.is_touching(hitbox2)
