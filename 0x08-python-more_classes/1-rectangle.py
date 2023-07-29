#!/usr/bin/python3
"""Module for Rectangle class with height and width setters."""

class Rectangle:
    """Rectangle class."""
    def __init__(self, width=0, height=0):
        """Initialize rectangle class with 'width' and 'height'
        Args:
            width (int): width of rectangle
            height (int): height of rectangle
        """   

        self.width = width
        self.height = height

    @property
    def width(self):
        """Get/set width of rectangle."""
        return self.__width
    
    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")

        if value < 0:
            raise ValueError("width must be >= 0")
        
        self.__width = value

    @property
    def height(self):
        """Get/set height of rectangle."""
        return self.__height
    
    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")

        if value < 0:
            raise ValueError("height must be >= 0")
        
        self.__height = value
