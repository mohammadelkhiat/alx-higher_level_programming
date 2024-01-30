#!/usr/bin/python3
'''Module of the Square class'''


from models.rectangle import Rectangle


class Square(Rectangle):
    '''A class defines square'''
    def __init__(self, size, x=0, y=0, id=None):
        '''Class constructor'''
        super().__init__(size, size, x, y, id)

    def __str__(self):
        '''return [Square] (<id>) <x>/<y> - <size>'''
        return "[Square] ({}) {}/{} - {}".format(self.id,
                                                 self.x, self.y, self.width)

    @property
    def size(self):
        '''Getter for size'''
        return self.width

    @size.setter
    def size(self, value):
        '''Setter for size'''
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        '''Update arguments as values to each attribute'''
        attrs = ("id", "size", "x", "y")
        if len(args) > 0:
            argv = args[:4]  # To handle if more than 4 arguments passed
            for i, arg in enumerate(argv):
                setattr(self, attrs[i], arg)
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        '''returns the dictionary representation of a Square'''
        return {"id": self.id, "size": self.size, "x": self.x, "y": self.y}
