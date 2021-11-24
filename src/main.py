# This is a sample Python script.
import json

from Gameloop import Gameloop


def print_hi(name):
    return 4


def lode_settings() -> dict:
    with open("assets/settings.json") as json_file:
        s: dict = json.load(json_file)
    return s


if __name__ == '__main__':
    settings: dict = lode_settings()

    gameloop = Gameloop()
    gameloop.setup(settings.get("window_width"), settings.get("window_height"))
    gameloop.run()
