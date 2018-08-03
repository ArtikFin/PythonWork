import random
class game:
    player = []
    computer = []
    computerView = []
    score = 0
    computerScore = 0
    def populateBoardList():
        "This creates a list of zeros and ones to be used for the board"
        board = []
        base = [1,1,0,0,0,0,0,0,0]
        for n in range(9,0,-1):
            temp = random.randint(0,n-1)
            board.append(base[temp])
            del base[temp]
        return board
    def createBoards():
        "This recategorizes the lists into three lists, a list within a list kinda thing"
        tempPlayer = game.populateBoardList()
        tempComputer = game.populateBoardList()
        game.computerView = [[0,0,0],[0,0,0],[0,0,0]]
        game.player = [tempPlayer[0:3],tempPlayer[3:6],tempPlayer[6:9]]
        game.computer = [tempComputer[0:3],tempComputer[3:6],tempComputer[6:9]]
    def displayBoard():
        "This displays the board in a 3x3 format to display for the player"
        for n in range(0,3):
            print(game.player[n])
    def displayEnemyBoard():
        "This displays the visible enemy board in a 3x3 format to display for the player"
        for n in range(0,3):
            print(game.computerView[n])
    def startGame():
        "This runs the game"
        game.score = 0
        game.computerScore = 0
        game.createBoards()
        print("\nWelcome to Battleship\n\nThis is your board for this match:")
        game.displayBoard()
        while game.score != 2 and game.computerScore !=2:
            game.playerTurn()
            game.enemyTurn()
        game.endGame()
    def playerTurn():
        "This is the players turn, they select a number between 0 and 2 for both row and column in order to score a hit"
        "A hit is marked with a 4 while a miss is marked with 3. game.score goes up one for a hit"
        print("\nWhere do you take aim?\n")
        try:
            temp1 = int(input("Row(0-2): "))
            temp2 = int(input("Column(0-2): "))
            if game.computer[temp1][temp2] == 1:
                print("\nHit! Enemy's current board:")
                game.computerView[temp1][temp2] = 4
                game.displayEnemyBoard()
                game.score += 1
            else:
                print("\nMiss! Enemy's current board:")
                game.computerView[temp1][temp2] = 3
                game.displayEnemyBoard()
        except:
            print("\nThis is not a valid response. Were you trying to exit?")
            temp3 = input("")
            if temp3 == "yes":
                game.endGame()
            else:
                game.playerTurn()
        f = input("\nEnemy's Turn")
    def enemyTurn():
        "This is the computer's turn to do the same"
        try:
            temp1 = random.randint(0,2)
            temp2 = random.randint(0,2)
            if game.player[temp1][temp2] == 4 or game.player[temp1][temp2] == 3:
                game.enemyturn()
            elif game.player[temp1][temp2] == 1:
                print("\nHit! Your current board:")
                game.player[temp1][temp2] = 4
                game.displayBoard()
                game.computerScore += 1
            else:
                print("\nMiss! Your current board:")
                game.player[temp1][temp2] = 3
                game.displayBoard()
        except:
            game.enemyTurn()
    def endGame():
        if game.score == 2:
            print("\nYou win!")
        else:
            print("\nYou lose!")
        x = input("\nWould you like to play again?: ")
        if x.lower() == "yes":
            print("\n")
            game.startGame()
