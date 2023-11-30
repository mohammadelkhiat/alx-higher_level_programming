#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    def addition_of_arguments():
        arguments = sys.argv[1:]
        result = sum(int(arg) for arg in sys.argv[1:])
        print(result)
