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

class Rectangle(BaseGeometry):
    """ Rectangle class """

    def __init__(self, width, height):
        """ Function that initializes width and height """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
    
    def area(self):
        """ Function that returns area """
        return self.__width * self.__height
    
    def __str__(self):
        """ Function that returns string """
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
