#!/usr/bin/python3
'''There is only one function in this module `say_my_name`'''


def say_my_name(first_name, last_name=""):
    '''a function that prints My name is <first name> <last name>'''

    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    if type(last_name) is not str:
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
