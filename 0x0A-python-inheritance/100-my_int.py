#!/usr/bin/python3

"""Module that contains a class MyInt that inherits from int"""

class MyInt(int):
    """Class that inherits from int"""

    def __eq__(self, other):
        """Function that returns the opposite of the default behavior"""
        return super().__ne__(other)

    def __ne__(self, other):
        """Function that returns the opposite of the default behavior"""
        return super().__eq__(other)
