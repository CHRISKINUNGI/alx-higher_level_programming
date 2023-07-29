#!/usr/bin/env python3

""" Module that contains a function that returns a list with the available attributes and methods of an object """

def lookup(obj):
    """ Function that returns a list with the available attributes and methods of an object """
    return dir(obj)