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

    # Def qui commence
    def whoStart(self, firstPlayer, secondPlayer):
        roll = random.randint(1,2)
        if roll == 1:
            print(f"{firstPlayer} play first")
        else:
            print(f"{secondPlayer} play first")
        return roll

    # Def tour
    def turn(self,roll):
        if roll == 1:
            self.turn = 1

    # Def qui joue en fonction d'un modulo
    def whoPlay(self):
        if self.turn % 2 == 0:
            print(f"It's {self.secondPlayer} turn")
            return self.p2
        else :
            print(f"It's {self.firstPlayer} turn")
            return self.p1

    # Fais tourner le compteur de tour pour changer de joueur
    def playTurn(self):
        self.turn += 1

    # Def qui gagne
    def whoWin(self):
        if self.turn % 2 == 0:
            self.p2Score += 1
            print(f"The winner is {self.secondPlayer}")
        else:
            self.p1Score += 1
            print(f"The winner is {self.firstPlayer}")