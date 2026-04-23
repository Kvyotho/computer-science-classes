'''
I - 1
V - 5
X - 10
L - 50
C - 100
D - 500
M - 1000

LVIII - 58
MCMXCIV - 1994
'''


def romanToInt_v1(roman):
    #convert to int
    roman_numbers = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }
    roman = list(roman)
    roman.reverse()
    result = 0
    previous = 0

    for char in roman:
        value = roman_numbers[char]

        if value < previous:
            result -= value
        else:
            result += value

        previous = value

    return result
    
def romanToInt_v2(roman):
    roman_numbers = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }
    result = 0
    index = 0
    while index < len(roman):
        current_value = roman_numbers[roman[index]]
        next_value = roman_numbers[roman[index+1]]

        if current_value < next_value:
            result += next_value - current_value
            index += 2
        else:
            result -= current_value
            index += 1


print(romanToInt_v1('MCMXCIV'))
print(romanToInt_v2('XIV'))