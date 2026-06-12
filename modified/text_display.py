#Filename: text_display.py

"""
This file helps with the UI aspect of this project. Note that it will definitely be of little digression.
"""

def str_pad(string: str, pad_char: str, pad_amt: int) -> str:
    """
    Example:
    Input: str_pad("Hello", "*", 3)
    Expected Output: "***Hello***"
    """

    pad_material = pad_char * pad_amt
    return pad_material + string + pad_material

def str_pad_sep(string: str, pad_char: str, pad_amt_arr: list[int]) -> str:
    """
    Example:
    Input: str_pad_sep("Hello", "*-", [3, 5])
    Expected Output: "***Hello-----"
    """

    return (pad_char[0] * pad_amt_arr[0]) + string + (pad_char[1] * pad_amt_arr[1])

def hfun_bd_bdry(side_char: str, middle: int, sc_length: int) -> str:
    """
    This looks like such a cryptic message but it's actually just "helper function for bounded display <boundary>".
    What this means is that - it [this function] only exist to help the bounded display function or as it is called
    here "b_display" and this specific cuntion helps with the boundary that means it helps only with the top and 
    bottom lines of the UI display.

    Note: 
    side_char is a four-character string so it's just used as a sorta array. 
    left will always be at 2 and right will always be 3 in the case of side_char

    Example:
    Input: hfun_bd_bdry("*^-&", 0, 20)
    Expected Output: "-*********************************&" <assuming the * was called 20 times>
    """

    #We know that left is 2 and right is 3 especially when it's very close to the 
    return side_char[2] + (side_char[middle] * sc_length) + side_char[3]

def disp_bound(side_char_lr: str, character: str, amount: int) -> None:
    """
    disp_head = display header [the header is the line that u see as the boundary]
    Example
    """

    amount_ = amount - 2 #we just need "amount - 2"
    print(side_char_lr[0] + (character * amount_) + side_char_lr[1])

def b_display(str_arr: list[str], side_char_udlr: str, pad_char: str, AWOL: int) -> str | None: #*
    """
    This function is meant to give it a sort of "pagey" look

    Note:
    str_arr: A list of all the strings to be included in the UI
    side_char_udlr: Characters used for the up, down, left and right sides [In that specific manner]
    pad_char: The character that'll be used in place for the padding... could be spaces or asterisks but never empty spaces
    AWOL: Amount of Words in One Line

    Example:
    Input {
        hello_list = ["Hello my Fellow friends how are we doing",
                      "I am sure you all doing fine and good",
                      "Thank you for being so kind"
                      ]
        b_display(hello_list, "-*[]", " ", 90)
    }
    
    Output {
        "[----------------------------------------------------]\n
         [          Hello my Fellow friends how are we doing  ]\n
         [       I am sure you all are doing fine and good    ]\n
         [           Thank you for being so kind              ]\n
         [****************************************************]"

         Note this is not an accurate output - it's just an overview [How I want it to look like]
    }
    """
    
    dec2_awol = AWOL - 2

    for s in str_arr:
        s_length = dec2_awol - len(s) #Get the remaining length of the word in s (if it's bigger than dec2_awol - it will be negative)
        rem_space = pad_char * (s_length % 2)
        print(side_char_udlr[0] + str_pad(s, " ", s_length//2) + rem_space + side_char_udlr[1]) #We are using the half, though it will be kinda biased

def b_display_l(str_arr: list[str], side_char_udlr: str, pad_char: str, AWOL: int) -> None:
    """
   The left-sided mirrored version of b_display


    Example:
    Input {
        hello_list = ["Hello my Fellow friends how are we doing",
                      "I am sure you all doing fine and good",
                      "Thank you for being so kind"
                      ]
        b_display_l(hello_list, "-*[]", " ", 90)
    }
    
    Output {
        "[----------------------------------------------------]\n
         [Hello my Fellow friends how are we doing            ]\n
         [I am sure you all are doing fine and good           ]\n
         [Thank you for being so kind                         ]\n
         [****************************************************]"

         Note this is not an accurate output - it's just an overview [How I want it to look like]
    }
    """

    dec2_awol = AWOL - 2

    for s in str_arr:
        s_length = dec2_awol - len(s) 
        rem_space = pad_char * (s_length * (s_length > 0))
        a_string = s[:min(AWOL, len(s))] #This is the actual string
        print(side_char_udlr[0] + a_string + rem_space + side_char_udlr[1])

def b_display_r(str_arr: list[str], side_char_udlr: str, pad_char: str, AWOL: int) -> None:
    """
    The right-sided mirrored version of b_display

    Example:
    Input {
        hello_list = ["Hello my Fellow friends how are we doing",
                      "I am sure you all doing fine and good",
                      "Thank you for being so kind"
                      ]
        b_display_r(hello_list, "[]", " ", 90)
    }
    
    Output {
        "[----------------------------------------------------]\n
         [            Hello my Fellow friends how are we doing]\n
         [           I am sure you all are doing fine and good]\n
         [                         Thank you for being so kind]\n
         [****************************************************]"

         Note this is not an accurate output - it's just an overview [How I want it to look like]
    }
    """

    dec2_awol = AWOL - 2

    for s in str_arr:
        s_length = dec2_awol - len(s) 
        rem_space = pad_char * (s_length * (s_length > 0))
        a_string = s[:min(AWOL, len(s))]
        print(side_char_udlr[0] + rem_space + a_string + side_char_udlr[1])

"""
Make a return function for b_display, b_display_l, b_display_r

def b_display(str_arr: list[str], side_char_udlr: str, pad_char: str, AWOL: int) -> str | None: #*
    \"""
    This function is meant to give it a sort of "pagey" look

    Note:
    str_arr: A list of all the strings to be included in the UI
    side_char_udlr: Characters used for the up, down, left and right sides [In that specific manner]
    pad_char: The character that'll be used in place for the padding... could be spaces or asterisks but never empty spaces
    AWOL: Amount of Words in One Line

    Example:
    Input {
        hello_list = ["Hello my Fellow friends how are we doing",
                      "I am sure you all doing fine and good",
                      "Thank you for being so kind"
                      ]
        b_display(hello_list, "-*[]", " ", 90)
    }
    
    Output {
        "[----------------------------------------------------]\n
         [          Hello my Fellow friends how are we doing  ]\n
         [       I am sure you all are doing fine and good    ]\n
         [           Thank you for being so kind              ]\n
         [****************************************************]"

         Note this is not an accurate output - it's just an overview [How I want it to look like]
    }
    \"""
    
    dec2_awol = AWOL - 2
    start = hfun_bd_bdry(side_char_udlr, 0, dec2_awol)  #0 for Up
    end = hfun_bd_bdry(side_char_udlr, 1, dec2_awol)    #1 for Down

    print(start)

    for s in str_arr:
        s_length = dec2_awol - len(s) #Get the remaining length of the word in s (if it's bigger than dec2_awol - it will be negative)
        rem_space = pad_char * (s_length % 2)
        print(side_char_udlr[2] + str_pad(s, " ", s_length//2) + rem_space + side_char_udlr[3]) #We are using the half, though it will be kinda biased

    print(end)

    del start, end #Coming from systems programming makes you to feel like Python is the same
"""
