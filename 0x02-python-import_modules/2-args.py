#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    sin = sys.argv

    NA = len(sys.argv) - 1

    if NA == 0:
        print(f"{NA} arguments")
    elif NA == 1:
        print(f"{NA} argument")
    else NA > 1:
        print(f"{NA} argument")
    for i in range(0, NA):
        print(f"{i}: {sin}")
