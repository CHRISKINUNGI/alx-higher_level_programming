#!/usr/bin/python3
""" module containing function to print a square """


def print_square(size):
    """
        print_square()

        args:
            size (int)

        return:
            void
        raise:
            TypeError: size must be an integer
            ValueError: size must be >= 0
            TypeError: size must be an integer

    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if type(size) == float and size < 0:
        raise TypeError("size must be an integer")

    for i in range(size):
        for j in range(size):
            print("#", end="")
        print()
