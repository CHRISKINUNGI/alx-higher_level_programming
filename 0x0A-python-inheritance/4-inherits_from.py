#!/usr/bin/python3

def inherits_from(obj, a_class):
    """
    Check if the object is an instance of a class that inherited (directly or indirectly) from the specified class.

    :param obj: The object to check.
    :param a_class: The class to check against.
    :return: True if the object is an instance of a subclass of a_class, otherwise False.
    """
    # Check if obj is an instance of a_class or any of its subclasses
    is_subclass = isinstance(obj, a_class)

    # Check if obj is not an instance of a_class itself but a subclass
    is_subclass_but_not_base = type(obj) != a_class

    # Return True if obj is a subclass of a_class, otherwise False
    return is_subclass and is_subclass_but_not_base
