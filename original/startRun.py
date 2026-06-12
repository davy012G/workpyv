#File Name: startRun.py
#Format: Camel Case

import toolKit.customTools as c
import games.tictactoe as ttt
#import toolKit.notes_beta as note
import games.chess as chess
import games.misc as misc
import games.eyeTest as eyetest
import games.towerOfHanoi as toh

"""
Notes :: Everything-Else
-------------------------
* This is most likely a documentation for the upcoming versions.
* The file named games.monopoly is currently under development right now and facing some issues development-wise.
However, my deepest wish is to finish it before the first semester official break.  

Documentation
-------------
Name of Project: Project - HelperBot
Description: "This is my second COMPLETE project."
Author: her0_tr1b£
Format: Camel Case
Start Date: Last Year around June (June 2025)
End Date: xxxxxxx (Has not been resolved yet)
Version: 0.0.9
This version might be the final version of this software.
"""

WORK = """

Work

This is the work zone please state which tool you want to work with;

1.Noteit - Helps you with texts and other issues you might want to put down in you computer.
2.WorkBase - this includes your database and some data that you might want to save
3.Advanced_Calc. - helps with your calculations and works like an artificial intelligence
press any integer key to exit\n
"""

WORKBASE = """

WorkBase

Hello, Welcome to WorkBase here are statistical things you'ld like to work with
1. Pie Chart - It only gives you values
2. Bar Chart - Tries to imitate the bar chart
3. Pictogram - I'm not so sure how I'll put this to you but it's sure to show the workout a lot better
[This is to be removed when 0.1.0 is underway which is very close]
press any integer key to exit\n
"""

HOW_Before = """

Notes before you start the tutorial:
1.BE case sensitive when typing into the input system.
2.If you enter anything wrongly it will ask the question again.
3.The password generator generates passwords at random so a password can't be the same for two computers

Once you enter the DPJE app you'll see the sign in option as the first thing. For Example;

--------------------------------------------------------------------------------------------------------
Name: (your name)
Age: (your age)
Profession: (your profession)
Birthday: (your birthdate)
Do you have any other information: No
Verify that: Your name is (your name), you were born on the (your birthdate), you are a (your profession) 
and you are (your age) years old
---------------------------------------------------------------------------------------------------------

Take note of the Notes
After you fill in the sign in options they'll ask you if you want to add some other notes
it will then be left for you to make the decision whether you want to input it or not.
if you pass this criteria, you'll enter into the password zone. For Example:

---------------------------------------------------------------------------------------------------------
Your password is : 7500007699
Please enter your password: 7500007699
---------------------------------------------------------------------------------------------------------

Once you enter the password,you see something like this

-------------------------------------------------------------------------------
Welcome (your name) how can we help you
1. Games
2. Work
Please input one of the integers listed above. Thank you as you do so.
--------------------------------------------------------------------------------

Enjoy the app.\n
"""

HOW = """

Notes before you start the tutorial:
1.BE case sensitive when typing into the input system.
2.If you enter anything wrongly it will ask the question again.
3.It now offers user defined password input do you can input any password of your choice

Once you enter the DPJE app you'll see the sign in option as the first thing. For Example;

--------------------------------------------------------------------------------------------------------
Name: (your name)
Age: (your age)
Profession: (your profession)
Birthday: (your birthdate)
Do you have any other information: No

NAME: (your name)
BIRTHDAY: (your birthday)
PROFESSION: (your profession)
AGE: (your age)
---------------------------------------------------------------------------------------------------------

Take note of the Notes
After you fill in the sign in options they'll ask you if you want to add some other notes
it will then be left for you to make the decision whether you want to input it or not.
if you pass this criteria, you'll enter into the password zone. For Example:

---------------------------------------------------------------------------------------------------------
Enter your password: sgt2873@_
Confirm the password: sgt2873@_
---------------------------------------------------------------------------------------------------------

Once you enter the password,you see something like this

-------------------------------------------------------------------------------
Welcome (your name) how can we help you
1. Games
2. Work
Please input one of the integers listed above. Thank you as you do so.
--------------------------------------------------------------------------------

Enjoy the app.\n
"""

MENU = """
Help

Welcome you must be a beginning user so what would you like to know:
1. About Us and Updates
2. How to do
3. Credits
press any key to exit\n
"""

CREDIT = """

Front and Back end Programming: David George
Editing and Writing: David George
Design and Animation: Paul George
Help: John the Beloved and Emmanuel George
All these people listed above are the pioneers of DPJE Productions.\n
"""

GAMEMENU = """

Games

1. Tictactoe                      
2. Chess                          
3. EyeTest
4. HangMan
5. Rock-Paper-Scissors
6. Guessing Game
7. Tower Of Hanoi

press any integer key to exit \n
"""

ABOUT = """

Note:
- Please check our HTML file named 'aboutUs.html' to know about us.
- Please if there is any more information or update you want to be aware of go to the same file.
- This decision will be changed in the upcoming versions.
- Monopoly and some other games are still in-development.
- The WorkBase [This is to be removed when 0.1.0 is underway which is very close] due to the uselessness.
Version Code: 0.0.8

Thank You. \n
"""

WELCOME = """

1. Games
2. Work
press any integer key to exit\n
"""

name, birthday, profession, age = ["", "", "", 0]

class Main: #Fit all the FrontEnd into this class

    def __init__(self):
        """This is the init function of the 'Main' Class. This class majors in the frontend of the entire app making it the center of 
        the entire frontend system."""
        while True:
            match input("Welcome to the ToolBox::Concept\nEnter Sign In or Help or Exit: ").lower():
                case "sign in":
                    self.signIn()
                case "help":
                    self.menu()
                case "exit":
                    self.ending()
                    break
                case _:
                    print("Let's try that again, Input is not recognized")

    def ending(self):
        print("-"*15, "Exit", "-"*15)

    def welcomeUser(self):
        match c.errorEvasion(input(WELCOME + "Enter in here:" )):
            case 1:
                self.gameLink()
            case 2:
                self.workLink()
            case 3:
                self.ending()
            case _:
                print("Let's try this again - Input must be a number and must be within the range listed.")

    def password(self):
        set_password = input("Enter your Password: ")
        confirm = input("Confirm the password: ")

        if confirm == set_password and c.passwordVerifier(set_password):
            self.welcomeUser()
        else:
            print("Make sure the password has contains letters, numbers and symbols.")
            self.password()

    def signIn(self):
        """This 'sign-in' method will ask the user about his name, birthday and proffession before providing a valid
        info and sending it to the <global startRun list>."""
        name = input("Name: ")
        birthday = input("Birthday: ")
        profession = input("Profession: ")

        try:
            age = c.ageIdentify(birthday, "/")
        except:
            print("Let's try this again\n Make sure birthday is in a DD/MM/YYYY format.")
            self.signIn()

        match input("Do you have any other information [Yes or No]:").lower():

            case "no":
                print("NAME: %s\nBIRTHDAY: %s\nPROFESSION: %s\nAGE: %s"%(name, birthday, profession, age))
                self.password()

            case "yes":
                information = input("Input it right here [in one line]\n")
                print(f"NAME: {name}\nBIRTHDAY: {birthday}\nPROFESSION: {profession}\nAGE: {age}\nOTHER INFORMATION: {information}")
                self.password()

            case _:
                self.signIn()

    #Help Section

    def about_us(self):
        print(ABOUT)
        self.menu()

    def how(self):
        print(HOW)
        self.menu()

    def credit(self):
        print(CREDIT)
        self.menu()

    def menu(self):
        while True:
            match c.errorEvasion(input(MENU + "Enter an integer: ")):
                case 1:
                    self.about_us()
                case 2:
                    self.how()
                case 3:
                    self.credit()
                case _:
                    self.ending()
                    break

    #Menu section
    def gameLink(self):
        #while True:
        match c.errorEvasion(input(GAMEMENU + "Enter an integer: ")):
            case 1:
                print("Tic-Tac-Toe")
                ttt.TicTacToe()
            case 2:
                print("Chess")
                chess.main_()
            case 3:
                print("EyeTest")
                eyetest.EyeTest(c.errorEvasion(input("What Level would you want to go at: ")))
            case 4:
                print("Hangman")
                misc.Hangman()
            case 5:
                print("Rock-Paper-Scissors")
                misc.RPS()
            case 6:
                print("Guessing Game")
                misc.GuessingGame()
            case 7:
                print("Tower Of Hanoi")
                toh.TowerOfHanoi_Text(c.errorEvasion(input("What Level would you want to go at: ")))
            case _:
                self.ending()
                #break

    def workLink(self):
        #while True:
        match c.errorEvasion(input(WORK + "Enter a number: ")):
            #case 1:
                #note.Notes_Text()
            case 1:
                print(WORKBASE)
                print("-I- WorkBase -I-")
            case 2:
                print("-I- Advanced Calculator -I-")
            case _:
                self.ending()
                #break

if __name__ == "__main__":
    Main()
