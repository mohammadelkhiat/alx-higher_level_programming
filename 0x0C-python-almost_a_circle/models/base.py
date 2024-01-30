#!/usr/bin/python3
'''Model of the base class'''


import json
from os.path import exists


class Base:
    '''The base class of all of the classes in this project'''
    __nb_objects = 0

    def __init__(self, id=None):
        '''Instantiating the id and increament nb_objects'''
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = self.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        '''returns the JSON string representation of list_dictionaries'''
        if list_dictionaries:
            return json.dumps(list_dictionaries)
        else:
            return json.dumps([])

    @staticmethod
    def from_json_string(json_string):
        '''returns the list of the JSON string representation json_string'''
        if not json_string:
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def save_to_file(cls, list_objs):
        '''writes the JSON string representation of list_objs to a file'''
        list_dict = []
        if list_objs:
            for ob in list_objs:
                list_dict.append(ob.to_dictionary())
        with open((cls.__name__ + ".json"), "w", encoding="utf-8") as afile:
            afile.write(cls.to_json_string(list_dict))

    @classmethod
    def create(cls, **dictionary):  # One red check here
        '''returns an instance with all attributes already set'''
        if cls.__name__ == "Rectangle":
            ob = cls(1, 1)
        else:
            ob = cls(1)
        ob.update(**dictionary)
        return ob

    @classmethod
    def load_from_file(cls):
        '''returns a list of instances'''
        listofobj = []
        if exists(cls.__name__ + ".json"):
            with open(cls.__name__ + ".json", "r", encoding="utf-8") as afile:
                list_dict = cls.from_json_string(afile.read())
                for ob in list_dict:
                    listofobj.append(cls.create(**ob))
        return listofobj
