#Filename: essentials.py

"""
Notes
=====
This python file that holds very important functions that other libraries will need.
It will only have (or mostly have) return-type functions than none-type functions.
Please this file should NOT import anything in this folder - it's meant to stay closed 
off from every file that is not in the standard python library.
"""

import datetime as dt

NUMBERS : str = "0123456789"
SYMBOLS : str = "+!\"£$%^&*(){}:@~<>?|\\,./;'[]#=-_`¬"

def int_return(string: str, default: int = 0) -> int:
    """
    Example:
    Input {
        print(int_return("9"))
        print(int_return("11a", 10))
    }
    Output {
        9
        10
    }
    """

    try:
        answer = int(string)
    except ValueError:
        answer = default
    
    return answer

def text_array(nl_string: str) -> list[str]:
    """
    Note
    text_array is only a helper function, but because it has a "stand-still" duty doesn't mean that it can't
    be kept for future purposes, this means that it will be kept after fulfilling it's duty 
    nl_string: newlined string or a string that contains one or more new_lines

    Example:
    Input {
        text_array("nl_string\n90")
    }
    Output {
        ["nl_string", "90"]
    }
    """

    return [ n.strip(" ") for n in nl_string.split("\n")]

#############################################################################
##                             help_main.py                                ##
#############################################################################

def name_inspector(string: str) -> bool:
    #if it doesn't have any form of symbols then it's probably a real name, else it's not
    return [ s in SYMBOLS for s in string].count(True) == 0

def password_check(string: str) -> bool:
    numbers = [ s in NUMBERS for s in string].count(True) > 3 #let there be at least 3 integers
    symbols = [ s in SYMBOLS for s in string].count(True) > 2 #and 2 symbols to make it strong...

    return numbers and (len(string) > 7) and symbols

def age_calculator(string: str, seperator: str = "/") -> int:
    answer : int = 0
    date_tuple = string.split(seperator)
    
    if len(date_tuple) == 3:
        day, month, year = date_tuple
        today = dt.datetime.now()
        answer = today.year - int_return(year, today.year)
        answer -= (today.month < int_return(month)) and (today.day > int_return(day))
    else:
        answer = -1
    
    return answer
