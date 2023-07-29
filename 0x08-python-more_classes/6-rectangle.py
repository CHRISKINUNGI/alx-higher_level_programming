#!/usr/bin/python3
"""Module for Rectangle class with del methods."""

class Rectangle:
    """Rectangle class."""

    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """Initialize rectangle class with 'width' and 'height'
        Args:
            width (int): width of rectangle
            height (int): height of rectangle
        """   

        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

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

    def area(self):
        """Return area of rectangle."""
        return self.width * self.height
    
    def perimeter(self):
        """Return perimeter of rectangle."""
        if self.width == 0 or self.height == 0:
            return 0
        return (self.width * 2) + (self.height * 2)

    def __str__(self):
        """Print rectangle using #"""
        if self.width == 0 or self.height == 0:
            return ""
        return "\n".join(["#" * self.width] * self.height)
    
    def __repr__(self):
        """Return string representation of rectangle"""
        return "Rectangle({}, {})".format(self.width, self.height)

    def __del__(self):
        """Print message when rectangle is deleted"""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
