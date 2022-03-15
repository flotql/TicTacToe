

class Board:

    def __init__(self):
        self.board = []

    def createBoard(self):
        for i in range(3):
            line = []
            for j in range(3):
                line.append('-')
            self.board.append(line)

    def showBoard(self):
        for line in self.board:
            for j in line:
                print("   ",j, end=" ")
            print()

    def casePicked(self,line,column,who):
        self.board[line-1][column-1] = who

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
        res = ""
        for i in self.board:
            for j in i:
                if self.board[i][j] == "X":
                    res +="X"
                elif self.board[i][j] == "O":
                    res += "O"
                else:
                    res += "-"
            if res == "XXX" or res == "OOO":
                return True
        return False

    def checkColumn(self):
        res = ""
        for i in self.board:
            for j in i:
                res += self.board[j][i]
            if res == "XXX" or res == "OOO":
                return True
        return False

    def checkDiagonal(self):
        res = ""
        for i in self.board:
            res += self.board[i][i]
            if res == "XXX" or res == "OOO":
                return True
        return False

    def isBoardFull(self):
        for i in self.board:
            for j in i:
                if j == '-':
                    return False
        return True