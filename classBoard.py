

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
        res = ''
        for i in self.board:
            for j in i:
                res += self.board[i][j]
            if res == 'XXX' or res == 'OOO':
                return True
        return False

    # Verification si une colonne est victorieuse (return True)
    def checkColumn(self):
        res = ''
        for i in self.board:
            for j in i:
                res += self.board[j][i]
            if res == 'XXX' or res == 'OOO':
                return True
        return False

    # Verification si une diago est victorieuse (return True)
    def checkDiagonal(self):
        res = ''
        for i in self.board:
            res += self.board[i][i]
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