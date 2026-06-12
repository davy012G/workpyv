#!/usr/bin/python3 set_info.py

# Filename: set_info.py

"""
Documentation
=============

This is more of a convenient .json (JavaScript Object Notation) file than it is a .py (Python) file. So the name is a pun with
the words 'settings' and 'info' which is just as simple to understand cuz it serves as the settings and the information storage
for the entire codebase of Project::HelperBot.
"""

PREF_LENGTH : int = 100
NAME : str = "HelperBot"
SIDECHAR: str = "||" #COULD BE CHANGED
HEAD : str = "*"
VERSION : tuple[int, int, int] = (0, 1, 0)

#Changeable variables
type credentials = tuple[str, str, int, str, str, str] #This makes sure that it is always kept that way
user_credentials : list[credentials] = []

# Information
INTRO = [
    "Welcome to the Work Module 0.1.0", 
    "Please choose whatever you want to do here",
    " ",
    "1. Sign In", 
    "2. Get Help", 
    "3. Exit"
]

EXIT = [
    " ",
    "Exiting...",
    "Thank you for coming",
    " "
]

SI_PAGE = [
    "Sign In>",
    "Welcome to the Sign-In Page; ",
    " "
]

WORK_ = [
    "Welcome,",
    " ",
    "This is the work zone please state which tool you want to work with;",
    " ",
    "1.Noteit - Helps you with texts and other issues you might want to put down in you computer.",
    "2.WorkBase - this includes your database and some data that you might want to save",
    "3.Advanced_Calc. - helps with your calculations and works like an artificial intelligence"
]

HOW_ = [
    '', 
    'Notes before you start the tutorial:', 
    '1.BE case sensitive when typing into the input system.', 
    '2.If you enter anything wrongly it will ask the question again.', 
    '3.It now offers user defined password input do you can input any password of your choice', 
    '', 
    "Once you enter the DPJE app you'll see the sign in option as the first thing. For Example;", 
    '', #[:7]
    'Name: (your name)', 
    'Age: (your age)', 
    'Profession: (your profession)', 
    'Birthday: (your birthdate)', 
    'Do you have any other information: No', 
    '', 
    'NAME: (your name)', 
    'BIRTHDAY: (your birthday)', 
    'PROFESSION: (your profession)', 
    'AGE: (your age)',
    '', #[7:18]
    'Take note of the Notes', 
    "After you fill in the sign in options they'll ask you if you want to add some other notes", 
    'it will then be left for you to make the decision whether you want to input it or not.', 
    "if you pass this criteria, you'll enter into the password zone. For Example:", 
    '', #[18:23]
    'Enter your password: sgt2873@_', 
    'Confirm the password: sgt2873@_', #[23:25]
    '', 
    'Once you enter the password,you see something like this', 
    '', #[25:28]
    'Welcome (your name) how can we help you', 
    '1. Games', 
    '2. Work', 
    'Please input one of the integers listed above. Thank you as you do so.',#[28:32]
    '', 
    'Enjoy the app.', 
    ''#[32:]
]

CREDIT_ = [
    '', 
    'Front and Back end Programming: David George', 
    'Editing and Writing: David George', 
    'Design and Animation: Paul George', 
    'Help: John the Beloved and Emmanuel George', 
    'All these people listed above are the pioneers of DPJE Productions.', 
    ''
]

MENU_ = [
    '', 
    'Help', 
    '', 
    'Welcome you must be a beginning user so what would you like to know:', 
    '1. About Us and Updates', 
    '2. How to do', 
    '3. Exit'
    ''
]

ABOUT = [
    '', 
    'Note:', 
    "- Please check our HTML file named 'aboutUs.html' to know about us.", 
    '- Please if there is any more information or update you want to be aware of go to the same file.', 
    '- This decision will be changed in the upcoming versions.', 
    '- Monopoly and some other games are still in-development.', 
    '- The WorkBase [This is to be removed when 0.1.0 is underway which is very close] due to the uselessness.', 
    '',
    f'Version Code: {VERSION[0]}.{VERSION[1]}.{VERSION[2]}',
    'Thank You.', 
    ''
]
