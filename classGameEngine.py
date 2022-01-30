from classPlayer import *
import random

class GameEngine:

    def __init__(self, firstPlayer, secondPlayer):
        self.firstPlayer = firstPlayer
        self.secondPlayer = secondPlayer
        self.p1Score = 0
        self.p2Score = 0
        self.players = Player(firstPlayer, secondPlayer)

    def whoStart(self, firstPlayer, secondPlayer):
        roll = random.randint(1,2)
        if roll == 1:
            print(f"{firstPlayer} start")
        else:
            print(f"{secondPlayer} start")

    def pickCase(self):

    def Winner(self, firstPlayer, secondPlayer):
