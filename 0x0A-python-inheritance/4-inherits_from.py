#!/usr/bin/python3

def inherits_from(obj, a_class):
    """Check if the object is an instance of a subclass of the specified class.

    Args:
        obj (object): The object to check.
        a_class (class): The class to compare against.

    Returns:
        bool: True if the object is an instance of a
        subclass of the specified class; otherwise False.
    """
    return issubclass(type(obj), a_class) and type(obj) != a_class
