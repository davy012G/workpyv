#File name: towerOfHanoi.py
#Format: Camel Case

import random as r

UNIDICT = {"a":0, "b":1, "c":2} #@Dictionary

mix = lambda listItem: r.sample(listItem, k = len(listItem)) #@Function

def shuffle(menu):
    """shuffles any list item amd returns a shuffled list with all it's elements still intact.
    another miscellaneous function as i have seen a better one - r.sample(menu,k=len(menu))"""
    add = [] 
    sets = menu

    while len(sets) > 0:
        length = len(sets)
        number = r.randrange(0,length)
        section = sets[number]
        add.append(section)
        del section

    return add

def threeGrouping(number):
    """returns a three-element list item of which the sum of all its elements equals the number."""
    menu = [0,0,0]

    for i in range(number):
        menu[i%3] += 1

    return menu

def twoGrouping(number):
    """a miscellaneous list-returning function - could be useful."""
    menu = [0,0,0]

    for i in range(number):
        menu[i//3] += 1 #This could spring up some pretty interesting errors though

    return menu

def listGrouper(number):
    tower = []

    for i in range((number+2)//3):
        no = i*3
        tower.append(list(range(no+1, min(number+1,no+4))))

    return tower

def indivRandomise(number):
    individuals = []

    for l in listGrouper(number):
        individuals.append(r.sample(l,k=len(l)))

    return individuals

def ascendOrder(charPos, number):
    """Reason for name: To indicate that it shows if all the numbers in a certain function are in ascending order."""
    #charPos is there to replace board and pos
    record = 0
    no = number - 1

    for n in range(no):
        if charPos[n] == charPos[n+1]-1:
            record += 1

    return record == no

def arrange(number):
    """The arrangements..."""
    charList = mix(threeGrouping(number))
    randList = indivRandomise(number)
    pallete = [["|" for _ in range(number)] for w in range(3)]
    coords = [number-i for i in charList] #coords as in coordinates or locations
    arrangeList = [0 for i in range((number+2) // 3)]

    for s in range(3):
        for i in range(charList[s]):
            pallete[s][i - charList[s]] = randList[i][arrangeList[i]]
            arrangeList[i] += 1

    del charList, randList
    return pallete, coords

#def parMove(rack, posOne, posTwo, location):
#    """parMove means parameter for movement across the several rows."""
#    return board[posOne][location[posTwo]] < board[posTwo][location[posTwo]]

class TowerOfHanoi_Text:

    def __init__(self, integer: int) -> None:
        self.main(integer)

    def printBoard(self, board, no):
        for b in range(no):
            print("  _   _   _  ")
            print(f" |{board[0][b]}| |{ board[1][b]}| |{ board[2][b]}| ")
            print("  _   _   _  ")

    def request(self):
        #This is the same in all files in games folder
        #question = input("Would you like to continue this game: ")

        match input("Would you like to continue this game: ").lower():
            case "yes":
                return True
            case "no":
                return False
            case _:
                self.request()
                
    def changePos(self, board, location, posOne, posTwo):
        character =  board[posOne][ location[posOne]]
        board[posOne][ location[posOne]] = "|"
        location[posOne] += 1
        location[posTwo] -= 1
        board[posTwo][ location[posTwo]] = character

    def main(self, number):
        board, location = arrange(number)
        running = True

        self.printBoard(board, number)
        print("Welcome to Tower Of Hanoi [DPJE Version] \nInput A, B or C... ")

        while running:
            try:
                p1 = input("Input the first position: ")
                posOne = UNIDICT[p1[0].lower()]
            except ValueError:
                posOne = int(p1) % 4

            try:
                p2 = input("Input the second position: ")
                posTwo = UNIDICT[p2[0].lower()]
            except ValueError:
                posTwo = int(p2) % 4

            #Reason for split error handling is for control of the input

            #If the second cell is empty just fill it without options
            if  location[posTwo] >= number:
                self.changePos(board, location, posOne, posTwo)
            #But if the first cell happens to be empty you need to alert the player
            elif  location[posOne] >= number:
                print("Looks like that cell is empty.")
            #Else you can carry out the normal things you would carry out in the tower of hanoi game
            else:
                if  board[posOne][ location[posOne]] <  board[posTwo][ location[posTwo]]:
                    self.changePos(board, location, posOne, posTwo)
                else:
                    print("The number below is lesser than your input number.")
        
            self.printBoard(board, number)
            
            #The winning check algorithm;

            if  board[posTwo].count("|") == 0:
                #If the cell is full and...
                if ascendOrder( board[posTwo], number) == True:
                    #All the numbers are arranged in ascending order then...
                    print("You win, Hurray!")
                    if self.request():
                        print("Alright shall we proceed?")
                        self.main(number)
                    else:
                        print("Closing Tower_Of_Hanoi program...")
                        running = False
                else:
                    #The numbers are not arranged in the ascending order then... 
                    print("Cell %s is full but not in ascending order..." % board[posTwo])

        print("Tower of Hanoi program has been closed;")
