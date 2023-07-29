#!/usr/bin/python3

"""Student to JSON module"""

class Student:
    """Student class
    """
    def __init__(self, first_name, last_name, age):
        """Initializes an instance
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Retrieves a dictionary representation of a Student instance
        """
        if attrs is None:
            return self.__dict__
        else:
            new_dict = {}
            for key, value in self.__dict__.items():
                if key in attrs:
                    new_dict[key] = value
            return new_dict
        
    def reload_from_json(self, json):
        """Replaces all attributes of the Student instance
        """
        for key, value in json.items():
            self.__dict__[key] = value
