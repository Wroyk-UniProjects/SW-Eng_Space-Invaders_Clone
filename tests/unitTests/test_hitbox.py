import pytest

import hitbox
from hitbox import Hitbox, HitMask


def test__init__():
    hitbox = None
    hitbox = Hitbox(1, 8, 2, 5)  # ( position_x, position_y, width, height)
    assert hitbox is not None and hitbox.x == 1 and hitbox.y == 8 and hitbox.width == 2 and hitbox.height == 5


def test_set_hitbox_size():
    hitbox = Hitbox(0, 0, 0, 0)
    hitbox.set_hitbox_size(6, 5)  # (width, height)
    assert hitbox.width == 6 and hitbox.height == 5


def test_set_hitbox_position():
    hitbox = Hitbox(0, 0, 0, 0)
    hitbox.set_hitbox_position(9, 7)
    assert hitbox.x == 9 and hitbox.y == 7


def test_get_hitbox_position():
    hitbox = Hitbox(3, 4, 0, 0)
    pos = hitbox.get_hitbox_position()
    assert pos[0] == 3 and pos[1] == 4 and len(pos) == 2


def test_get_size_hitbox():
    hitbox = Hitbox(0, 0, 8, 1)
    pos = hitbox.get_size_hitbox()
    assert pos[0] == 8 and pos[1] == 1 and len(pos) == 2


def test_is_colliding_collides():
    hitbox1 = Hitbox(0, 0, 5, 5)
    hitbox2 = Hitbox(4, 4, 5, 5)
    assert hitbox1.is_colliding(hitbox2)


def test_is_colliding_doesnt_collides():
    hitbox1 = Hitbox(0, 0, 5, 5)
    hitbox2 = Hitbox(5, 5, 5, 5)
    assert not hitbox1.is_colliding(hitbox2)


def test_is_colliding_masked_hitbox1_all_hitbox2():
    hitbox1 = Hitbox(0, 0, 5, 5, mask=HitMask.ENEMY)
    hitbox2 = Hitbox(4, 4, 5, 5)
    assert hitbox1.is_colliding(hitbox2)


def test_is_colliding_all_hitbox1_masked_hitbox2():
    hitbox1 = Hitbox(0, 0, 5, 5)
    hitbox2 = Hitbox(4, 4, 5, 5, mask=HitMask.ENEMY)
    assert hitbox1.is_colliding(hitbox2)


def test_is_colliding_masked_hitbox1_all_hitbox2_revers():
    hitbox1 = Hitbox(0, 0, 5, 5, mask=HitMask.ENEMY)
    hitbox2 = Hitbox(4, 4, 5, 5)
    assert hitbox2.is_colliding(hitbox1)


def test_is_colliding_all_hitbox1_masked_hitbox2_revers():
    hitbox1 = Hitbox(0, 0, 5, 5)
    hitbox2 = Hitbox(4, 4, 5, 5, mask=HitMask.ENEMY)
    assert hitbox2.is_colliding(hitbox1)


def test_is_colliding_masked1_hitbox1_masked2_hitbox2():
    hitbox1 = Hitbox(0, 0, 5, 5, mask=HitMask.PLAYER)
    hitbox2 = Hitbox(4, 4, 5, 5, mask=HitMask.ENEMY)
    assert not hitbox1.is_colliding(hitbox2)


def test_is_colliding_same_mask():
    hitbox1 = Hitbox(0, 0, 5, 5, mask=HitMask.ENEMY)
    hitbox2 = Hitbox(4, 4, 5, 5, mask=HitMask.ENEMY)
    assert hitbox1.is_colliding(hitbox2)

