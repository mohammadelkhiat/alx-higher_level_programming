#!/usr/bin/python3
def print_last_digit(number):
    LN = abs(number) % 10
    print(LN, end='')
    return LN
