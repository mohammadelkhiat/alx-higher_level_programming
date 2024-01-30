#!/usr/bin/python3
'''Test suit for Square class in the models.square module'''


import unittest
from unittest.mock import patch
from io import StringIO
from models.square import Square
from models.base import Base
from models.rectangle import Rectangle


class TestSquareClass(unittest.TestCase):
    '''Test class for Square class'''
# The setUp and tearDown of all tests

    def setUp(self):
        '''Befor each test'''
        Base._Base__nb_objects = 0

    def tearDown(self):
        '''After each test'''
        Base._Base__nb_objects = 0
# **************************************************************************
# Check inheritance from Base and Rectangle

    def test_inheritationfromBase(self):
        '''Test if the Square is inherited from Base'''
        self.assertTrue(issubclass(Square, Base))

    def test_inheritationfromBase(self):
        '''Test if the Square is inherited from Base'''
        self.assertTrue(issubclass(Square, Rectangle))

# **************************************************************************
# Check the existing of all the attributes

    def test_attributs(self):
        '''test that attributes exists'''
        r1 = Square(10)
        self.assertTrue(hasattr(r1, 'width'))
        self.assertTrue(hasattr(r1, 'height'))
        self.assertTrue(hasattr(r1, 'size'))
        self.assertTrue(hasattr(r1, 'x'))
        self.assertTrue(hasattr(r1, 'y'))
        self.assertTrue(hasattr(r1, 'id'))
# **************************************************************************
# Check Validation of all setters about type

    def test_validation_size_type(self):
        '''Test the validation of size of type'''
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r1 = Square("str", 2)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r1 = Square(True, 2)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r1 = Square(None, 2)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r1 = Square([10], 2)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r1 = Square((10, ), 2)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r1 = Square({'str': 10}, 2)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r1 = Square(10.52, 2)

# **************************************************************************
# Check Validation of all setters about value

    def test_validation_size_value(self):
        '''Test the validation of size of value'''
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            r1 = Square(0, 2)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            r1 = Square(-10, 2)
