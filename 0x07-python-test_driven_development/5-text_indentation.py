#!/usr/bin/python3
'''here is only one function in this module `text_indentation` function'''


def text_indentation(text):
    '''prints a text with 2 new lines
    after each of these characters: ., ? and :'''

    if type(text) is not str:
        raise TypeError("text must be a string")

    skip = True

    for charc in text:
        if charc == ' ' and skip:
            continue
        if charc != ' ':
            skip = False
        if charc not in ['.', '?', ':']:
            print(charc, end="")
        if charc in ['.', '?', ':']:
            print(charc)
            print()
            skip = True
