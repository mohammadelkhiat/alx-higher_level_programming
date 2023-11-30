#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    arguments = sys.argv[1:]
    output = 1
    for arg in sys.argv[1:]:
        output += sum(int(arg))
    print(output)
