#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    arguments = sys.argv[1:]
    result = 1
    for arg in sys.argv[1:]:
        result += sum(int(arg))
    print(result)
