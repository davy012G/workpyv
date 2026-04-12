#File Name: customTools.py
#File Format: Camel Case

import datetime
import random as r

NUMBERS = "0123456789."
LETTERS = "ABCDEFGHIJKLMNOPQRSTUVWYZabcdefghijklmnopqrstuvwyz"
SYMBOLS = "-_+=!£$%^&*<>:@?~#;'/.,"

#Functions

def errorEvasion(numberInput, default=1):
    try:
        output = int(numberInput)
    except ValueError:
        output = default

    return output


def passwordVerifier(password: str) -> bool: #BackEnd
    #Local Constants? you may ask, there is a reason why
    record = 0

    for i in [NUMBERS, LETTERS, SYMBOLS]:
        for p in password:
            if p in i:
                record += 1
                break

    return record == 3

def ageIdentify(birthdate: str, seperator: str) -> int:
    mDict = {"january":1, "february":2, "march":3, "april":4, "may":5, "june":6, "july":7, "august":8, "september":9, "october":10, "november":11, "december":12}
    addDict = {True:1, False:0}
    _, month, year = birthdate.split(seperator)
    today = datetime.datetime.now()
    age = today.year - int(year)

    if type(month) == str:
        if month in mDict:
            addition = addDict[today.month > mDict[month]]
        else:
            addition = 0
    else:
        addition = addDict[today.month > int(month)]

    age += addition
    return age

def selectLettersMin(level, letters, number):#@Public Function - eyeTest.py
    """We use this function for now though."""
    fNum = r.randrange(level + 1, number + 3)
    minimalNum = min(fNum, number - fNum)
    return letters[:minimalNum], letters[minimalNum:]

def selectLettersMax(level, letters, number):#@Miscellaneous function - eyeTest.py
    """This tool was made for any upcoming problems where it might be needed."""
    fNum = r.randrange(level, number - 1)
    maximalNum = max(fNum, number - fNum)
    return letters[:maximalNum], letters[maximalNum:]

def intRep(specifiedNo: int):
    s = NUMBERS[:-1] + LETTERS
    return [s[i] for i in range(specifiedNo)]

def _numberArrange(numbers: int):
    """Note that: this function will only return a string based on the number inputed."""
    result = " "*3
    alphabeticals = NUMBERS[:-1] + LETTERS
    for i in range(numbers):
        result += (" "*2 + alphabeticals[i])
    return result

#Classification: @StringOps

def randOutputIter(number: int, element_no: int) -> list:
	rand_string = ""
	list_of_str = []
	str_elements = list("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.")
	for n in range(number):
		for e in range(element_no):
			rand_string += r.choice(str_elements)
		list_of_str.append(rand_string)
		rand_string = ""
	return list_of_str

#Classes

class AsciiCoordinates:

    """
    def __init__(self) -> None:
        self.drawOnBoard(15, self.asciiGotoList((15, 15), (0, 15))) #Test whether it still works...
    """
    
    def newFunc(self, l, cf, a):
        """ Note that:
        n is a list of numbers
        cf is a change format or jump format as i like to call it.
        a is the first term atleast that's what we are taught in senior secondary school."""
        number = a
        newList = l
        for i in range(len(l)):
            newList[i] = number + cf
            number = newList[i]

        return newList
    """
    def alterCoords(self, l, cf, a):
        #same thing as first function but slightly different in change format.
        pass
    """

    def asciiGotoList(self, boardCoords, endCoords, startCoords= (0,0)): #*
        """
        x is an integer
        y is an integer
        boardCoords is a tuple representing the limit of the x and y coordinates of the same board
        """
        x, y = endCoords
        bDict = {True:-1, False:1}
        xEnd, yEnd = boardCoords 
        xStart, yStart = startCoords
        realX, realY = xEnd + (1-xStart), yEnd + (1-yStart)
        formulaPart = abs(x - y)
        isolatedPart = max(abs((x//realX) - (y//realY)), abs((x%realX) - (y%realY))) # Find the maximum number btw the difference of the row and the column respectively
        try:
            constant = formulaPart // isolatedPart
            steps = formulaPart % isolatedPart
        except ZeroDivisionError:
            constant = 1
            steps = 1

        if x > y:
            fX = x - (constant*isolatedPart)
            fY = x
        else:
            fX = x
            fY = x + (constant*isolatedPart)

        n = (list(range(fX, fY, constant)) + [fY])[::bDict[x > y]]
        n[len(n)-steps:] = self.newFunc(n[len(n)-steps:], {realX:realX+1, realX+1:1, 1:realX-1, realX-1:realX}[constant]*bDict[x > y], n[len(n)-(steps+1)])
        return n

    def drawOnBoard(self, root, sInput):
        """Now this function will be used for testing the shape functions in order to correct some things.
        Will be kept in the archived part of the AsciiCoordinates Class in toolkit.customTools."""

        fillLetter = "*"
        board = ["" for i in range(root ** 2)]
        #inputSys = self.asciiGotoList((root, root), (0, 15))

        for i in sInput:
            board[i%(root**2)] = fillLetter

        #Print the board - coordinate format set
        t = intRep(root) #(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, "A", "B", "C", "D", "E")
        print(_numberArrange(root)) #A here is 10 just as in hexaDecimal formats
        for i in range(root):
            print("%s - "%t[i%len(t)], end=" ")
            for j in board[i*root :(i+1)*root]:
                print(j+" ", end=" ")
            print()

    def misCoords(self, coordinates: tuple[int, int]|list[int], xP: int) -> int:
        """mode 0- shows you the position on a space of multiplied platform
        mode 1- shows you the possible end of line result to expect."""
        x, y = coordinates # example: (1, 2)
        return ((y * (xP+1)) + x) - 1

    def misCoordsTwoOutput(self, coordinates: int, xP: int) -> str:
        """The xP is the x-part of the overall platform coordinates..."""
        return "%s:%s"%(coordinates%xP, coordinates//xP)

    def checkCoord(self, inputStr: str) -> int:
        #Could be used to check if you can use miscoordstwooutput and miscoords
        return len(inputStr.split(":"))

class NumOps:

    def symCheck(self, word):
        """This does the handling of the signs..."""
        p = n = "+"
        j = ["+", "-"]
        e = 0
        for w in word:
            if w in j:
                e += {"+":0, "-":1}[w]
                n = j[e % 2]
            else:
                p = w
        return p, n

    def elements(self, string):
        """This is meant to save me the stress of having to build an elaborate system of types and statics 
        specifications..."""
        string = string + " "
        i = j = 0
        w = ""
        final = 2
        n = "+"
        t = []

        while i < len(string):
            g = j % 3
            if string[i] in [NUMBERS, LETTERS, SYMBOLS][g]:
                w += string[i]
                i += 1
                final = (j + 2) % 3
            else:
                if len(w) > 0:
                    if g < 1:
                        #if steps is 0 then make it a float
                        returnValue = float(n + w)
                        returnSign = n
                    elif g == 1:
                        #if steps is 1 save it as a letter
                        returnValue = w
                        returnSign = n
                    else:
                        #if steps is 2 it's a valuable symbol and so check the final component and add to the list
                        a, b = self.symCheck(n)
                        returnValue = a
                        returnSign = b
                    t.append(returnValue)
                    n = returnSign

                w = "" #Reset w

                if g == final:
                    if string[i] != " ":
                        t.append(string[i])
                    j += 1 #Go to next parameter
                    i += 1 #Go to next word
                else:
                    j += 1 #Go to the next word

        return t

    def coordSeperator(self, disintegrates): #Done
        """disintegrates must be a list that is produced by self.elements"""
        i = 0
        l = []
        
        while i < len(disintegrates):

            """
            #if disintegrates looks like a list opening save it as list
            if disintegrates[i] == "[":
                store, length = self.coordSeperator(disintegrates[i+1:])
                l.append(store)
                i += (length+1) #we increment the increment value by one to avoid the program seeing a chance to break
            #when disintegrates looks like a tuple opening save it as tuple
            elif disintegrates[i] == "(":
                store, length = self.coordSeperator(disintegrates[i+1:])
                l.append(tuple(store))
                i += (length+1)
            #anytime disintegrates looks like a set opening save it as set
            """

            if disintegrates[i] in "[({":
                store, length = self.coordSeperator(disintegrates[i+1:])
                l.append({"(":tuple, "[": list, "{":set}[disintegrates[i]](store))
                i += (length+1)

            elif disintegrates[i] in "]})":
                break

            else:
                l.append(disintegrates[i])
            i += 1 
            
        return l, i
    
    def splitCoords(self, string, spec= "t"):
        string += ","
        #Essential tools
        separator = {'t': tuple, 's': set, 'l': list}
        pair = ':()[]{} '
        group = ','
        #the three levels of storage
        word = ''
        bundle = []
        additionals = []

        #The checking stage (vocab to be corrected; checking)
        for s in string:
            if s in pair: #if s is not anything in the string called pair
                if len(word) > 0: #if the length of the word is 0 then don't do anything
                    bundle.append(word)
                    word = ''

            elif s in group: #if s is a comma
                bundle.append(word)
                additionals.append(separator[spec](bundle))
                bundle = []
                word = ''

            else:
                word += s
        
        return additionals
    
    def standardCsys(self, string:str):
        """A standard Coordinate system in my own terms looks like this;
        "20:30, 78:52, 64:90, 34:20", ...
        And the splitCoords needs this function to catch any errors because it ain't seeing any other system apart from that
        one"""
        standard = "0123456789:., "
        boolean = True

        for s in string:
            if s not in standard:
                boolean = False
                break
        
        return boolean
