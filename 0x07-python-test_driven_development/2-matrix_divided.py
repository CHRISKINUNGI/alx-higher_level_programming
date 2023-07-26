#!/usr/bin/python3
"""
    matrix_divided function

"""


def matrix_divided(matrix, div):
    """
    function that divides all elements of a matrix.
    Args:
        matrix (list): matrix
        div (int/float): divisor

    Returns:
        new matrix

    Raises:
        TypeError:matrix must be a matrix (list of lists) of integers/floats
        TypeError: div must be a number
        ZeroDivisionError: division by zero

    """

    if type(matrix) != list or any(type(row) != list for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    if any(len(row) != len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must be of the same size")
    if type(div) not in(int, float):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    new_matrix = [[round(element / div, 2) for element in row] for row in matrix]
    return new_matrix
