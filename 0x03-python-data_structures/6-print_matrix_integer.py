#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if matrix:
        for i in matrix:
            for j in range(len(i)):
                if i == len(j) - 1:
                    print("{:d}".format(j[i]), end='')
                else:
                    print("{:d} ".format(j[i]), end='')
            print()
