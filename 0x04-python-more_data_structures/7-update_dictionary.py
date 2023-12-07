#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    if a_dictionary[key]:
        a_dictionary[key] = value
    else:
        a_dictionary.update(key, value)
