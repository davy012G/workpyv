#File name: eyeTest.py
#Format: Camel Case

import random as r
import toolKit.customTools as c
#Once i come back i will address the issue of the verbose BoardSet

RCHOICE = ["brick", "zRow", "zCol", "diagonal", "octagon", "hexagon", "heptagon", "square", "lCol", "lRow", "cross", "block", "triangle", "pentagon"]
alphabetList = list(c.LETTERS)

"""def letterGen(length):
    \"""This function is made for the sole aim of generating letters based on the length needed...\"""
    return [c.LETTERS[a] for a in getNumbers(length, 0, len(c.LETTERS))]"""

def setOfCoords(coords: list, length: int):
    return set([c.AsciiCoordinates().misCoordsTwoOutput(g, length) for g in coords])

def groupNumbers(array, iterable):
    m = []
    i = 0
    for r in iterable:
        m.append(array[i:i+r])
        i += r
    return m

def getNumbers(listLength, rangeOne, rangeTwo):
    limit = listLength #r.randrange((listLength*2)+1, (listLength*3)+1)
    integers = []

    while limit > 0:
        number = r.randrange(rangeOne, rangeTwo)
        if number not in integers:
            integers.append(number)
            limit -= 1
    
    return integers

def letterGen(length):
    """This function is made for the sole aim of generating letters based on the length needed..."""
    return [c.LETTERS[a] for a in getNumbers(length, 0, len(c.LETTERS))]

def determine(listLength, rangeOne, rangeTwo):
    return [r.randrange(rangeOne, rangeTwo) for f in range(listLength)]

def showCoordinates(string):
    coords = []
    characters = ""

    for s in string:
        if s == ",":
            coords.append(characters)
            characters = ""
        elif s == " ":
            continue
        else:
            characters += s
    #If all goes well there is a possibilty that the last character will be left so definitely this one will
    #catch it...
    if len(characters) > 0:
        coords.append(characters)

    return set(coords)

class BoardSet:

    """This class is closely affiliated with the EyeTest Class. This class is a numerical class meaning it operates
    by releasing numbers or list of numbers.
    When iterating through with elements dont forget to use the remainder theory.
    addition to notes: step being = min(xMax, step) is finally debunked as there is a better way to do it now...
    and that's the same remainder theory.
    """

    def rShape(self, number, xMax, step):
        #randomShape
        return self.shape_outline(self.pick((xMax, -xMax, xMax-1, -xMax+1, 1, -1, xMax+1, -xMax-1), r.randrange(4,10,2)), step, number)

    def triangle(self, number, xMax, step): #*
        # Triangle's good to go
        step = min(xMax, step)
        l= []
        for s in range(step):
            l += [number + ((xMax-1)*s), number + ((xMax-1)*(step-1)) + s, number + ((xMax+1)*s), number + ((xMax+1)*(step-1)) - s]
        return l

    def triangleInv(self, number, xMax, step): #*
        # TriangleInverse's good to go
        step = min(xMax, step)
        l= []
        for s in range(step):
            l += [number - ((xMax-1)*s), number - ((xMax+1)*s), number - ((xMax+1)*(step-1)) + s, number - ((xMax-1)*(step-1)) - s]
        return l

    def zCol(self, number, xMax, step):
        # ZigZagCol's good to go
        l= []
        i = 0
        n = number
        step = min(xMax, step) - 1
        pointerZ = ((xMax+1, xMax-1), (xMax-1, xMax+1), (-xMax+1, -xMax-1), (-xMax-1, -xMax+1))
        identity = {True:0, False:1}[xMax//2 >= number%xMax] + {True:0, False:2}[xMax//2 >= number//xMax]

        while i//step < xMax//step:
            l.append(n)
            n += pointerZ[identity][(i//step)%2]
            i += 1

        return l

    def zRow(self, number, xMax, step):
        # ZigZagRow's good to go
        l= []
        i = 0
        n = number
        step = min(xMax, step) - 1
        pointerZ = ((xMax+1, -xMax+1), (xMax-1, -xMax-1), (-xMax+1, xMax+1), (-xMax-1, xMax-1))
        identity = {True:0, False:1}[xMax//2 >= number%xMax] + {True:0, False:2}[xMax//2 >= number//xMax]

        while i//step < xMax//step:
            l.append(n)
            n += pointerZ[identity][(i//step)%2]
            i += 1

        return l

    def lCol(self, number, xMax, step): #*
        # LineColumn's good to go
        step = min(xMax, step)
        l= []
        for s in range(step):
            l += [number + (s*xMax), (number+1) + (s*xMax)]
        return l

    def lColRev(self, number, xMax, step): #*
        # LineRowReverse's good to go
        step = min(xMax, step)
        l= []
        for s in range(step):
            l += [number - (s*xMax), (number+1) - (s*xMax)]
        return l

    def lRow(self, number, xMax, step): #*
        # LineRow's good to go
        step = min(xMax, step)
        l= []
        for s in range(step):
            l += [number + s, number + xMax + s]
        return l

    def lRowRev(self, number, xMax, step): #*
        # LineRowReverse's good to go
        step = min(xMax, step)
        l= []
        for s in range(step):
            l += [number - s, number + xMax - s]
        return l

    def block(self, number, xMax, step):
        return self.rShape(number, xMax, step)

    def octagon(self, number, xMax, step):
        #octagon
        return self.shape_outline((xMax-1, xMax, xMax+1, 1, -xMax+1, -xMax, -xMax-1, -1), step, number)

    def cross(self, number, xMax, step): #*
        # Cross's good to go
        step = min(xMax, step)
        l= []
        for s in range(step):
            l += [number + (xMax*s), number + s, number - (xMax*s), number - s]
        return l

    def diagonal(self, number, xMax, step): #*
        # Diagonal's good to go
        step = min(xMax, step)
        l= []
        for s in range(step):
            l += [number + ((xMax+1)*s), number + ((xMax-1)*s), number - ((xMax+1)*s), number - ((xMax-1)*s)]
        return l

    def hexagon(self, number, xMax, step):
        #hexagon
        return self.shape_outline((xMax-1, xMax, xMax+1, -xMax+1, -xMax, -xMax-1), step, number)

    def square(self, number, xMax, step): #*
        # Square's good to go
        step = min(xMax, step)
        l= []
        for s in range(step):
            l += [number + s, number + step-1 + (xMax*s), number + (xMax*s), number + (xMax*step) + s]
        return l

    def squareInv(self, number, xMax, step): #*
        # SquareInverse's good to go
        step = min(xMax, step)
        l= []
        for s in range(step):
            l += [number - s, number - (step-1) - (xMax*s), number - (xMax*s), number - (xMax*step) - s]
        return l

    def brick(self, number, xMax, step):
        return self.rShape(number, xMax, step)

    def heptagon(self, number, xMax, step):
        #heptagon
        return self.shape_outline((xMax-1, xMax-1, xMax, xMax+1, 1, 1, -xMax+1, -xMax, -xMax-1, -xMax-1), step, number)
    
    def pentagon(self, number, xMax, step):
        #pentagon
        return self.shape_outline((xMax-1, xMax, 1, 1, -xMax, -xMax-1), step, number)
    
    def shape_outline(self, input_tuple, step, number):
        l = []
        n = number

        for s in input_tuple:
            for j in range(step):
                l.append(n+(s*j))
            n += s * (step-1)

        return l

    def pick(self, data, noOfItems):
        #data is a list
        tempStorage = [] #Temporary Storage
        limit = noOfItems

        while limit > 0:
            temp = r.choice(data)
            if temp not in tempStorage:
                tempStorage.append(temp)
                limit -= 1

        return tempStorage

class EyeTest: # Will be done by next week

    default = 2

    def __init__(self, level):
        #Variables
        self.level = level
        number = self.lNumber(level)
        noOfSpaces = r.randrange(9+(3*number), 11+(3*number))
        noOfBackground = 1
        noOfConfusers = r.randrange((2*number)-1, (2*number)+1)
        noOfMisplacements = r.randrange(2*number, (2*number)+2)
        shapeFormat = r.choice(RCHOICE)
        noOfTries = 0
        #Arrays
        confArray = determine(noOfConfusers, (2*number)-1, (2*number)+1)
        mispArray = determine(noOfMisplacements, (3*number)-1, (3*number)+2)
        sumOfLengths = noOfConfusers + noOfMisplacements + noOfBackground + 1 
        sumOfArrays = sum(confArray) + sum(mispArray)
        letterArray = groupNumbers(letterGen(sumOfLengths), (noOfBackground, noOfConfusers, noOfMisplacements))
        spaceLineUp = groupNumbers(getNumbers(sumOfArrays, 0, noOfSpaces**2), confArray + mispArray)
        searchElements = letterArray[2]
        lookUpBoard = self.setPlatform(letterArray[0][0], letterArray[1], spaceLineUp[:noOfConfusers], searchElements, spaceLineUp[noOfConfusers:], noOfSpaces, shapeFormat, number)

        print("\nWelcome to DPJE's EyeTest Game")
        print("Be sure to seperate coordinates with a comma(,) and specify coordinates with a colon(:)")
        print("Please Note that %s is 10 - %i respectively"%(c.LETTERS[:noOfSpaces-10], noOfSpaces))
        print("Input 'exit' to stop playing the game.\n")
        self.printBoard(lookUpBoard, noOfSpaces)

        while noOfTries < noOfMisplacements:

            setLetter = searchElements[noOfTries]
            answer = self.setOfCoords(spaceLineUp[noOfConfusers:][noOfTries], noOfSpaces)
            enterCoords = input("Where is %s: "%setLetter)
            userCoords = showCoordinates(enterCoords)
            compareCoords = len(userCoords & answer)

            #If all coordinates are entered, print the following
            if compareCoords == len(answer):
                print(f"Correct - Your Input: {userCoords}")
                noOfTries += 1
            #If some or few of the coordinates are entered, tell the user the number of coordinates remaining to be inputed
            elif compareCoords != len(answer) and compareCoords > 0:
                print("Remaining, %i coordinates to enter."%len(userCoords - answer))
            #Else either bring up the problem or exit the game...
            else:
                if enterCoords.lower() == "exit":
                    print("Exiting Game...")
                    noOfTries = 100
                else:
                    print("None of the coordinates were inputed here.")
        else:
            print("Redirecting to Request Section...")
            self.request()

    def lNumber(self, levelType):
        """Note: levelType must be a string of following "easy", "normal" & "hard"."""
        try:
            number = {"Easy":1, "Normal":2, "Hard":3}[levelType]
        except KeyError:
            number = self.default
        return number

    """#Used to be here...
    def intRep(self, specifiedNo):
        s = "0123456789" + c.LETTERS
        return [s[i] for i in range(specifiedNo)]"""

    def setOfCoords(self, coords: list, length: int):
        return set([c.AsciiCoordinates().misCoordsTwoOutput(g, length) for g in coords])

    def setPlatform(self, background, confusion, cEntries, misplacements, mEntries, openings, sformat, levelNo):
        """     Note This;
        background - The letter to be used as the main board...
        strTuple - divided into confusion and misplacements
        format - [brick, zRow, zCol, diagonal, octagon, hexagon, heptagon, square, lCol, lRow, cross, block, triangle, pentagon]
        openings - total number of platform
        sformat - string for <format> specification
        levelNo - Could be 1, 2 or 3 for Easy, Normal or Hard
        misplacements - the list that contains both the number of locations and the locations that all elements of strTuple[1]
        is supposed to be located.
        """
        #Lists for loading
        modeNum = openings ** 2
        platform = [background for i in range(modeNum)]

        #Decorators
        decorators = {"brick":BoardSet().brick, "block":BoardSet().block, "cross":BoardSet().cross, "zRow":BoardSet().zRow, "zCol":BoardSet().zCol,
        "octagon":BoardSet().octagon, "diagonal":BoardSet().diagonal, "hexagon":BoardSet().hexagon, "heptagon":BoardSet().heptagon, "lCol":BoardSet().lCol, "lRow":BoardSet().lRow, 
        "triangle":BoardSet().triangle, "square":BoardSet().square, "pentagon":BoardSet().pentagon}[sformat]

        # Load the confusers
        for i, j in zip(confusion, cEntries):
            for elements in j:
                for d in decorators(elements, openings, levelNo+2):
                    platform[d%modeNum] = i

        #Load the misplacements; Based on formula [(no*2)+1, (no*3)+1]
        for char, stacks in zip(misplacements, mEntries):
            for s in stacks:
                platform[s%modeNum] = char

        return platform

    def printBoard(self, platform, length):
        t = c.intRep(length)
        print(" "*4, end=" ")
        for a in t:
            print("%s "%a, end=" ")
        print("\n")
        for i in range(length):
            print("%s - "%t[i], end=" ")
            for j in platform[i*length :(i+1)*length]:
                print(j+" ", end=" ")
            print("")

    def request(self):
        match input("Do you still want to continue this game: ").lower():
            case "yes":
                print("Yay, let's do this.")
                EyeTest(self.level)
            case "no":
                print("Sheesh, goodbye see you next time.")
            case _:
                print("Didn't understand what you typed, let's try that again.")
                self.request()

