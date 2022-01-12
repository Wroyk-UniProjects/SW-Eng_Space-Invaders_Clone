import json

from pyglet import resource
from pyglet.window import key
from pyglet.window import Window
from Player import Player
from enemy import Enemy


class gamestate:
    player: Player = None
    enemiesArr = []
    gameStarted = None
    gameStopped = None
    gameLost = None
    gameWon = None

    def __init__(self, player, enemies):
        self.gameLost = False
        self.gameStarted = False
        self.gameStopped = False
        self.gameWon = False
        for enemy in enemies:
            self.enemiesArr.append(enemy)
        self.player = player

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
