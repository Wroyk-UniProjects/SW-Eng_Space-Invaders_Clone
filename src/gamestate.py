from pyglet.window import key
from pyglet.window import Window
from Player import Player
from enemy import Enemy


class gamestate:
    player: Player = None
    enemiesArr = []
    window: Window = None
    gameStarted = None
    gameStopped = None
    gameLost = None

    def __init__(self, windows, player, enemies):
        self.window = windows
        self.gameLost = False
        self.gameStarted = False
        self.gameStopped = False
        for i in enemies:
            self.enemiesArr.append(i)
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

    def getLoseStatus(self):
        return self.gameLost

    def update(self, dt):
        self.checkIfPlayerDead()
        enemyIndex = 0
        for enemy in self.enemiesArr:
            if not enemy.active:
                self.enemiesArr.pop(enemyIndex)
            enemyIndex += 1
        print('Enemies left: ' + str(len(self.enemiesArr)))