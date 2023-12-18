def magic_calculation(a, b):
    try:
        result = 0
        result = a ** b + 98
    except TypeError:
        result = None
    except ZeroDivisionError:
        result = None
    return result
