#!/usr/bin/python3 help_main.py

"""
Filename: help_main.py
Author: #DavyG
Purpose: To start the "Work" Project afresh - The one in the original module is deprecated
"""

import set_info as s
import text_display as td
import essentials as es

def bounds():
    #For the boundaries
    td.disp_bound(s.SIDECHAR, s.HEAD, s.PREF_LENGTH)

def center(str_arr: list[str]):
    #For a center display
    td.b_display(str_arr, s.SIDECHAR, " ", s.PREF_LENGTH)

def left(str_arr: list[str]):
    #For a left oriented display
    td.b_display_l(str_arr, s.SIDECHAR, " ", s.PREF_LENGTH)

def right(str_arr: list[str]):
    #For a right side display
    td.b_display_r(str_arr, s.SIDECHAR, " ", s.PREF_LENGTH)

def msg_box(message: str):
    #Since alot of functions use this then I'll make a seperate function for it
    print("\n")
    bounds()
    center([" ", message, " "])
    bounds()
    print("\n")

def num_input() -> int:
    int_input = es.int_return(input("==> "), 4)
    print("\n")

    return int_input

def exit_():
    #Just print the exit list
    bounds()
    center(s.EXIT)
    bounds()
    print("\n")

#############################################################################
##                              Sign-In                                    ##
#############################################################################

def start_work():
    print("\n")
    bounds()
    center(s.WORK_[:4])
    left(s.WORK_[4:])
    bounds()
    print("\n")

def any_other_info():
    running = True
    user_info = " "

    while running:
        yes_no = input("Any other information to give: ").lower()

        if yes_no == "yes":
            message = "Input any other information about yourself in one line: "
            user_info = input("==> ")
            running = False
        elif yes_no == "no":
            message = "Proceeding to next phase"
            running = False
        else:
            message = "Prompt is not recognized, please try again."
            running = True

        msg_box(message)

    return user_info

def security_code() -> str:
    running = True
    user_code = " "

    while running:
        user_code = input("Enter your password: ")

        if es.password_check(user_code):
            confirm = input("Confirm your password: ")

            if confirm == user_code:
                message = "Authorization granted."
                running = False
            else:
                message = "Passwords didn't match..."
                running = True
        else:
            message = "Note that a password must be more than 8 symbols and have at least 3 numbers and 2 symbols."
            running = True

        msg_box(message)
    
    return user_code

def prof_recogniser():
    user_prof = input("Enter your profession: ")
    print("\n")

    return user_prof #This one doesn't have any function checking it

def bday_celebrate() -> tuple[str, int]:
    message: str
    running = True
    user_bday = " "

    while running:
        user_bday = input("Enter your birthdate [Format- DD/MM/YYYY]: ")
        age = es.age_calculator(user_bday)

        if age > 17:
            #If he is greater 
            message = "Adulthood confirmed..."
            running = False #I put 0 here - but it makes me actually question if it would have worked if I had just let the 0 stay
        elif age > 0:
            message = "You are still young."
            running = False
        else:
            message = "Wrong Format, Try Again... Format: DD/MM/YYYY"
            running = True #Start afresh

        msg_box(message)

    return user_bday, age

def name_collector() -> str:
    message: str
    running = True
    user_name = " "

    while running:
        user_name = input("Enter your real name: ")

        if es.name_inspector(user_name):
            #If it's a real name then
            message = "Yes, it's a real name..."
            running = False #Terminate the loop but don't break off it just yet...
        else:
            message = "No, it's not a real name..."
            running = True

        msg_box(message)

    return user_name

def sign_in():
    bounds()
    left([s.SI_PAGE[0]])
    center(s.SI_PAGE[1:])
    bounds()
    print("\n")

    name = name_collector()
    birthday, age = bday_celebrate()
    proffession = prof_recogniser()
    password = security_code()
    others = any_other_info() #This is pratically useless and I don't know why it's still there

    bounds()
    left([
        " ", 
        f"NAME: {name}", 
        f"BIRTHDAY: {birthday}",
        f"AGE: {age}",
        f"PROFFESSION: {proffession}",
        f"ADDITIONAL INFO: {others}"
    ])
    bounds()

    s.user_credentials.append((name, birthday, age, proffession, password, others))
    start_work()

#############################################################################
##                             Help                                        ##
#############################################################################

def about():
    #About Section
    bounds()
    left(s.ABOUT[:4] + s.CREDIT_)
    bounds()
    print("\n")

def display_how():
    #'How' Section
    bounds()
    left(s.HOW_[:7])
    bounds()
    left(s.HOW_[7:18])
    bounds()
    left(s.HOW_[18:23])
    bounds()
    left(s.HOW_[23:26])
    bounds()
    left(s.HOW_[26:32])
    bounds()
    left(s.HOW_[32:])
    bounds()
    print("\n")

def help_():
    #Help Section
    bounds()
    center(s.MENU_[:4])
    left(s.MENU_[4:])
    bounds()
    print("\n")

    int_input = num_input()

    match int_input:
        case 1:
            about()
        case 2:
            display_how()
        case 3:
            exit_()
        case _:
            print("Try Again!")
            help_()

#############################################################################
##                               Others                                    ##
#############################################################################

def introduction():
    """This function is the introduction for the user
    This is where the user will choose to either go for the Sign In, Get Help or Exit Page."""
    
    bounds()
    center(s.INTRO[:3])
    left(s.INTRO[3:6])
    bounds()
    print("\n")

    int_input = num_input()

    match int_input:
        case 1:
            sign_in()
        case 2:
            help_()
        case 3:
            exit_()
        case _:
            print("Try again")
            introduction()

def main():
    """This function starts the whole process... 
    Make sure to keep this as the test function alone"""
    
    introduction()

if __name__ == "__main__":
    main()
