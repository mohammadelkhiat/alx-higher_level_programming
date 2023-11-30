#!/usr/bin/python3
if __name__ == "__main__":
    import calculator_1 as test
    a = 10
    b = 5
    print("{} + {} = {}".format(a, b, test.add(a, b)))
    print("{} - {} = {}".format(a, b, test.sub(a, b)))
    print("{} * {} = {}".format(a, b, test.div(a, b)))
    print("{} / {} = {}".format(a, b, test.mul(a, b)))
