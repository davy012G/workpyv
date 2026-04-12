#File Name: misc.py
#File Format: Camel Case

import random as r

#For ease of writing...
CONTINUEMSG = "Alright, Let's continue this then!"
GOODBYEMSG = "Okay, Goodbye for now though."

class Hangman:

    def __init__(self):
        self.hangman_run()

    def hangman_run(self):
        word = r.choice(["Hangman", "Hare", "Lion", "Bad"]) #For test purposes 
        charSeq, traceSeq = ["*" for i in range(len(word))], list(word)
        tries = 5
        print("Welcome to The Hangman Game")
        self.printSequence(charSeq)
        
        while tries > 0:
            try:
                userInput = input("Enter a character: ")[0]
            except IndexError:
                print("You didn't input a character.")

            if self.search(userInput, word) == True and userInput != "¬":
                location, letter = self.fetch(traceSeq, userInput.lower())
                charSeq[location] = letter
                traceSeq[location] = "¬"
                print("Yes, %s is a letter in the word I picked, Well Done!"%letter)
            else:
                print("No, the letter %s is not in the word I picked, Try Again."%userInput)
                tries -= 1
            print("\n")

            if traceSeq.count("¬") == len(word):
                print("Well done you won. Word: %s"%word)
                self.request()
                break

            if tries > 1:
                print("You have %s tries."%tries)
            elif tries == 1:
                print("You have %s tries."%tries)
            else:
                print("You don't have any more tries. Word: %s"%word)
                self.request()
                break

            self.printSequence(charSeq)
            #reply([1,0])

    def search(self, letter, word):
        return letter.lower() in list(word.lower())

    def printSequence(self, sequence):
        print("Word:", " ".join(sequence))

    def fetch(self, letterGr, letter):
        #letterGr means letter group, letter is well... a letter
        l = 0
        w = ""
        for no, i in enumerate(letterGr):
            if i.lower() == letter:
                l = no
                w = i
                break
        
        return l, w

    def request(self):
        match input("Do you still want to continue this game: ").lower():
            case "yes":
                print(CONTINUEMSG)
                Hangman()
            case "no":
                print(GOODBYEMSG)
            case _:
                print("Didn't understand what you typed, let's try that again.")
                self.request()

class RPS: # Check

    def __init__(self):
        self.rockPaperScissors()

    def rockPaperScissors(self):
        """RPS - Rock Paper Scissors is a game that is focused on random decisions
        from the computer so rest assured that the output is completely random."""
        tries = 5
        print("Welcome to the Rock-Paper-Scissors Game.")

        while tries > 0:
            autoGesture = r.choice(["Rock", "Paper", "Scissors"])
            userGesture = self.returnHand(input("Input either [r, p or s]: "))

            if self.checkStatus(userGesture, autoGesture) == "Win":
                print("You win, %s - %s"%(userGesture, autoGesture))
            elif self.checkStatus(userGesture, autoGesture) == "Lose":
                print("You lost, %s - %s"%(userGesture, autoGesture))
                tries -= 1
            else:
                print("Tie, %s - %s"%(userGesture, autoGesture))

            if tries > 1:
                print("You have %s tries."%tries)
            elif tries == 1:
                print("You have %s tries."%tries)
            else:
                print("You don't have any more tries.")
                self.request()
                break

    def returnHand(self, gesture):
        try:
            handGesture = {"r": "Rock", "p": "Paper", "s":"Scissors"}[gesture]
        except KeyError:
            handGesture = "Rock"
        return handGesture

    def checkStatus(self, user, auto):
        var = "Same"
        for i in [("Paper", "Rock"), ("Rock", "Scissors"), ("Scissors", "Paper")]:
            if user == i[0] and auto == i[1]:
                var = "Win"
                break
            else:
                if user == auto:
                    var = "Same"
                else:
                    var = "Lose"
        return var

    def request(self):
        match input("Do you still want to continue this game: ").lower():
            case "yes":
                print(CONTINUEMSG)
                RPS()
            case "no":
                print(GOODBYEMSG)
            case _:
                print("Didn't understand what you typed, let's try that again.")
                self.request()

class GuessingGame:

    def __init__(self):
        self.guessTheNumber

    def guessTheNumber(self):
        # This will be a piece of cake

        guessedNumber = r.randrange(0, 101) # Choose a number from 1-100
        tries = 5
        print("Welcome to The Guessing Game")

        while True:
            try:
                numInput = int(input("Enter a number: "))
            except ValueError:
                print("Numbers Only.")

            if numInput < guessedNumber:
                print("%s is lesser than the number I picked."%numInput)
                tries -= 1
            elif numInput > guessedNumber:
                print("%s is greater than the number I picked"%numInput)
                tries -= 1
            else:
                print("%s is the number"%numInput)
                self.request()
                break
            print("\n")

            if tries > 1:
                print("You have %s tries."%tries)
            elif tries == 1:
                print("You have %s tries."%tries)
            else:
                print("You don't have any more tries. Number: %s"%guessedNumber)
                self.request()
                break

    def request(self):
        match input("Do you still want to continue this game: ").lower():
            case "yes":
                print(CONTINUEMSG)
                GuessingGame()
            case "no":
                print(GOODBYEMSG)
            case _:
                print("Didn't understand what you typed, let's try that again.")
                self.request()
