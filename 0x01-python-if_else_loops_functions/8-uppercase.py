#!/usr/bin/python3
def uppercase(str):
    msg = ""
    for i in range(0, len(str)):
        char = str[i]
        if 'a' <= char <= 'z':
            msg += '{}'.format(chr(ord(char) - 32))
        else:
            msg += char
