#!/usr/bin/python3
'''There is only one function in this module `print_square` function'''


def print_square(size):
    '''prints a square with the character # with given size.'''

    if size == 0:
        print()
        return

    if type(size) is int and size < 0:
        raise ValueError("size must be >= 0")

    if type(size) in [int, float]:

        if type(size) is not float or size > 0:

            for i in range(int(size)):
                print("#" * int(size))
            return

    raise TypeError("size must be an integer")
