# This is a sample Python script.
import json

from pyglet import font
from pyglet.window import Window

from gameloop import GameBoard


def print_hi(name: str):
    return name


def lode_settings() -> dict:
    with open("assets/settings.json") as json_file:
        s: dict = json.load(json_file)
    return s


if __name__ == '__main__':
    settings: dict = lode_settings()
    font.add_file('assets/monogram-extended.ttf')

    window = Window(settings.get("window_width"), settings.get("window_height"), vsync=False)
    gameboard: GameBoard = GameBoard(window, "Space Invaders")
    gameboard.setup()
    gameboard.run()
