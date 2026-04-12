#Format: Camel Case
#File name: notes_beta.py

import tkinter as tk
import tkinter.ttk as ttk

backwardsWords = lambda essay, sepChar: list(essay.split(sepChar))[::-1] #Words in a string returned backwards
backwardsChars = lambda essay: essay[::-1] #Characters in a string returned backwards
showFind = lambda word, essay: essay.replace(word, "|" + word + "|") #Same thing as the last showFind just a little bit more efficient

def startTop(char, string):
    """Returns the first instance of char in string."""
    i = 0
    while i < len(string):
        if string[i: i+len(char)] == char:
            break
        else:
            i += 1
    else:
        i = len(string)
    return i

def startBottom(char, string):
    """Returns the last instance of char in string."""
    i = len(string) - 1
    while i > -1:
        if string[i-len(char): i] == char:
            break
        else:
            i -= 1
    else:
        i = -1
    return i

def binary_search(iterable: list, input: str, start: int = 0) -> list:
	array = []
	for i in iterable:
		if i[start: min(start + len(input), len(i))] == input:
			array.append(i)
	return array

def aiSearch(subject, writeUp):
    """The aiSearch looks for which is best...
    if it is a char look at the individuals elements of the writeUp which is a string and return it's list of locations
    if it is a word look a list of words seperated by space and return the list of locations for the word."""
    form = [writeUp, list(writeUp.split())][min(2,len(subject))-1]
    results = []

    for f,e in enumerate(form):
        if e == subject:
            results.append(f)

    return results

def searchComb(subject, writeUp):
    """searchComb simply means search the combination of letters that make up subject which is a string and 
    not a char of one letter. """
    results = []

    for f, e in enumerate(writeUp): # Note for self, f is the integer, e is the string
        if writeUp[f : f + len(subject)] == subject:
            results.append(f)

    return results

def searchWords(subject, writeUp):
    """The searchWords function searches words in the writeUp or a set of words, and i mean the real set of 
    words with a space. """
    results = []

    for f, e in enumerate(list(writeUp.split())):
        if e == subject:
            results.append(f)

    return results

def remove(firstList, secondList):
    """Remove the elements of the secondList that correspond with the elements of the firstList."""
    q = secondList

    for i in firstList:
        for n, j in enumerate(q): #I'll use i and j as the elements of the iterable
            if i == j: del q[n]

    return q

def replace(word, newWord, text, exception=[]):
    """Note: word:string, newWord:string, exception:listItem, text:string
    This function replaces <word> with <newWord> in <text> exception of <exception>. I hope that clears
    misunderstandings."""
    newText = list(text.split()) #make a variable containing the text

    for r in remove(exception, searchWords(word, text)):
        newText[r] = newWord

    return " ".join(newText)

def fileSpec(extension):
    """Return "txt", "colon", "braces" or "greatSign" if extension is a file extension recognised here
    else return "unidentified". """

    try:
        spec = {"txt":"None","py":"colon","jav":"braces","jav":"braces","htm":"greatSign","cpp":"braces"}[extension]
    except KeyError:
        spec = "unidentified"

    return spec

def symCheck(setOfChar, commentSymbol="#"):
    """If the last item in the setOfChar is one of these [: { >] then 1 is the return integer value else 0 it is.
    commentSymbol is the only real deal here because a comment can be of several words and are a pain in the butt. """
    #Things to watch for - #, [:, {, >]
    if len(setOfChar) > 0:
        if commentSymbol in setOfChar:# error_eg: #comment indexerror
            words = setOfChar[: max(1, startTop(commentSymbol, setOfChar))].strip()
        else:
            words = setOfChar.strip()
    else:
        words = " "

    return {True:1, False:0}[words[-1] in [":", "{", ">"]]

def symCheck2(setOfChar, commentSymbol="#", endSymbol="|"):
    """If the last item in the setOfChar is one of these [: { >] then 1 is the return integer value else 0 it is.
    commentSymbol is the only real deal here because a comment can be of several words and are a pain in the butt.
    <This one's with an endSymbol to end line
    endSymbol is used to break the indentation. """
    #Things to watch for - #, [:, {, >]
    words = " "

    if commentSymbol in setOfChar or endSymbol in setOfChar:
        words = setOfChar[:startTop(commentSymbol, setOfChar)]

    return {True:1, False:0}[words[-1] in [":", "{", ">"]] + {True:-1, False:0}[words[-1] in endSymbol]

class Notes_Text:
    def __init__(self):
        #fileEncoding = "utf-8"
        fileName = input("File Name: ")
        #title = input("Draft a Title for your File: ")
        self.selectEditor(fileSpec(list(fileName.split("."))[1]))

    def printLines(self, string, lineChar):
        print(string + "\n" + lineChar*(len(string)+1))

    def selectEditor(self, extSpec):
        """extSpec means extension Specification"""
        self.printLines("Write Notes/Code Here", "_")

        if extSpec in ["colon", "braces", "greatSign"]:
            self.indentFormat(extSpec)
        else:
            self.plainFormat()

    def plainFormat(self):
        record = 2
        fullText = ""

        while record > 0:
            singleLine = input()
            fullText = singleLine + "\n"

            if len(singleLine) == 0:
                record -= 1
            else:
                record = 2

        self.printLines("Notes", "_")
        self.options(fullText)

    def indentFormat(self, symbol):
        record = 3
        noOfTabs = 0
        fullCode = ""

        while record > 0:
            tabs = noOfTabs * "\t" #Gives the indentations
            singleLine = input(tabs)
            fullCode += tabs + singleLine + "\n"
            noOfTabs += symCheck(singleLine) #Symcheck is a vital tool here

            if len(singleLine) > 0:
                record = 3
            else:
                record -= 1
                noOfTabs = max(0, noOfTabs - 1)

        self.printLines("Code", "_")
        print(fullCode)
        self.options(fullCode)

    def options(self, groupWords): #Leaving this one for the next update
        modifiedText = ""
        textLength = len(list(groupWords.split()))
        taskManager = 0

        print("Type:\nsf for Show Find\nre for Replace\nec for Except\nru for Run\nsa for Save\nex for Exit\nFor Example: \"sf word\".")
        while taskManager < textLength:
            commandPallete = list(input("Input Command: ").split())

            match commandPallete[taskManager].lower():
                case "sf":
                    print(showFind(commandPallete[taskManager+1],groupWords))
                    taskManager += 2
                case "re":
                    if taskManager + 3 > textLength:
                        modifiedText = replace(commandPallete[taskManager+1], commandPallete[taskManager+2], groupWords, [])
                    else:
                        modifiedText = replace(commandPallete[taskManager+1], commandPallete[taskManager+2], groupWords, commandPallete[(taskManager+4):])
                    print(modifiedText)
                    taskManager = textLength
                case "sa":
                    self.save(modifiedText)
                    textLength += 1
                case "ru":
                    self.run(modifiedText)
                    textLength += 1
                case _:
                    break

    def save(self, entireString):
        pass

    def run(self, completeCode): 
        exec(completeCode)
        