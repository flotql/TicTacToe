from classGameEngine import *
from classBoard import *
game = True

while game:
    # Mise en place joueurs
    p1Score = 0
    p2Score = 0
    player1 = input("First player name:\n")
    player2 = input("Second player name:\n")
    print(f"Hello {player1} and {player2}, let's the game begin hope you have fun !\n")
    print('#-------------------------------#')
    print('#-----------LETS BEGIN----------#')
    print('#-------------------------------#')
    # Mise en place du plateau
    board = Board()
    board.createBoard()
    # Qui commence
    engine = GameEngine(player1, player2)
    engine.whoStart(player1, player2)
    start = True
    while start:
        print('---------------------')
        board.showBoard()
        print('---------------------')
        dispo = True
        while dispo:
            # Input joueur
            line, column = list(map(int,input("Choose the line and column you want (put a space between them): \n").split(' ')))
            # Verification existance input dans case
            dispo = board.caseEmpty(line-1,column-1)
        # Ajout de l'input du joueur dans la case correspondante
        board.casePicked(line,column,engine.whoPlay())
        if board.checkLine():
            engine.whoWin()
            board.showBoard()
            start = False
        if board.checkColumn():
            engine.whoWin()
            board.showBoard()
            start = False
        if board.checkDiagonal():
            engine.whoWin()
            board.showBoard()
            start = False
        if board.isBoardFull():
            print('---------')
            print("DRAW !")
            print('---------')
            board.showBoard()
            start = False
        # Changement de tour
        engine.playTurn()

