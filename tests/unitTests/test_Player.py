from src.Player import Player




def test_moveright():
    player = Player(50, 50, '../../assets/player.png')
    player.moveright()
    assert player.startx == 51


def test_moveleft():
    player = Player(50, 50, '../../assets/player.png')
    player.moveleft()
    assert player.startx == 49
