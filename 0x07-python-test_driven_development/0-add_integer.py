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
    if not (isinstance(a, (int, float))):
        raise TypeError("a must be an integer")
    if not (isinstance(b, (int, float))):
        raise TypeError("b must be an integer")
    a = int(a)
    b = int(b)

    return int(a+b)
