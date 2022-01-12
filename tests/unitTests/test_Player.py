from player import Player


def test_moveright():
    player = Player(50, 50, '../../assets/player.png')
    player.moveright()
    assert player.velocity == 400


def test_moveleft():
    player = Player(50, 50, '../../assets/player.png')
    player.moveleft()
    assert player.velocity == -400
