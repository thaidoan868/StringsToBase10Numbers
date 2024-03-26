"""This program converts base 26 strings to base 10 numbers, these two numbers have the same value but expressed in different radixes"""
def StringToNumber(String):
    digit_list = [ord(i)-97 for i in String]
    for digit in digit_list:
        if not(0 <= digit <= 26): return 0
    StringToNumber = 0
    digit, i = digit_list, range(len(digit_list)-1, -1, -1)
    for digit, i in zip(digit_list, range(len(digit_list)-1, -1, -1)): StringToNumber += digit*(26**i)
    return StringToNumber