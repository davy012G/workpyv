# File Name: monopoly.py

#Importing
#import toolKit.customTools as c
import random as r

"""
Notes :: Journey
----------------
This is my third time doing this project... I intend to maintain a steady build-test workflow I'll optimize later after I'm done
with the whole project and it's working well. I hope that this will be my last time on this project though, I'm getting sick of it.
Looks like I won't be using toolKit.customTools due to the fact that it might not be easily accessible by the module. The rule is simple
the game will end only if the money in the universal bank account has finished... I'm just finding out now that the greatest gift that 
was ever gifted to the art of gaming was the random module because if you're gonna make a game that will really appeal to people it needs
to be kinda unpredictable in it's actions and maybe it's gameplay (but that's sometimes though).
End of Day1 - Problem: How to make them inherit Playable
Day2 - <solved the End of Day1 Problem> Went out without any sort of problems just yet. Well, the only thing is that I need to add 
the features that make this game Monopoly and that's the chances, community chest stuff and the location defines... 
Day3 - [Adding the features] is in process... Then again the function <gameloop> might be the biggest of it's kind that i've ever made.
I'll resume this later... Was supposed to continue but because I came back later from church later than I ever thought I would (by 5pm
and it started 10am), haaa... I really need to look for another church tho. 
Day4 - I just sent some of my files in this Project file to my flash today, I don't really want to enter another file loss problem just 
like one time when I lost a lot of my project files and I was sorry for myself - It was so sad... So let's start this thing right?
Let's remember that we are still in the code testing and modification zone cuz I'm going to change a lot of things.

So this is the 24th of January 2026 (about a month since I started this project and nothing has changed...haaa) So I intend to enter
another phase by changing a few things - like removing the Player class and Auto class and just including something we will call specifix 
this helps to make things a lot easier for me later on in the project cuz we will be handling things that will not need much projects
to run smoothly... Plus we are changing the some stuff in the function set_players so that it'll support the one class movement. Also
there is a new update: The accountant will no longer be a Bank class element and will instead be a Playable class due to the fact that 
we will not need 

Documentation
-------------
[This is part of Generic Project Work]
Project name: Monopoly
Description: This is a One-file Monopoly CLI Game... It is an computer-based adaptation or (in this case) variant of the actual board game
of same name.
Author: her0_tr1b£
Start Date: 23rd of January 2026
End Date: 

Obsolete Code Samples
----------------------
class Player(Playable): #Inherit from the class Playable

    def __init__(self, name: str, symbol: str) -> None:
        \"""This is used to represent the user \"""
        self.name = name
        self.sym = symbol
        self.spec = "Player"
        super().__init__()
        #self.playerData.append([playerName, symbol, 0, 0, 0, 0, 0, 0, 0, True, {"houses":0, "hotels":0 ,"landedProps":[]}, []])

    def name_out(self):
        return self.name
    
    def play_input(self, string: str):# options: list, addition: list):
        \"""There is a good reason why I'm adding the useless ['---'] before the options and that's because the options are the ones
        recognizable by the code but sometimes the player might not know the right code to choose and will choose wrongly to try and 
        see if it'll be right but instead of this resisting the error it'll make the error to be another error that the computer
        can actually recognize and fix... Pls spare my explanation - I'm just not in my right mind yet.\"""
        return input(string).lower() #str_det(input(string), parent= ["-"] + addition + options).lower() #Every code will be in lower case letters (all of them)
    
    def print_cred(self):
        params = (["Name", "Symbol", "Location", "Cash", "Debit", "Pardon Points", "Permission to Move"],
                  [self.name, self.sym, self.loc_details(0), self.cash, self.debit, self.pardon_points, self.move_indicate])
        self.print_credentials(*params)

class Auto(Playable):

    def __init__(self, difficulty: str, number: int) -> None:
        \"""This is present in most of my present AI versus man projects. One identifies as a Player and the other as Auto.\"""
        self.name = "|Auto|%d|%s|"%(number, difficulty)
        self.diff = difficulty
        self.sym = "%d"%(number)
        self.spec = "Auto"
        #self.history = {}
        super().__init__() #Ended up putting this here cuz' I thought that using the easily accessible route by making Playable not...
        # to have an __init__ method was not working, but it turned out to be the self.cur_loc * int(self.move_indicate) typa curse that
        # was the problem...
        #Playable()

    def make_buy_decisions(self):
        pass

    def name_out(self):
        return self.name
    
    def play_input(self, string: str):
        \"""This is class Auto's play_input method and here are key things to note about it
        - Don't put options that are going to kill or overpower the machine in the options instead put them in the addition
        they might just get overlooked by the algorithm...
        - If you put an option that doesn't need to be in the options but in the additions then if you leave the options
        barren the algorithm might as well just pick it.\"""
        print("%s said yes to the prompt '%s'"%(self.name, string))
        return "yes"
    
    def print_cred(self):
        params = (["Name", "Symbol", "Difficulty", "Location", "Cash", "Debit", "Pardon Points", "Permission to Move"],
                  [self.name, self.sym, self.diff, self.loc_details(0), self.cash, self.debit, self.pardon_points, self.move_indicate])
        self.print_credentials(*params)

class Bank:

    def __init__(self, amount: int):
        self.money = amount
        self.ledger = [] #Ledger will probably be a list and append string accounts only

    def transfer_bandf(self, amount: int, sender: Player|Auto, reciever: Player|Auto):
        \"""transfer_bandf just means Transfer Back and Forth - This transaction is between a potential sender and a reciever at the 
        debit end so it's just a normal transfer occurence nothing too out of the ordinary...\"""
        reciever.cash += amount
        sender.cash -= amount
        print("Transfer fromto %s was successful"%(reciever.name))

    def transfer(self, amount: int, reciever: Player|Auto):
        \"""transfer just means to send to someone right so that's what the Bank Class is gonna be doing.\"""
        reciever.cash += amount
        self.money -= amount

    def collect(self, amount: int, sender: Player|Auto):
        \"""To collect is probably lighter to use than using the 'tax' keyword that adds a much harsher tone to the normal act of
        asking someone to pay up.\"""
        sender.cash -= amount
        self.money += amount

    def still_in_game(self):
        \"""The function main_game_loop uses this to check if the game has ended. It should be brought to the notice of people that 
        it's only if the money in the bank has finished that the game has ended and then it will count the money of each individual 
        and see who had the highest in the whole game.\"""
        return self.money > 0

Tested this under the 'main' function:
    retrieve = []
    for s in LocDict: #Retrive all the locdict lists
        retrieve.append(s[4]) #then retrive all the third elements in those locdicts 
    print(retrieve.count(0), retrieve) #This is to test if all of them are integers cuz we have forty instances of locations
After Test:
    #Final verdict 28 meaning there are 28 sales points... well given the stuff I've seen it'll make sense that that's the 
    #truth. QED
    #Print-out: 28, ['-', 0, '-', 0, '-', 0, 0, '-', 0, 0, '-', 0, 0, 0, 0, 0, 0, '-', 0, 0, '-', 0, '-', 0, 0, 0, 0, 0, 0, 0, '-', 0, 0, '-', 0, 0, '-', 0, '-', 0]

"""

# Universal Constants and Variables

# LocDict = ([Location, tag[sale, -, random, take, jail], price or amount of tax to pay, a list meant to store the names of the 
# players that bought houses (for the ones that have the sale tag on them), the number of lands bought (shouldn't be more than one), 
# the price of a house in that area, the price of a hotel in that area, the number of houses/hotels bought here])

LocDict = (["Go", "-", 0, "-", "-", 1, 0, 0],
["Old Kent Road", "sale", 600, [""], 0, 300, 500, 0],
["Community Chest", "random", 0, "-", "-", 1, 0, 0],
["WhiteChapel Road", "sale", 600, [""], 0, 300, 500, 0],
["Income Tax", "take", 0, "-", "-", 1, 0, 0],
["King's Cross Station", "sale", 2000, [""], 0, 1000, 1600, 0],
["The Angel Islington", "sale", 1000, [""], 0, 400, 700, 0],
["Chance", "random", 0, "-", "-", 1, 0, 0],
["Euston Road", "sale", 1000, [""], 0, 400, 700, 0],
["Pentonville Road", "sale", 1200, [""], 0, 500, 900, 0],
["Jail", "-", 0, "-", "-", 1, 0, 0],
["Pall Mall", "sale", 1400, [""], 0, 600, 1000, 0],
["Electric Company", "sale", 1500, [""], 0, 700, 1100, 8],
["White Hall", "sale", 1400, [""], 0, 600, 1000, 0],
["Northumber Land Avenue", "sale", 1600, [""], 0, 800, 1300, 0],
["Martyleborne station", "sale", 2000, [""], 0, 1000, 1600, 0],
["Bow Street", "sale", 1800, [""], 0, 900, 1500, 0],
["Community Chest", "random", 0, "-", "-", 0, 0, 0],
["Marlborough Street", "sale", 1800, [""], 0, 900, 1500, 0],
["Vine Street", "sale", 2000, [""], 0, 1000, 1600, 0],
["Free Parking", "-", 0, "-", "-", 0, 0, 0],
["Strand", "sale", 2200, [""], 0, 1000, 1600, 0],
["Chance", "random", 0, "-", "-", 1, 0, 0],
["Fleet Street", "sale", 2200, [""], 0, 1000, 1600, 0],
["Trafalgar Square", "sale", 2400, [""], 0, 1200, 1800, 0],
["FenChurch Station", "sale", 2000, [""], 0, 1000, 1600, 0],
["Leicester Square", "sale", 2600, [""], 0, 1400, 1800, 0],
["Coventry Street", "sale", 2600, [""], 0, 1400, 1800, 0],
["Water Works", "sale", 1500, [""], 0, 700, 1100, 8],
["Picadilly", "sale", 2800, [""], 0, 1500, 2000, 0],
["Go to Jail", "jail", 0, "-", "-", 1, 0, 0],
["Regent Street", "sale", 3000, [""], 0, 1600, 2200, 0],
["Oxford Street", "sale", 3000, [""], 0, 1600, 2200, 0],
["Community Chest", "random", 0, "-", "-", 0, 0, 0],
["Bond Street", "sale", 3200, [""], 0, 1600, 2200, 0],
["Liverpool Station", "sale", 2000, [""], 0, 1000, 1600, 0],
["Chance", "random", 0, "-", "-", 1, 0, 0],
["Park Lane", "sale", 3500, [""], 0, 2600, 3000, 0],
["Super Tax", "take", 1000, "-", "-", 1, 0, 0],
["MayFair", "sale", 4000, [""], 0, 3000, 3600, 0])

#CHANCE = ((Message, Tag, The Price or what is needed to perform the action specified by the tag.))
CHANCE = (("Make General Repairs on all of your houses and hotels \nFor each house pay $250 \nFor each hotel pay $1000.", "acc-pay", (-250, -1000)),
("Go to Jail, Move directly to jail, Do not pass 'Go' - Do not collect $2000", "location", (10, -2000)),
("Pay School Fees of $1500", "pay", -1500),
("Bank Pays you dividend of $500", "pay", 500),
("You have won a crossword competition, Collect $1000", "pay", 1000),
("Your Building loan matures recieve $1500", "pay", 1500),
("Advance to Trafalgar square, if you pass 'Go', Collect $2000", "location", (24, 0)),
("You have been assessed for street repairs \n$400 - for a house, $1150 - for a hotel", "acc-pay", (-400, -1150)),
("Go back three spaces", "-space", 3),
("Speeding Fine $150", "pay", -150),
("Advance to MayFair", "location", (39, 0)),
("Advance to Pall Mall, if you pass 'Go', Collect $2000", "location", (11, 2000)),
("'Drunk in Charge' - Fine $200", "pay", -200),
("Take a trip to Martyleborne station and if you pass 'Go', collect $2000", "location-pay", (15, 2000)),
("Get out of Jail free - (This card may be kept until needed)", "pardon", 1))

#CHEST = Is the same as Chance...
CHEST = (("Recieve Interest on 7% preference shares - 250", "pay", 250),
("Bank error in your favour, Collect $2000", "pay", 2000),
("Advance to Go", "location", (0, 0)),
("You have won second prize in a beauty contest, Collect $100", "pay", 100),
("Pay a $100 fine or take a chance", "chance", -100),
("Pay your Insurance Premium - it's $500 by the way...", "pay", 500),
("From sale to stock you get - $500", "pay", 500),
("Go back to Old Kent road", "location", (1, -2000)),
("Get out of Jail for free", "pardon", 1))

names = ("David", "Wallace", "John", "Piper", "Jemma", "Akira", "Paul") #I aim to have over one hundred names here...

#Return-Type Function

def str_det(string: str, parent: list[str] = ["e", "h", "n"]) -> str:
    """str_det means string-determine which means it tries to determine the string that the user meant...
    parent is used to know if the string parameter is within the lines of what was intended by the author.
    The original parameters will tell you that it was made with the diff variable under the setplayer's while-match
    loop directly under the 'c' case."""
    result = string

    if string not in parent:
        result = parent[0]
    return result

def int_det(pinteger: str, default_: int = 0) -> int :
    """The name int_det might be used to mean integer determine and unlike str_det might be used in turning strings (mostly) into 
    integers but it's based on the default_ integer you put in place..."""
    try:
        result = int(pinteger)
    except ValueError:
        result = default_

    return result

def roll_d_dice() -> int:
    """A dice has 6 faces and rolling it will give you one of the 6 faces for sure... The thought process behind the addition of
    two die was just based on the normal way we play it..."""
    return r.randrange(1, 6) + r.randrange(1, 6)

#Classes

class Playable:

    def __init__(self, name: str, specifix: str, symbol: str, difficulty: str, amount: int = 0, ) -> None:
        """Now we all know that the difficulty of a man to the eyes of a computer is "easy" so we are supposed to put "e"
        there is no reason in having to make another type of class to describe these ones or make another sort of "specifix" to 
        differentiate a human from a computer."""

        self.name = name
        self.spec = specifix
        self.symbol = symbol
        self.diff = difficulty
        self.cur_loc = 0
        self.past_loc = 0
        #self.loc_details = LocDict[self.cur_loc] - Handles the locations details
        self.cash = amount
        self.debit = 0
        self.uctu = 0 #UCTU means Untouchable by Computer but Touchable by User
        self.pardon_points = 0
        self.move_indicate = False
        self.deposit = 0 #This encourages saving and can only be accessed later on after fulfilling the actions of the second course of
        #action in the game
        #self.first_time = True
        #self.pass_threshold = False - I don't need it for now-- I guess
        self.message = []
        self.new_message = False
        self.property = {"houses":0, "hotels":0 ,"landedProps":[]}

    def isHuman(self):
        return self.spec == "h"

    def perm2start(self, roll_value: int, threshold: int):
        """This acronym means permission to start and  that is the thing that happens on your first time entering into the monopoly 
        world where you literally have to check what happens """
        if roll_value == threshold:
            self.move_indicate = True
            print("The threshold has been reached, Congratulations")
        else:
            print("Try again later! The number picked was %d and threshold is %d"%(roll_value, threshold))

    def check_lap(self):
        return self.past_loc >= self.cur_loc
    
    def position(self, increment: int):
        self.past_loc = self.cur_loc
        self.cur_loc = (self.cur_loc + (increment * int(self.move_indicate))) % 40

    def print_credentials(self, reference: list[str], value: list, sep= "=+>"):
        """This is the print_credentials part of the entire program"""
        print("Player credentials...")
        for r, v in zip(reference, value):
            print(r, sep, v)

    def loc_details(self): #(used to have address: int added so that it can be able to do the self.loc)
        """Specify the specific address that you want to get, in other words, I want it to be specific..."""
        return LocDict[self.cur_loc]

    def message_someone(self, PlayerName, message_str: str):
        PlayerName.message.append(message_str)

    def play_input(self, prompt: str):
        """prompt is just for the human alone and is just like a question. This was created with the game_loop first course of action in
        mind and might change as the code progresses."""

        if self.isHuman():
            answer = input(prompt)
        else:
            answer = "yes"

        return answer
    
    def transfer(self, price: int, p2):
        """cash is the money"""
        transfer = min(self.cash - self.uctu, price)
        p2.cash += transfer
        self.debit += price - transfer
        self.cash -= transfer
        self.deposit += self.uctu # The uctu is like transfer of your own money into the deposit so that you can access it when the need 
        # arises 

    def print_cred(self):
        params = (["Name", "Symbol", "Location", "Cash", "Debit", "Pardon Points", "Permission to Move"],
                  [self.name, self.symbol, self.loc_details()[0], self.cash, self.debit, self.pardon_points, self.move_indicate])
        self.print_credentials(*params)

# None-Type and Various-Type functions

def set_players():
    """This function sets and picks the right class for each player... m belongs to human players, c belongs to AI players"""
    turns = 1
    player_numbers = max(int_det(input("How many players will be present: "), default_= 3), 2)
    uniq_list = []
    record = {}
    no_of_c = -1
    
    while turns < player_numbers + 1:

        match str_det(input("Enter [c for computer and m for man]: "), parent= ["c", "m"]):
            case "m":
                specifix = "h" #h for human or man-controlled system
                diff = "e"
                name = input("Player [%d]'s name: "%(turns))
                symbol = input("Player [%d]'s symbol: "%(turns))

                if symbol not in uniq_list and len(symbol) == 1 and symbol.isnumeric() == False:
                    print("Player %d identifies as man with %s with a unique symbol of %s"%(turns, name, symbol))
                    turns += 1
                else:
                    print("You symbol needs to be unique, a one character symbol and not an integer... Let's try that again")

            case "c":
                specifix = "c" #c for computer or auto - It's a trend in my projects especially the ones that have AI systems in them
                no_of_c += 1
                name = r.choice(names)
                symbol = str(no_of_c)
                diff = str_det(input("Enter the difficulty: "))
                print("Player %d is an AI system with a difficulty of %s and a symbol of %d"%(turns, diff, no_of_c))
                turns += 1 #Must be the last thing in the code block...

            case _:
                print("Wrong code input. Let's try that again...")

        record[symbol] = Playable(name, specifix, symbol, diff)
        uniq_list.append(symbol) 
        #we ain't putting turns += 1 here cuz there is a parameter in match-case::m that if it doesn't go then don't move to next thing stay at that one...

    return uniq_list, record

def print_layout(board: list) -> None:
    """I'm just going to assume that the board we are talking about has 40 elements..."""
    boxes_up_there = ""
    boxes_down_there = ""

    #Bundle the ones at the upside and the downside
    for i in range(11):
        boxes_up_there += "|%s|"%(board[i])
        boxes_down_there += "|%s|"%(board[30-i])

    # Print Them Out
    print(boxes_up_there) #The boxes you see that start with GO and ends at Jail
    for p in range(11, 20): # count 9
        print("|%s|"%(board[50-p]), " "*25, "|%s|"%(board[p])) #There is a reason I put "   "*7 and it's because if you put 9 it will go off the board frame.
    print(boxes_down_there) #The boxes you see that starts with Go to Jail and ends at Free Parking

def get_chance() -> None:
    """A Chance well I think it's supposed to refer to how life handles stuff... You know LIFE IS BY CHANCE."""
    pass

def get_comm_chest() -> None:
    """This is an abbreviation for get community chest. A Community Chest is random tho..."""
    pass

def sales_dep(player: Playable, cur_addr: int, landBought: int, currency: str) -> None:
    """This will be the official sales department for my monopoly program.
    player as you already know is for the Playable element, cur_addr is just abbreviation for
    current address, landBought is an integer that works like a boolean: if it is 0 that means the land
    has not been bought yet and if it happens to be 1 then it means it has been bought, currency here
    is just used for ease of change cuz I might decide to change it from euro(£) to dollars($) """

    location = LocDict[cur_addr]

    if player.isHuman():
        if bool(landBought):
            print("Do you want to buy a house or hotel in %s for %s%d or %s%d")
        else:
            input("Do you want to buy %s for %s%d?"%())

def final_dec():
    """The name is final decisions - This function allows the player to be able to make final decisions based on what he/she wants...
    This can only be shown in demo... Note this is Player-specific and Auto cannot be allowed to do this (I don't even know how Auto will
    be able to pull it off)..."""
    pass

def game_loop() -> None:
    """This is the main game_loop and I am so sure that I will not like the length of this code in a few more days of writing it...
    Most people will wonder why I decided to make the request_to_continue variable be bound to an if statement - well the answer is
    in the fact that I, only, knows what type of loop catastrophe we are entering into and it's not gonna be a few, It's gonna be alot.
    Note: when calling player.loc_details refer to the LocDict for guidance"""

    turns = 0
    threshold = 6 #The threshold is six
    curr = "$" #This will specify the currency type so that I dont need to think too much about adding it to every one of them
    layout_board = [" "]*40
    accountant = Playable("accountant", "c", "100", "e", amount= 1_000_000) #A million dollars or euro's
    sym_list, pl_dict = [":", "2"], {':': Playable("David", "h", ":", "e"), '2': Playable("Wallace", "c", "●", "h")} #Will be replaced with - set_players()

    print("Benchmark") #This must be where it goes on to stop - Yep my speculation was right

    while accountant.cash > 0:
        player : Playable =  pl_dict[sym_list[turns]]
        request_to_continue = player.play_input("Do you want to roll the die [possible entries include- yes, leave, stop]: ") #, ["yes"], ["leave", "stop"])
        print(f"{request_to_continue= }")

        if request_to_continue == "yes":
            die_result = roll_d_dice()

            if player.move_indicate == True: #If a player has reached threshold then allow him to go

                if player.check_lap(): # If a player has gone a full lap then reward that player
                    accountant.transfer(2000, player)

                player.position(die_result) #Move according to the die value, bro
                layout_board[player.past_loc] = " " #Just blank the space that is no more used and 
                layout_board[player.cur_loc] = player.symbol #Fill the space that is avaiilable
                print(f"{player.cur_loc= }, {player.past_loc= }.") #Let me at least try to reveal the truth...
                print_layout(layout_board)
                player.print_cred() #There is a reason it's under here - It needs to capture all the changes
                print("Next Phase: \n")

                match player.loc_details(1): #1 means check the tag and then 2 gives us the prices attached to that property
                    case "sale":
                        # This is for the ones that scream "Come buy" vibez
                        # Let's think about sales... more like the property is asking people to buy it, right?!
                        print("Buy %s for %s%d."%(player.loc_details(0), curr, player.loc_details(2)))
                        #player._input("What do you want to buy [l- land, u- houses, t- hotel, n- none]: ", ["l", "u", "t", "h"])

                    case "take":
                        #This belongs to anything that has tax at the end of it's name
                        print("Welcome to %s. Your tax is %s%d."%(player.loc_details(0), curr, player.loc_details(2)))
                        #input("Input []: ")

                    case "random":
                        #This belongs to either Chest or Community Chest
                        print("%s says: <xxxxx> Hasn't been set yet."%(player.loc_details(0)))

                    case "jail":
                        #The Go to Jail is the only motherfucker with this punishment of a tag 
                        print("Sorry you'll need to %s. Pay %s%d to get out."%(player.loc_details(0), curr, player.loc_details(2)))

                    case "-":
                        # The Go and Free Parking map are the only ones with this...
                        print(r.choice(["A quick break before the menace rebegins", "Take a break now, before you continue the journey"]))

                if player.spec == "Player":
                    final_dec()
                #else do nothing cuz' there's nothing to do or there's nothing you can possibly do

            else:
                # If you haven't passed the threshold yet, Then roll the die to see if the number will land in the threshold
                # Maybe, just maybe you might get a number that will help you pass it (mostly 6 for most monopoly games i've played)
                # Yes of course 
                player.perm2start(die_result, threshold)

        #elif request_to_continue == "no":
        #    print("Okay, Moving to the next player...")
        
        elif request_to_continue == "leave":
            del pl_dict[player.symbol], sym_list[turns]
            print(r.choice(["It was nice playing with you though", "We'll see you again soon"]))

        elif request_to_continue == "stop":
            break

        else:
            print("[%s] is not recognized by the database - try using ['yes', 'leave' or 'stop']"%(request_to_continue))

        turns = (turns + 1) % len(pl_dict) #This is the indicator for a movement to the next player
        print("\nNext:: [Player %d]..."%(turns + 1))
    
    # Once the game breaks or it's done thenwe should think of wrapping up like going to the request function but that task is
    # For my guy <main> to decide - You see, I couldn't be bothered in the least by these types of things y'know
    print(r.choice(["Exiting...", "Moving to the request stage...", "Shutting game interface down..."])) 

def request():
    pass

def main():
    """This is the central program for running the monopoly.py"""
    print("her0_tr1b£ presents Monopoly")
    #game_loop()
    print("This is to test if all of LocDict[x][3] is 0")
    game_loop()

#This is for testing purposes
if __name__ == "__main__":
    main()