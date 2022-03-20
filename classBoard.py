

class Board:

    def __init__(self):
        self.board = []

    # Cree le plateau
    def createBoard(self):
        for i in range(3):
            line = []
            for j in range(3):
                line.append('-')
            self.board.append(line)

    # Affichage plateau
    def showBoard(self):
        for line in self.board:
            for j in line:
                print("   ",j, end=" ")
            print()

    # Selection case par joueur
    def casePicked(self,line,column,who):
        self.board[line-1][column-1] = who

    # Check si case vide ou non
    def caseEmpty(self,line,column):
        if self.board[line][column] == '-':
            return False
        else :
            print('~~~~~~~~~~~~~~~~~~~~')
            print ('Case already picked')
            print('~~~~~~~~~~~~~~~~~~~~')
            return True

    # Verification si une ligne est victorieuse (return True)
    def checkLine(self):
        verif = ''
        for i in self.board:
            for j in i:
                verif += j
            if verif == 'XXX' or verif == 'OOO':
                return True
        return False

    # Verification si une colonne est victorieuse (return True)
    def checkColumn(self):
        verifC1 = ''
        verifC2 = ''
        verifC3 = ''
        for i in self.board:
            for index,value in enumerate(i):
                if index == 0:
                    verifC1 += value
                elif index == 1:
                    verifC2 += value
                else:
                    verifC3 += value
            if verifC1 == 'XXX' or verifC1 == 'OOO':
                return True
            elif verifC2 == 'XXX' or verifC2 == 'OOO':
                return True
            elif verifC3 == 'XXX' or verifC3 == 'OOO':
                return True
        return False

    # Verification si une diago est victorieuse (return True)
    def checkDiagonal(self):
        res = ''
        for i in self.board:
            res += i[i]
            if res == 'XXX' or res == 'OOO':
                return True
        return False

    # Check si plateau plein
    def isBoardFull(self):
        for i in self.board:
            for j in i:
                if j == '-':
                    return False
        return True
