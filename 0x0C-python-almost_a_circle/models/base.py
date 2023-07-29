#!/usr/bin/python3

"""This module defines a base class for all models in our pre-hbnb clone"""

import json
import os
import csv

class Base:
    """A base class for all hbnb models"""
    __nb_objects = 0

    def __init__(self, id=None):
        """Instatntiates a new model"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns JSON string representation of list_dictionaries"""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        json_list = []
        if list_objs is not None:
            for obj in list_objs:
                json_list.append(obj.to_dictionary())
        file_name = cls.__name__ + '.json'
        with open(file_name, 'w') as f:
            json.dump(json_list, f)

    @staticmethod
    def from_json_string(json_string):
        """Returns list of JSON string representation json_string"""
        if json_string is None or len(json_string) == 0:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Returns an instance with all attributes already set"""
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        elif cls.__name__ == "Square":
            dummy = cls(1)
        else:
            dummy = cls()
        dummy.update(**dictionary)
        return dummy


    @classmethod
    def load_from_file(cls):
        """Returns a list of instances"""
        file_name = cls.__name__ + '.json'
        try:
            with open(file_name, 'r') as f:
                json_list = cls.from_json_string(f.read())
                return [cls.create(**obj) for obj in json_list]
        except:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Serializes in CSV"""
        file_name = cls.__name__ + '.csv'
        with open(file_name, 'w') as f:
            if list_objs is None or len(list_objs) == 0:
                f.write("[]")
            else:
                if cls.__name__ == "Rectangle":
                    for obj in list_objs:
                        f.write("{},{},{},{},{}\n".format(obj.id, obj.width,
                                                          obj.height, obj.x,
                                                          obj.y))
                else:
                    for obj in list_objs:
                        f.write("{},{},{},{}\n".format(obj.id, obj.size,
                                                       obj.x, obj.y))
