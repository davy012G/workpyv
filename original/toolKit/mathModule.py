#File Name: mathModule.py
#Format: Camel Case

"""
The Math Module is for personal use only. It will implement modules such as the math modules and more mathematical
related modules.
"""

import math

def decimalPlace(number:float, fig:int):
    quotient, remainder = divmod(number*(10**(fig+1)), 10)
    result = (quotient + remainder//5) * 10**-fig
    return result

def quadEqn(a, b, c):
    discriminant = b**2 - (4*a*c)

    if discriminant > 0:
        # If it is positive follow the normal formula
        xOne = (-b + (discriminant**0.5)) / (2*a)
        xTwo = (-b - (discriminant**0.5)) / (2*a)
    else:
        # Else it is a complex number ending with i (i = sqrt(i))
        xOne = f"(-{b} / {(2*a)}) + {discriminant}i "
        xTwo = f"(-{b} / {(2*a)}) - {discriminant}i "

    return xOne, xTwo

def simEqn(a, b, c, d, e, f):
    x = ((c*e) - (b*f)) / ((a*e) - (b*d))
    y = ((c*d) - (a*f)) / ((b*d) - (a*e))

    return x, y

def decimal_base(n, b):
    """n - number, b - base, r - remainder"""
    number = n
    baseNo = 0
    j = 0
    while number > 0:
        q, r = divmod(number, b)
        baseNo += r * (10**j)
        number = q
        j += 1

    return baseNo

def base_decimal(x, y):
    number = x
    decimal = 0
    j = 0
    while number > 0:
        q, r = divmod(number, 10)
        decimal += r * (y**j)
        number = q
        j += 1

    return decimal

simple_hex = lambda integer: hex(integer)[2:].upper()

"""
binary = lambda integer: int(bin(integer)[2:])

def return_hex(integer: int) -> str:
	\"""First variant of the actual program\"""
	hexadecimals = "0123456789ABCDEF"
	n = integer
	hex_number = ""
	while n > 0:
		q, r = divmod(n, 16)
		hex_number += hexadecimals[r]
		n = q
	return hex_number[::-1]

def ret_hex(integer: int) -> str:
	\""" The actual hex program \"""
	hexadecimals = "0123456789ABCDEF"
	if integer > 15:
		n = integer
		hex_number = ""
		while n > 0:
			q, r = divmod(n, 16)
			hex_number += hexadecimals[r]
			n = q
	else:
		hex_number = hexadecimals[integer] + "0"
	return hex_number[::-1]
"""

def base_base(x, y, z):
    """This function helps in changing a number from base to base: eg: base_base(1023, 2, 5)"""
    return decimal_base(base_decimal(x, y), z)

"""
def exponentTen(n):
    \"""Task: find the floor division of log(10) of the number, n.\"""
    j = -1
    number = abs(n)
    while number > 0:
        number //= 10
        j += 1

    return j
"""

def std_exp(number: int) -> int:
    """Find the standard exponent of a number also the floor division of log 10 of parameter number..."""
    n = number
    x = 0
    while n > 10:
        n /= 10
        x += 1
    return x

def queue(x):
    """The creator has no reason for naming the function queue."""
    number = x
    n = exponentTen(x)
    groupedNo = []
    for i in range(n//3, -1, -1):
        e = 10 ** (3*i)
        no = number // e
        groupedNo.append(no)
        number -= no * e

    return groupedNo

def threeBythree(a, b, c, d, e, f, g, h, i):
    """This function handles tri-matrix related problems with a single formula approach."""
    return (b*f*g) - (c*e*g) - (a*f*h) + (c*d*h) + (a*e*i) - (b*d*i)

def twoBytwo(a, b, c, d):
    """This function handles bi-matrix related problems with a single formula approach."""
    return (a*d) - (b*c)

def root(number, rootValue):
    """The root function uses the standard law of indices which states that root of x = x ^ 1/rootvalue."""
    return number ** (1/rootValue)

def exponent(number, expValue):
    return number ** expValue

def factors(number):
    values = []
    for integer in range(1, number + 1):
        if number % integer == 0:
            values.append(integer)
    return values

def hcf(first_number, second_number):
    """hcf means highest common factor that means it finds the highest common factor in two list of factors of two numbers."""
    result = 0
    first_multiple = factors(first_number)
    second_multiple = factors(second_number)

    for f in range(1, len(first_multiple)):
        if first_multiple[f] in second_multiple:
            result = first_multiple[f]

    return [result, 1][int(result == 0)]

def hcf_beta(*integers: int):
    """This one is for """
    factor_sets = [set(factors(i)) for i in integers]
    ret_set = factor_sets[0] #this set will be returned in the final solution
    for f in range(1, len(factor_sets)):
        ret_set &= factor_sets[f]
    return max(ret_set)
		
def decimal_fraction(decimal_no):
    """Now this is not going to use the normal methods but its gonna use the <str> class - and yes I do not advice the constant use of these"""
    str_conv = str(decimal_no)
    conv_length = len(str_conv) - 2
    main_number = int(str_conv[:str_conv.find(".")]) #The number before decimal point
    mantissa = int(str_conv[str_conv.find(".") + 1:]) #The number after the decimal point
    divisor = hcf(mantissa, 10**conv_length)
    return main_number, mantissa / divisor, (10 ** conv_length) / divisor

def fraction_lowest(numerator, denominator):
    #It's literally like a snippet from the decimal_fraction function
    divisor = hcf(numerator, denominator)
    return numerator / divisor, denominator / divisor

def quadrilinear(a, b, c, d, e, f):
    mainPart = b*d
    discriminant = (b*d)**2 - (4*a*e*d*c - 4*(a**2)*e*f)
    div = 2*a*e

    if discriminant > 0:
        xOne = (mainPart + (discriminant**0.5)) / div
        xTwo = (mainPart - (discriminant**0.5)) / div
    else:
        xOne = f"({mainPart} + {discriminant}i) / {div}"
        xTwo = f"({mainPart} - {discriminant}i) / {div}"

    return xOne, xTwo

class NumberNaming:

    TRIPLE = ("", "thousand", "million", "billion", "trillion")
    UNIT = ("", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine")
    TENS_ONE = ("Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen")
    TENS = ("", "", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety")

    def splitNumbers(self, number, mode = 1):
        a = []
        b = number
        while b > 0:
            a.append(b%10)
            b //= 10
        return a[::mode]

    def figWords(self, number):
        l = []
        checkInt = 0
        for no, i in enumerate(self.splitNumbers(number)):
            r = no % 3
            if r == 0:
                l.append(self.TRIPLE[no//3])
                l.append(self.UNIT[i])
                checkInt = i
            elif r == 1:
                if i == 1:
                    change = self.TENS_ONE[checkInt]
                else:
                    change = self.TENS[i] + " " + self.UNIT[checkInt]
                l[-1] = change
            else:
                if i == 0:
                    l.append(self.UNIT[i] + " and")
                else:
                    l.append(self.UNIT[i] + " hundred and")

        return " ".join(l[::-1])
