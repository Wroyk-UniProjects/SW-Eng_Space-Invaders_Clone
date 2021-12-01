import pytest
from src.hitbox import Hitbox



def test__init__():
    hitbox = None
    hitbox = Hitbox(1, 8, 2, 5)  # ( position_x, position_y, length, width)
    assert hitbox is not None and hitbox.pos_x == 1 and hitbox.pos_y == 8 and hitbox.length == 2 and hitbox.width == 5


def test_set_hitbox_size():
    hitbox = Hitbox(0, 0, 0, 0)
    hitbox.set_hitbox_size(6, 5)  # (length, width)
    assert hitbox.width == 5 and hitbox.length == 6


def test_set_hitbox_position():
    hitbox = Hitbox(0, 0, 0, 0)
    hitbox.set_hitbox_position(9, 7)
    assert hitbox.pos_x == 9 and hitbox.pos_y == 7


def test_get_hitbox_position():
    hitbox = Hitbox(3, 4, 0, 0)
    pos = hitbox.get_hitbox_position()
    assert pos[0] == 3 and pos[1] == 4 and len(pos) == 2


def test_get_size_hitbox():
    hitbox = Hitbox(0, 0, 8, 1)
    pos = hitbox.get_size_hitbox()
    assert pos[0] == 1 and pos[1] == 8 and len(pos) == 2


def test_is_touching_collides():
    hitbox1 = Hitbox(0, 0, 5, 5)
    hitbox2 = Hitbox(4, 4, 5, 5)
    assert hitbox1.is_touching(hitbox2)


def test_is_touching_doesnt_collides():
    hitbox1 = Hitbox(0, 0, 5, 5)
    hitbox2 = Hitbox(5, 5, 5, 5)
    assert not hitbox1.is_touching(hitbox2)
