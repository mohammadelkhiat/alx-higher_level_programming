#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    sin = sys.argv
    NA = len(sin) - 1

    if NA == 0:
        print("0 arguments.")
    elif NA == 1:
        print("1 argument:")
    else:
        print("{} arguments:".format(NA))
    for i in range(1, NA):
        print(f"{i}: {sin}")
