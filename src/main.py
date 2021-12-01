# This is a sample Python script.
import json

from pyglet import font, resource
from pyglet.window import Window

from gameloop import GameBoard


def lode_settings() -> dict:
    json_file = resource.file('settings.json')
    s: dict = json.load(json_file)
    return s


if __name__ == '__main__':
    resource.path = ['../assets']
    resource.reindex()

    settings: dict = lode_settings()
    resource.add_font('monogram-extended.ttf')

    window = Window(settings.get("window_width"), settings.get("window_height"), vsync=False)
    gameboard: GameBoard = GameBoard(window, "Space Invaders")
    gameboard.setup()
    gameboard.run()
