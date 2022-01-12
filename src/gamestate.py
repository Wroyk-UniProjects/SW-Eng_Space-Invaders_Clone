import json
from enum import Enum

from pyglet import resource
from pyglet.window import key
from pyglet.window import Window
# from player import Player
from enemy import Enemy


class GameStates(Enum):
    LUNCHING = -2
    EXIT = -1
    ACTIVE = 1
    PAUSED = 0
    WON = 2
    LOST = 3


class GameState:
    # player: Player = None
    # enemiesArr = []
    # gameStarted = None
    # gameStopped = None
    # gameLost = None
    # gameWon = None

    state = GameStates.LUNCHING

    # def __init__(self, player, enemies):
    # self.gameLost = False
    # self.gameStarted = False
    # self.gameStopped = False
    # self.gameWon = False
    # for enemy in enemies:
    # self.enemiesArr.append(enemy)
    # self.player = player

    def set_game_won(self):
        self.state = GameStates.WON

    def set_game_lost(self):
        self.state = GameStates.LOST

    def set_game_state(self, state: GameStates):
        self.state = state

    def on_key_press(self, symbol, modifiers):
        if symbol is key.RETURN or symbol is key.ENTER:
            self.gameStarted = True
        elif symbol is key.Q:
            self.gameStopped = True

    def checkIfGameStarted(self):
        return self.gameStarted

    def checkIfGameStopped(self):
        return self.gameStopped

    def checkIfPlayerDead(self):
        if not self.player.active:
            self.gameLost = True

    def checkIfPlayerWon(self):
        if len(self.enemiesArr) <= 0:
            self.gameWon = True

    def getLoseStatus(self):
        return self.gameLost

    def jsonLoadLeaderboard(self):
        with open(resource.file('leaderboard.json')) as leaderboard:
            jsonData = json.load(leaderboard)
        return jsonData

    def update(self, dt):
        self.checkIfPlayerDead()
        enemyIndex = 0
        for enemy in self.enemiesArr:
            if not enemy.active:
                self.enemiesArr.pop(enemyIndex)
            enemyIndex += 1
        self.checkIfPlayerWon()
        # print('Enemies left: ' + str(len(self.enemiesArr)))


# Singleton
GAME_STATE = GameState()
