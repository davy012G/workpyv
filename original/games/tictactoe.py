#File name: tictactoe.py
#Format: Camel Case
import random as r

refPoints = {"r":"row", "c":"column", "d":"diagonal"}
playerDict = {"X":"", "O":""}
autoName = "!C¬~|\\54^"

#Note that number in the referee function is being used for the GUI version of this game. - Done...

def vacancy(board, inputInt):
    return board[inputInt] == " "

def referee(board, inputStr):
    reason = ""
    boolean = False
    number = 9
    for i in range(3):
        row_i = i*3
        if board[row_i] == board[row_i+1] == board[row_i+2] == inputStr: #Row
            reason = "r"
            boolean = True
            number = i
        elif board[i] == board[i+3] == board[i+6] == inputStr: #Column
            reason = "c"
            boolean = True
            number = i
        elif board[i] == board[4] == board[8-i] == inputStr: #Diagonal
            reason = "d"
            boolean = True
            number = i
    return reason, boolean, number

def easy(player):
    #Will use this as the runner for the Easy class
    pick = 0
    numberOne = r.randrange(0, 9)
    numberTwo = r.randrange(0, 9)

    if player == "X":
        pick = abs(numberOne - numberTwo)
    else:
        pick = abs(numberOne + numberTwo)

    return pick%9

def hard(player):
    #Will use this as the runner for the Hard class
    pick = 0
    numberOne = r.randrange(0, 9)
    numberTwo = r.randrange(0, 9)

    if player == "X":
        pick = (numberOne * 2)-10
    else:
        pick = (numberTwo * 4)//2
    
    return pick%9

class TicTacToe:
    
    #Belongs to this class only
    playerDict = {"X":"", "O":""}
    autoName = "!C¬~|\\54^"

    def __init__(self):
        """Tictactoe is a two-player game that is said to focus on sharpening mental abilities."""
        prompt = "What game would you be playing. \nInput m for man to man duel or \nEnter c for man to robot showdown \nHere:"
        difficulty = ["easy", "hard"] #Using this for only this function 
        tempLevel = input("Enter desired level %s: "%difficulty).lower()
        self.level = {True:tempLevel, False:r.choice(difficulty)}[tempLevel in difficulty] #Global Function
        try:
            {"m":self.nameCollection, "c":self.appointSecondPlayer}[input(prompt).lower()]()
        except KeyError:
            print("We do not understand this code: ")
        self.gameDuel()

    def nameCollection(self):
        firstPlayer = input("Enter the name of Player X: ")
        self.playerDict["X"] = firstPlayer
        secondPlayer = input("Enter the name of Player O: ")
        self.playerDict["O"] = secondPlayer

    def appointSecondPlayer(self):
        characters = ["X", "O"]
        nameEntry = input("Enter Your Name: ")
        try:
            charChoice = input("Which Player do you want to play as ['x','o','r']: ").upper()[0]
            decide = {True: charChoice, False:r.choice(characters)}[charChoice in characters]
            autoDecide = {"X":"O", "O":"X"}[decide]
        #R means pick at random
        except (KeyError, IndexError):
            decide, autoDecide = characters
        self.playerDict[decide] = nameEntry
        self.playerDict[autoDecide] = self.autoName

    def playFormat(self, board):
        #Assuming that the board has a complete nine elements
        for i in range(3):
            r = 3*i
            print(f"|{board[0+r]}|{board[1+r]}|{board[2+r]}|")

    def request(self):
        #Same 
        match input("Do you want to continue this game: ").lower():
            case "yes":
                print("Okay let's play again.")
                TicTacToe()
            case "no":
                print("Alright, See you later.")
            case _:
                print("This command is not recognized.")

    def reset(self, board):
        #Instead of using the reset function i'll just use the layout list 
        rack = board
        for r in range(len(rack)):
            rack[r] = " "
        return rack

    def inputChecker(self, nameOfplayer, player, mode):
        if nameOfplayer == self.autoName:
            if mode == "easy":
                cellNo = easy(player)
            else:
                cellNo = hard(player)
        else:
            try:
                cellNo = (int(input("Enter the location of %s: "%player))%9) - 1
            except ValueError:
                cellNo = 1 # 1 As default number, ain't that very strange
        
        return cellNo

    def gameDuel(self):
        board = [" " for i in range(9)]
        turns = 0
        spacesFilled = 0
        print("Welcome to DPJE's Tictactoe game.")
        self.playFormat(board)

        while spacesFilled < 9:
            player = ["X", "O"][turns%2]
            plInput = self.inputChecker(self.playerDict[player], player, self.level)

            if vacancy(board, plInput) == True:
                #If the cell is open
                board[plInput] = player
                self.playFormat(board)
                print("%s just played %s to cell number %s \n"%(self.playerDict[player], player, plInput))
                reason, result, number = referee(board, player)
                spacesFilled += 1
                turns += 1
                if result == True:
                    print("{} won, Nice play - {} win from cell {}".format(player, refPoints[reason], number))
                    self.request()
                    break
            else:
                #If the cell is already taken
                print("Sorry but this cell is already taken. Let's try that again, shall we?")
            
        else:
            print("Tie, Better luck next time.")
            self.request()

