#File Name: chess.py
#Format: Camel Case

TURNDICT = ([("Pw", "Bw", "Rw", "Kw", "Qw", "Lw", "Lb"), "White", "player-white"], [("Pb", "Bb", "Rb", "Kb", "Qb", "Lb", "Lw"), "Black", "player-black"])
AUTONAME = "!C¬~|\\54^"

def strToint(integer:str, default:int = 0) -> int:
    try:
        expectedNum = int(integer)
    except ValueError:
        expectedNum =  default

    return expectedNum

def decimalConv(coordinates:str, default:tuple = (0,0)) -> tuple:
    try:
        x, y = [int(i) for i in list(coordinates.split(sep= ":"))]
    except ValueError:
        x, y = default

    return x, y

def difference(fNum, sNum):
    if fNum > sNum:
        value = max(fNum, sNum)
    else:
        value = min(fNum, sNum)

    return value

def template(numOne, numTwo):
    n = numOne - numTwo
    if n == 0:
        integer = 0
    else:
        integer = (n*-1)//abs(n)
    return integer

class Public:

    def nameCollection(self):
        playerWhite = input("Enter the name of Player White: ")
        playerBlack = input("Enter the name of Player Black: ")
        if playerWhite == playerBlack or playerWhite == AUTONAME and playerBlack == AUTONAME:
            print("The names should not be recursive and choose a name different from the computer name.")
            self.nameCollection()
        else:
            print("Player 1: %s\nPlayer 2: %s\n"%(playerWhite, playerBlack))
            TURNDICT[0][2] = playerWhite
            TURNDICT[1][2] = playerBlack

    #--These Functions will be dormant till the next update--

    def selectMode(self):
        match input("Enter\nm for man to man\nc for computer to man\n:").lower():
            case "m":
                print("Man to Man duel")
                self.nameCollection()
            case "c":
                print("Computer to Man duel")
                self.selectColor()
            case _:
                print("Let's try this again.")
                self.selectMode()

    def selectColor(self):
        color = {"white":0, "black":1}[input("Enter either white or black: ")]
        TURNDICT[color][2] = input("Enter Your name: ")
        TURNDICT[(color-1)][2] = AUTONAME

# Numerical Coordinates Part

class NumericCoord: # Done
    """x - Start, y - Stop, turn - <specified number remainder>"""

    def bishopMove(self, x, y):
        return abs(x - y)%9 == 0 or abs(x - y)%7 == 0

    def rookieMove(self, x, y):
        return abs(x - y)%8 == 0 or x//8 == y//8

    def knightMove(self, x, y):
        return abs(x - y) in [6, 10, 15, 17]

    def queenMove(self, x, y):
        return self.bishopMove(x, y) or self.rookieMove(x, y)

    def kingMove(self, x, y):
        return abs(x - y) in [7, 8, 9] or x//8 == y//8

    def punZero(self, x, y, board): #Pun white
        return x - y == -8 or (7 < x < 16 and x - y == -16) or (x - y in [-7, -9] and board[y] != "  ")

    def punOne(self, x, y, board): #Pun black
        return x - y == 8 or (47 < x < 56 and x - y == 16) or ( x - y in [7, 9] and board[y] != "  ")

    #def promotion(self, x, board): #@Public Function
    #    return (7 < x < 16 and board[x] == "Pw") or (47 < x < 56 and board[x] == "Pb")

    def teamwork(self, y, board, turn): #@Public Function
        return board[y] not in TURNDICT[turn][0]

    def movement(self, x, y, board): #@Public Function
        #Movement
        if board[x] == "Pw":
            moveFreedom = self.punZero(x, y, board)
        elif board[x] == "Pb":
            moveFreedom = self.punOne(x, y, board)
        elif board[x] == "Bw" or board[x] == "Bb":
            moveFreedom = self.bishopMove(x, y)
        elif board[x] == "Rw" or board[x] == "Rb":
            moveFreedom = self.rookieMove(x, y)
        elif board[x] == "Kw" or board[x] == "Kb":
            moveFreedom = self.knightMove(x, y)
        elif board[x] == "Qw" or board[x] == "Qb":
            moveFreedom = self.queenMove(x, y)
        elif board[x] == "Lw" or board[x] == "Lb":
            moveFreedom = self.kingMove(x, y)
        else:
            moveFreedom = False

        return moveFreedom

    def checkObstruction(self, x, y, step, board):
        """This function returns whether your piece is being obstructed while"""
        blocked = False
        for i in range(x, y, step):
            if board[i] != "  ":
                blocked = True
                break

        return blocked

    def checkObstructor(self, x, y, step, board):
        """This one returns the piece that obstructs your piece or character."""
        piece = ""
        for i in range(x, y, step):
            if board[i] != "  ":
                piece = board[i]
                break
            
        return piece

    def queenLogic(self, x, y, listOfInt, elseNum):
        """This function is called queenLogic because it was originally made for the queen chess piece herself."""
        number = elseNum
        for l in listOfInt:
            if abs(x - y) % l == 0:
                number = l
        return number

    def blockage(self, x, y, board): #@Public Function
        """Should be called after movement is successful. Very movement-dependent"""
        if board[x] in ["Bw", "Bb"]:
            blockValue = self.checkObstruction(x, y, {True: 7, False: 9}[abs(x - y)%7 == 0], board)
        elif board[x] in ["Rw", "Bb"]:
            blockValue = self.checkObstruction(x, y, {True: 8, False: 1}[abs(x - y)%8 == 0], board)
        elif board[x] in ["Qw", "Qb"]:
            blockValue = self.checkObstruction(x, y, self.queenLogic(x, y, [7, 8, 9], 1), board)
        else:
            blockValue = False

        return blockValue

    #def enemyKill(self, x, y, board, turn): #@Public Function
    #    if board[x] in ["Bw", "Rw", "Kw", "Qw", "Lw", "Bb", "Rb", "Kb", "Qb", "Lb"]:
    #        killPermit = self.teamwork(y, turn)
    #    else:
    #        if board[x] == "Pw":
    #            killPermit = x - y in [-7, -9] and self.teamwork(y, turn) == True and board[y] != "  "
    #        elif board[x] == "Pb":
    #            killPermit = x - y in [7, 9] and self.teamwork(y, turn) == True and board[y] != "  "
    #        else:
    #            killPermit = False
    #    
    #    return killPermit

    def transform(self, y, board):#@Public Function
        """Also movement dependent, make sure to use after you have set the movement criteria right.
        This function specifies when a pun has reached the other end of the board.
        Supposed to be transform(self, x, y, board) but for dependency reasons we just use this """
        return (board[y] == "Pb" and -1 < y < 8) or (board[y] == "Pw" and 55 < y < 64) #Instead of
        #return (board[x] == "Pb" and -1 < y < 8) or (board[x] == "Pw" and 55 < y < 64)

    def loopObstruct(self, listOfTuples):
        """Made specifically for the function checkMate. To be only used with it.
        loopObstruct means obstructions in a looping system."""
        boolean = False
        piece = " "
        
        for t in listOfTuples:
            if self.checkObstruction(*t) == True:
                boolean = True
                piece = self.checkObstructor(*t)
                break
        
        return boolean, piece

    def knightStand(self, x, board, turn):
        boolean = False
        knights = ("Kw", "Kb")

        for loop in [6, 10, 15, 17]:
            if x - loop > 0 and (x//8) - ((x-loop)//8) == (loop//11) + 1 and board[x-loop] == knights[turn]:
                boolean = True
            elif x + loop < 64 and (x//8) - ((x+loop)//8) == -((loop//11)+1) and board[x+loop] == knights[turn]:
                boolean = True
        
        return boolean

    def checking(self, l, board, turn): #@Public Function
        """This function focuses on the Leaders or Kings alone
        Remember to save a space where the kings whereabouts will be monitored."""
        #l - This is the place where the king is located 

        diagonal, pieceDiagonal = self.loopObstruct([(l, l-(9*min(l%8, l//8)), 9, board), (l, l+(9*min(7-(l%8), l//8)), 9, board), (l, l-(7*min(7-(l%8), l//8)), 7, board), (l, l+(7*min(l%8, l//8)), 7, board)])
        straight, pieceStraight = self.loopObstruct([(l, l+(8*(7-(l//8))), 8, board), (l, l-(8*(l//8)), 8, board), (l, l+(7-(l%8)), 1, board), (l, l-(l%8), 1, board)])

        return (diagonal == True and pieceDiagonal in [["Bw","Qw"],["Bb", "Qb"]][turn]) or (straight == True and pieceStraight in [["Rw","Qw"],["Rb","Qb"]][turn]) or self.knightStand(l, board, turn)

class RunNumerical(Public): 

    def __init__(self):
        self.kingsLocation = {"Lw":4, "Lb":60}
        self.board = ["  " for i in range(64)]

        #Arranging players
        self.board[0:8] = ["Rw","Kw","Bw", "Qw","Lw","Bw","Kw","Rw"]
        self.board[8:16] = ["Pw"]*8
        self.board[48:56] = ["Pb"]*8
        self.board[56:] = ["Rb","Kb","Bb","Qb","Lb","Bb","Kb","Rb"]
        
        #Get some things set well
        self.nameCollection()
        self.printBoard()
        numC = NumericCoord()
        turns = 0

        while True:
            step = turns % 2

            print("\n%s pick your own"%TURNDICT[step][-1])

            x = strToint(input("Enter the first location: "))
            y = strToint(input("Enter the second location: "))

            print("\n") 

            if self.board[x] != "  " and self.board[x] in TURNDICT[step][0]:
                print("Checking if your input is correct...")
                if numC.movement(x, y, self.board) == True: #Movement
                    print("Checking for obstructions...")
                    if numC.blockage(x, y, self.board) == False: #Blocking
                        print("Checking if the next character being put upon is one of your teammates...")
                        if numC.teamwork(y, self.board, step) == True: #Enemy Kills
                            print("'%s' <Ontop> '%s'"%(self.board[x], self.board[y]))
                            print("Checking if your king is being checked...")

                            if numC.checking(self.kingsLocation[TURNDICT[step][0][5]], self.board, step) == False: #Checking
                                self.changePieceLocation(x, y)
                                turns += 1
                                print("Done")
                            else:
                                print("Your king is being spied on.")

                            if numC.transform(y, self.board) == True:
                                print("Congratulation to team %s, %s has entered the promotion zone."%(TURNDICT[step][1], self.board[y]))
                                self.startTransformation(y, step)
                        else:
                            print("You can't go against your friends. '%s' - '%s'"%(self.board[x], self.board[y]))
                    else:
                        print("%s have been blocked by a piece."%self.board[x])
                else:
                    print("%s wanted to go to %s."%(self.board[x], y))
            else:
                print("Your first piece pick was %s."%self.board[x])

    def startTransformation(self, y, turn):#Belongs to runNumerical
        turnTuple = TURNDICT[turn][0][1:5]
        codeInput = input(f"Enter one these codes - {turnTuple}: ")

        if codeInput in turnTuple:
            print("'%s' picked '%s'"%(TURNDICT[turn][-1], codeInput))
            self.board[y] = codeInput
        else:
            print("Let's try that again.")
            self.startTransformation(y, turn)
        print("\n")

    def changePieceLocation(self, x, y):#Belongs to runNumerical
        self.board[y] = self.board[x]
        self.board[x] = "  "

        if self.board[x] in ["Lw", "Lb"]:
            self.kingsLocation[self.board[x]] = y
        self.printBoard()

    def printBoard(self):# belongs to runNumerical
        for i in range(8):
            for j in self.board[8*i : 8*(i+1)]:
                print("|"+j+"|", end="")
            print("\n")

# Cartesian Coordinates Part

class CartesianCoord: # Copy of the NumericCoord class
    
    def bishopMove(self, x1, y1, x2, y2):
        return abs(x1-x2) == abs(y1-y2)

    def rookieMove(self, x1, y1, x2, y2):
        return (x1 == x2 and y1 != y2) or (x1 != x2 and y1 == y2)

    def knightMove(self, x1, y1, x2, y2):
        return (abs(x1-x2), abs(y1-y2)) in ((2,1), (1,2))
    
    def queenMove(self, x1, y1, x2, y2):
        return self.bishopMove(x1, y1, x2, y2) or self.rookieMove(x1, y1, x2, y2)

    def punZero(self, x1, y1, x2, y2,board):
        return (y1 - y2 == -1 and x1 == x2 and board[x2][y2]=="  ") or (y1-y2 == x1-x2 == -1 and board[x2][y2] != "  ") or (y1 == 1 and y1 - y2 == -2 and board[x2][y2]=="  ")
    
    def punOne(self, x1, y1, x2, y2, board):
        return (y1 - y2 == 1 and x1 == x2 and board[x2][y2]=="  ") or (y1-y2 == x1-x2 == 1 and board[x2][y2] != "  ") or (y1 == 6 and y1 - y2 == 2 and board[x2][y2]=="  ")

    def kingMove(self, x1, y1, x2, y2):
        return abs(x1-x2) in (0, 1) and abs(y1-y2) in (0, 1)

    def movement(self, x1, y1, x2, y2, layout):
        if layout[x1][y1] == "Pw":
            boolean = self.punZero(x1, y1, x2, y2, layout)
        elif layout[x1][y1] == "Pb":
            boolean = self.punOne(x1, y1, x2, y2, layout)
        elif layout[x1][y1] in ("Rw", "Rb"):
            boolean = self.rookieMove(x1, y1, x2, y2)
        elif layout[x1][y1] in ("Bw", "Bb"):
            boolean = self.bishopMove(x1, y1, x2, y2)
        elif layout[x1][y1] in ("Qw", "Qb"):
            boolean = self.queenMove(x1, y1, x2, y2)
        elif layout[x1][y1] in ("Kw", "Kb"):
            boolean = self.knightMove(x1, y1, x2, y2)
        elif layout[x1][y1] in ("Lw", "Lb"):
            boolean = self.kingMove(x1,y1,x2,y2)
        else:
            boolean = False

        return boolean
    
    def teamwork(self, x2, y2, layout, turn):
        return layout[x2][y2] not in TURNDICT[turn]

    def checkObstruction(self, x1, y1, x2, y2, xStep, yStep, layout):
        """The layout is presumably the board(list[list]) everything else are integers (int)"""
        i = x1
        j = y1
        boolean = False
        condition = {True:abs(x1-x2), False:abs(y1-y2)}[max(abs(x1-x2),abs(y1-y2))==abs(x1-x2)] - 1
        #parOne - First Parameter, parTwo - Second Parameter, cond - Condition

        while condition > 0:
            i = difference(i + xStep, x2)
            j = difference(j + yStep, y2)
            condition -= 1

            if layout[i][j] != "  ":
                boolean = True
                break
        
        return boolean

    def checkObstructor(self, x1, y1, x2, y2, xStep, yStep, layout):
        """To be used when checkObstruction is confirmed."""
        i = x1
        j = y1
        boolean = False
        condition = {True:abs(x1-x2), False:abs(y1-y2)}[max(abs(x1-x2),abs(y1-y2))==abs(x1-x2)]
        #parOne - First Parameter, parTwo - Second Parameter, cond - Condition

        while condition > 0:
            i = difference(i + xStep, x2)
            j = difference(j + yStep, y2)
            condition -= 1

            if layout[i][j] != "  ":
                piece = layout[i][j]
                break
        
        return piece

    def blockage(self, x1, y1, x2, y2, layout): #Extremely movement-dependent
        if layout[x1][y1] in ("Bw", "Rw", "Qw", "Bb", "Rb", "Qb"):
            boolean = self.checkObstruction(x1, y1, x2, y2, template(x1, x2), template(y1, y2), layout)
        else:
            boolean = False

        return boolean

    def transform(self, x2, y2, layout):
        return (layout[x2][y2] == "Pw" and y2 == 7) or (layout[x2][y2] == "Pb" and y2 == 0)

    def loopObstruct(self, listOfTuples: list[tuple], layout):
        """Made specifically for the function checkMate. To be only used with it.
        loopObstruct means obstructions in a looping system."""
        boolean = False
        piece = " "
        
        for t in listOfTuples:
            if self.checkObstruction(*t, layout) == True: # type: ignore
                boolean = True
                piece = self.checkObstructor(*t, layout) # type: ignore
                break
        
        return boolean, piece

    def knightStand(self, lx, ly, layout, turn):
        boolean = False
        knights = ("Kw", "Kb")[turn]

        for v in ((2,1),(1,2),(-2,-1),(-1,-2),(1,-2),(-2,1),(2,-1),(-1,2)):
            x = lx + v[0]
            y = ly + v[1]
            if 0 < x < 8 and 0 < y < 8 and layout[x][y] == knights:
                boolean = True

        return boolean

    def checking(self, lx, ly, layout, turn):
        minimum = min(lx,ly)
        cross, pieceCross = self.loopObstruct([(lx,ly,min(0,lx),ly,-1,0), (lx,ly,max(7,lx),ly,1,0), (lx,ly,lx,min(0,ly),0,-1), (lx,ly,lx,max(7,ly),0,1)], layout)
        xBool, pieceX = self.loopObstruct([(lx,ly,lx-minimum,ly-minimum,-1,-1), (lx,ly,lx+minimum,ly+minimum,1,1), (lx,ly,lx-minimum,ly+minimum,-1,1), (lx,ly,lx+minimum,ly-minimum,1,-1)], layout)

        return (cross == True and pieceCross in (("Rw","Qw"),("Rb","Qb"))[turn]) or (xBool == True and pieceX in (("Bw","Qw"),("Bb","Qb"))[turn]) or self.knightStand(lx, ly, layout, turn) == True

class RunCartesian(Public):

    def __init__(self):
        self.kingsLocationC = {"Lw":(0,4), "Lb": (4, 7)}
        self.layout = [["  " for i in range(8)] for j in range(8)] #[x, y]

        #Arranging players
        lookSheet = (["Rw","Kw","Bw","  ","Lw","Bw","Kw","Rw"], ["Pw"]*8, ["Pb"]*8, ["Rb","Kb","Bb","Qb","Lb","Bb","Kb","Rb"])
        self.layout[7][4] = "Qw"
        for i, j in zip((0,1,2,3), (0,1,6,7)):
            for k in range(8):
                self.layout[k][j] = lookSheet[i][k]

        #Set the remaining requirements for the chess game
        #self.nameCollection()
        self.printLayout()
        print("Welcome to the Cartesian - Chess\nMake sure the coordinates are seperated from each other by a colon.")
        rowCol = CartesianCoord()
        turns = 0

        while True:

            step = turns % 2

            print("\n%s pick your own"%TURNDICT[step][-1])

            xFirst, yFirst = decimalConv(input("Enter the first x and y coordinates: "))
            xSecond, ySecond = decimalConv(input("Enter the second x and y coordinates: "))

            print("\n") 

            if self.layout[xFirst][yFirst] != "  " and self.layout[xFirst][yFirst] in TURNDICT[step][0]:
                print("Checking if your input is correct...")
                if rowCol.movement(xFirst, yFirst, xSecond, ySecond, self.layout) == True: #Movement
                    print("Checking for obstructions...")
                    if rowCol.blockage(xFirst, yFirst, xSecond, ySecond, self.layout) == False: #Blocking
                        print("Checking if the next character being removed is one of your teammates...")
                        if rowCol.teamwork(xSecond, ySecond, self.layout, step) == True: #Enemy Kills
                            print("'%s' <Ontop> '%s'"%(self.layout[xFirst][yFirst], self.layout[xSecond][ySecond]))
                            print("Checking if your king is being checked...")

                            if rowCol.checking(*self.kingsLocationC[TURNDICT[step][0][5]], self.layout, step) == False: #Checking
                                self.changePieceLocation(xFirst, yFirst, xSecond, ySecond)
                                turns += 1
                                print("Done")
                            else:
                                print("Your king is being spied on.")

                            if rowCol.transform(xSecond, ySecond, self.layout) == True:
                                print("Congratulation to team %s, %s has entered the promotion zone."%(TURNDICT[step][1], self.layout[xSecond][ySecond]))
                                self.startTransformation(xSecond, ySecond, step)
                        else:
                            print("You can't go against your friends. '%s' - '%s'"%(self.layout[xFirst][yFirst], self.layout[xSecond][ySecond]))
                    else:
                        print("%s is being blocked by a piece."%self.layout[xFirst][yFirst])
                else:
                    print("%s wanted to go to %s:%s."%(self.layout[xFirst][yFirst], xSecond, ySecond))
            else:
                print("Your first piece pick was %s."%self.layout[xFirst][yFirst])

    def startTransformation(self, x2, y2, turn):
        turnTuple = TURNDICT[turn][0][1:5]
        codeInput = input(f"Enter one these codes - {turnTuple}: ")

        if codeInput in turnTuple:
            print("'%s' picked '%s'"%(TURNDICT[turn][-1], codeInput))
            self.layout[x2][y2] = codeInput
        else:
            print("Let's try that again.")
            self.startTransformation(x2, y2, turn)
        print("\n")

    def changePieceLocation(self, x1, y1, x2, y2):
        self.layout[x2][y2] = self.layout[x1][y1]
        self.layout[x1][y1] = "  "

        if self.layout[x2][y2] in ("Lw","Lb"):
            self.kingsLocationC[self.layout[x2][y2]] = (x2, y2)
        self.printLayout()

    def printLayout(self):
        for i in range(8):
            for j in range(8):
                print("|"+self.layout[j][i]+"|", end="")
            print("\n")

    #self.request()

def main_():
    print("Welcome to Chess")
    u_input = input("Input [e to Exit, n for Numerical and c for Cartesian ]: ")
    match u_input:
        case "n":
            RunNumerical()
        case "c":
            RunCartesian()
        case "e":
            print("Exiting...")
        case _:
            print("Looks like you typed in the wrong code, let's go again...")
            main_()
