#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = []
    for x in matrix:
        square_matrix = []
        for y in x:
            square_matrix.append(y**2)
        new_matrix.append(square_matrix)

    return new_matrix
