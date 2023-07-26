#!/usr/bin/python3

"""This module contains a function that prints My name is <first name> <last name>."""

def say_my_name(first_name, last_name=""):
    """This function prints My name is <first name> <last name>.

    Args:
        first_name (str): first name.
        last_name (str): last name.

    Returns:
        str: My name is <first name> <last name>.

    Raises:
        TypeError: If first_name or last_name are not strings.
    """

    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    if type(last_name) is not str:
        raise TypeError("last_name must be a string")

    return print("My name is {} {}".format(first_name, last_name))
