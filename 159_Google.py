"""
This problem was asked by Google.

Given a string, return the first recurring character in it, or null if there is no recurring character.

For example, given the string "acbbac", return "b". Given the string "abcdef", return null.
"""

def first_recurring(input_string):
    first_char = input_string[0]
    next_char = input_string[1]
    i = 1

    while first_char != next_char:
        i += 1

        if i == len(input_string):
            return None

        first_char = next_char
        next_char = input_string[i]



    return first_char


print(first_recurring("affccbaacc"))

