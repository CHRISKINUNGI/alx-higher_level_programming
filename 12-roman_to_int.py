#!/usr/bin/python3
def roman_to_int(roman_string):
    if roman_string is None or type(roman_string) != str:
        return 0

    roman_numeral = {'I': 1, 'V': 5, 'X': 10, 'L': 50,
                     'C': 100, 'D': 500, 'M': 1000}
    sum = 0
    for i in range(len(roman_string)):
        if i > 0 and roman_numeral[roman_string[i]] > \
                roman_numeral[roman_string[i - 1]]:
            sum += roman_numeral[roman_string[i]] - 2 * \
                roman_numeral[roman_string[i - 1]]
        else:
            sum += roman_numeral[roman_string[i]]
    return int(sum)
