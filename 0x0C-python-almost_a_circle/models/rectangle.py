#!/usr/bin/python3
'''Model of Rectangle class'''


from models.base import Base


class Rectangle(Base):
    '''A class that define width, height, x and y'''

    def __init__(self, width, height, x=0, y=0, id=None):
        '''Instantiation of width, height, x=0, y=0, id=None'''
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    def __validatePosInt(self, name, value, allowzero=True):
        '''Raise Error if value not a positive int'''
        if type(value) is not int:
            raise TypeError(name + ' must be an integer')
        if value < 0 and allowzero:
            raise ValueError(name + ' must be >= 0')
        if value <= 0 and not allowzero:
            raise ValueError(name + ' must be > 0')

    @property
    def width(self):
        '''Getter for width'''
        return self.__width

    @width.setter
    def width(self, value):
        '''Setter for width'''
        self.__validatePosInt("width", value, False)
        self.__width = value

    @property
    def height(self):
        '''Getter for height'''
        return self.__height

    @height.setter
    def height(self, value):
        '''Setter for height'''
        self.__validatePosInt("height", value, False)
        self.__height = value

    @property
    def x(self):
        '''Getter for x'''
        return self.__x

    @x.setter
    def x(self, value):
        '''Setter for x'''
        self.__validatePosInt("x", value)
        self.__x = value

    @property
    def y(self):
        '''Getter for y'''
        return self.__y

    @y.setter
    def y(self, value):
        '''Setter for y'''
        self.__validatePosInt("y", value)
        self.__y = value

    def __str__(self):
        '''return [Rectangle] (<id>) <x>/<y> - <width>/<height>'''
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id,
                                                       self.x, self.y,
                                                       self.width,
                                                       self.height)

    def area(self):
        '''returns the rectangle area'''
        return self.__width * self.__height

    def display(self):
        '''prints in stdout the Rectangle instance with the character #'''
        for i in range(self.__y):
            print()
        for row in range(self.__height):
            if self.__x > 0:
                print(" " * self.__x, end="")
            print("#" * self.__width)

    def update(self, *args, **kwargs):
        '''Update arguments as values to each attribute'''
        attrs = ("id", "width", "height", "x", "y")
        if len(args) > 0:
            argv = args[:5]  # To handle if more than 5 arguments passed
            for i, arg in enumerate(argv):
                setattr(self, attrs[i], arg)
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        '''returns the dictionary representation of a Rectangle'''
        return {"id": self.id, "width": self.width, "height": self.height,
                "x": self.x, "y": self.y}
