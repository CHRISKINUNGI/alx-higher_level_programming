#!/usr/bin/python3
""" Module that contains a function that deletes a key in a dictionary """


def simple_delete(a_dictionary, key=""):
    """ Function that deletes a key in a dictionary """

    if key in a_dictionary:
        del a_dictionary[key]
    return a_dictionary
