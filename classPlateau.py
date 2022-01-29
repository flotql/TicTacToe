


class Tiktaktoe:

    def __init__(self):
        self.board = []

    def Plateau(self):
        for i in range(3):
            line = []
            for j in range(3):
                line.append("")
            self.board.append(line)

