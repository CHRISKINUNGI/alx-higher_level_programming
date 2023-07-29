#!/usr/bin/python3

""" Module that contains a class BaseGeometry """

class BaseGeometry:
    """ BaseGeometry class """

    def area(self):
        """ Function that raises an exception """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ Function that validates value """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))

class Square(BaseGeometry):
    """ Square class """
    
    def __init__(self, size):
        """ Function that initializes size """
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        """ Function that returns area """
        return self.__size ** 2

    def __str__(self):
        """ Function that returns string """
        return "[Square] {}/{}".format(self.__size, self.__size)
