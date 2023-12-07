def print_sorted_dictionary(a_dictionary):
    sorted_keys = []

    for key in a_dictionary:
        sorted_keys.append(key)

    sorted_keys.sort()

    for key in sorted_keys:
        value = a_dictionary[key]
        print("{}: {}".format(key, value))
