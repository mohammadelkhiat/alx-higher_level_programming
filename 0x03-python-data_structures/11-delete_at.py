#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    if idx > len(my_list) - 1:
        return my_list
    elif idx < 0:
        return my_list
    else:
        del my_list[idx]
        return my_list