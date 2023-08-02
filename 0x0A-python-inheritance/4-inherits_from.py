#!/usr/bin/python3
"""Module that checks if an object is an instance of a class"""


def inherits_from(obj, a_class):
    """Function that returns True if the object is an instance of a class
    that inherited (directly or indirectly) from the specified class;
    otherwise False.
    Args:
        obj: object to check
        a_class: class to check
    Returns:
        True if the object is an instance of a class that inherited
        (directly or indirectly) from the specified class;
        otherwise False.
    """

    return isinstance(obj, a_class) and type(obj) != a_class
