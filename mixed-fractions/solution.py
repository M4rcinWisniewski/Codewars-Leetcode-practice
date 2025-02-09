#Simple fraction to mixed number converter
#Please check out the kata on: https://www.codewars.com/kata/556b85b433fb5e899200003f

import math

def mixed_fraction(s):
    a = ""
    b = ""
    division_index = len(s) - 1
    sign = ""
    # loop that specify numerator and denominator
    for i in range(0, len(s)):
        if s[i] == "/":
            division_index = i
            continue

        if s[i] == "-" and sign == "":
            sign = "-"
            continue
        if s[i] == "-" and sign == "-":
            sign = ""
            continue
        if i < division_index:
           a += s[i]

        else:
            b += s[i]
    if a == "0" and b != "0":
        return "0"
    try:
        b = int(b)  # Convert input to int
        a = int(a)
        result = a / b  # Might raise ZeroDivisionError
    except ZeroDivisionError:
        print("Error: Cannot divide by zero!")



    intiger = int(a) // int(b)

    if intiger == 0:
        a = int(a)
        b = int(b)
        gcd = math.gcd(a, b)
        a //= gcd
        b //= gcd
        return f"{sign}{a}/{b}"
    elif intiger > 0 and intiger == int(a) / int(b):
        return f"{sign}{intiger}"
    else:
        a = int(a)
        b = int(b)
        gcd = math.gcd(a, b)
        a //= gcd
        b //= gcd
        a -= intiger * int(b)

        return f"{sign}{intiger} {a}/{b}"







