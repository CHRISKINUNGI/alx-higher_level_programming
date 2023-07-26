#!/usr/bin/python3
""" first Module """


def add_integer(a, b=98):
    """
    This function adds 2 integers.

    Args:
        a (int): first integer.
        b (int): second integer.

    Returns:
        int: The return value. a + b.

    Raises:
        TypeError: If a or b are not integers or floats.
    """
    if type(a) is not int and type(a) is not float:
        raise TypeError("a must be an integer")
    if type(b) is not int and type(b) is not float:
        raise TypeError("b must be an integer")
    return int(a) + int(b)
