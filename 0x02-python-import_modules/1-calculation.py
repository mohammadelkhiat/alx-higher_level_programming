#!/usr/bin/python3
if __name__ == "__main__":
    import calculator_1 as yo

    a = 10
    b = 5
    print("{} + {} = {}".format(a, b, yo.add(a, b)))
    print("{} - {} = {}".format(a, b, yo.sub(a, b)))
    print("{} * {} = {}".format(a, b, yo.div(a, b)))
    print("{} / {} = {}".format(a, b, yo.mul(a, b)))
