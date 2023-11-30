#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    def print_arguments():
        num_arguments = len(sys.argv) - 1

        print(f"Number of argument(s): {num_arguments}", end=' ')
        print("argument" if num_arguments == 1 else "arguments", end='')
        print(":" if num_arguments > 0 else ".")
        for i in range(1, num_arguments + 1):
            print(f"{i}: {sys.argv[i]}")
