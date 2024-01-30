#!/usr/bin/python3
'''This module of add_integer function that adds two integers
    Prototype: def add_integer(a, b=98):

    a and b must be integers or floats, otherwise raise a TypeError exception
    with the message a must be an integer or b must be an integer'''


def add_integer(a, b=98):
    """The add_integer function adds 2 integers
    Returns: int: The addition of the two numbers
    Raises: TypeError: if a or b is not an integer"""
    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    elif type(b) not in [int, float]:
        raise TypeError("b must be an integer")
    else:
        return int(a) + int(b)
