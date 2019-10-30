"""
This problem was asked by Facebook.

Given a number in Roman numeral format, convert it to decimal.

The values of Roman numerals are as follows:

{
    'M': 1000,
    'D': 500,
    'C': 100,
    'L': 50,
    'X': 10,
    'V': 5,
    'I': 1
}
In addition, note that the Roman numeral system uses subtractive notation for numbers such as IV and XL.

For the input XIV, for instance, you should return 14.
"""

def convert_roman_to_deciaml(roman_number):
    roman_decimal_dict = {'M': 1000,
                          'D': 500,
                          'C': 100,
                          'L': 50,
                          'X': 10,
                          'V': 5,
                          'I': 1
                          }
    decimal_number = 0
    i = 0
    while i < (len(roman_number)-1):
        if len(roman_number) == 1:
            return roman_decimal_dict[roman_number[i]]
        else:
            if roman_decimal_dict[roman_number[i]] < roman_decimal_dict[roman_number[i+1]]:
                decimal_number = decimal_number + (roman_decimal_dict[roman_number[i+1]] - roman_decimal_dict[roman_number[i]])
                i = i+2
            else:
                decimal_number = decimal_number + roman_decimal_dict[roman_number[i]]
                i = i+1

    if i == len(roman_number):
        return decimal_number
    else:
        decimal_number = decimal_number + roman_decimal_dict[roman_number[-1]]

    return decimal_number

print(convert_roman_to_deciaml('MCDLVI'))