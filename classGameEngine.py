from classBoard import *
import random

class GameEngine(Board):

    def __init__(self, firstPlayer, secondPlayer):
        self.firstPlayer = firstPlayer
        self.secondPlayer = secondPlayer
        self.p1Score = 0
        self.p2Score = 0
        self.p1 = "X"
        self.p2 = "O"
        self.turn = 0
        self.firstPlayer = firstPlayer
        self.secondPlayer = secondPlayer

    def whoStart(self, firstPlayer, secondPlayer):
        roll = random.randint(1,2)
        if roll == 1:
            print(f"{firstPlayer} play first")
        else:
            print(f"{secondPlayer} play first")
        return roll

    def turn(self,roll):
        if roll == 1:
            self.turn = 1


    def whoPlay(self):
        if self.turn % 2 == 0:
            print(f"It's {self.secondPlayer} turn")
            return self.p2
        else :
            print(f"It's {self.firstPlayer} turn")
            return self.p1

    def playTurn(self):
        self.turn += 1


    def whoWin(self):
        if self.turn % 2 == 0:
            self.p2Score += 1
            print(f"The winner is {self.secondPlayer}")
        else:
            self.p1Score += 1
            print(f"The winner is {self.firstPlayer}")