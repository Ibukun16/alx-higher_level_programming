#!/usr/bin/python3
def roman_to_int(roman_string):
    """"A function that converts roman figure
    to integer."""
    if not roman_string or not isinstance(roman_string, str):
        return 0

    roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    result = 0
    for value in reversed(roman_string):
        dgt = roman[value]
        result += dgt if result < dgt * 5 else -dgt
    return result
