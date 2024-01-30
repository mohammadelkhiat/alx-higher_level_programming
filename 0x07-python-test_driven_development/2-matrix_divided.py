#!/usr/bin/python3
'''There is only one function in this module'''


def matrix_divided(matrix, div):
    '''divides all elements of a matrix.'''

    msg = 'matrix must be a matrix (list of lists) of integers/floats'

    # Check div validation
    if type(div) not in [int, float]:
        raise TypeError('div must be a number')
    if div == 0:
        raise ZeroDivisionError('division by zero')

    # Check matrix validation
    if type(matrix) is not list:
        raise TypeError(msg)

    # Create new matrix with the result
    new_matrix = []
    for i, row in enumerate(matrix):
        if type(row) is not list:
            raise TypeError(msg)
        if len(row) != len(matrix[0]):
            raise TypeError('Each row of the matrix must have the same size')
        new_matrix.append([])
        for item in row:
            if type(item) not in [int, float]:
                raise TypeError(msg)
            else:
                new_matrix[i].append(round((item / div), 2))

    return new_matrix
