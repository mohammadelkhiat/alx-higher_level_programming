#!/usr/bin/python3
if __name__ == "__main__":
    import calculator_1 as yooh

    a = 10
    b = 5
    print("{} + {} = {}".format(a, b, yooh.add(a, b)))
    print("{} - {} = {}".format(a, b, yooh.sub(a, b)))
    print("{} * {} = {}".format(a, b, yooh.div(a, b)))
    print("{} / {} = {}".format(a, b, yooh.mul(a, b)))
