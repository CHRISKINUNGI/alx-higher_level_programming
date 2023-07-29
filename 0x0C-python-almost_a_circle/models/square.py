#!/usr/bin/python3

""" square.py: module for Square class """

from models.rectangle import Rectangle

class Square(Rectangle):
    """Square class"""

    def __init__(self, size=None, x=0, y=0, id=None):
        """Initialize Square instance"""
        super().__init__(id=id, width=size, height=size, x=x, y=y)
        self.__size = size

    # Getters and setters
    @property
    def size(self):
        """Get size"""
        return self.__size

    @size.setter
    def size(self, value):
        """Set size"""
        self.__size = value
        self.width = value
        self.height = value

    def __str__(self):
        """Return string representation of Square instance"""
        return "[Square] ({}) {}/{} - {}".format(
            self.id, self.x, self.y, self.size
        )

    def update(self, *args, **kwargs):
        """Update attributes of Square instance"""
        if args:
            if len(args) > 0:
                self.id = args[0]
            if len(args) > 1:
                self.size = args[1]
            if len(args) > 2:
                self.x = args[2]
            if len(args) > 3:
                self.y = args[3]
        else:
            if 'id' in kwargs:
                self.id = kwargs['id']
            if 'size' in kwargs:
                self.size = kwargs['size']
            if 'x' in kwargs:
                self.x = kwargs['x']
            if 'y' in kwargs:
                self.y = kwargs['y']

    def to_dictionary(self):
        """Return dictionary representation of Square instance"""
        return {
            'id': self.id,
            'size': self.size,
            'x': self.x,
            'y': self.y
        }
