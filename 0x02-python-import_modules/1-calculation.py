#!/usr/bin/python3
if __name__ == "__main__":
    import calculator_1 as yooh

    a = 10
    b = 5
    print("{} + {} = {}".format(a, b, add(a, b)))
    print("{} - {} = {}".format(a, b, sub(a, b)))
    print("{} / {} = {}".format(a, b, div(a, b)))
    print("{} * {} = {}".format(a, b, mul(a, b)))
