#!/usr/bin/python3
'''Module of test suit for the class Rectangle'''


from unittest.mock import patch
import unittest
from io import StringIO
from models.rectangle import Rectangle
from models.base import Base


class TestRectangleClass(unittest.TestCase):
    '''Test class for the Rectangle class'''
# The setUp and tearDown of all tests

    def setUp(self):
        '''Befor each test'''
        Base._Base__nb_objects = 0

    def tearDown(self):
        '''After each test'''
        Base._Base__nb_objects = 0
# **************************************************************************
# Check inheritance from Base

    def test_inheritationfromBase(self):
        '''Test if the Rectangle is inherited from Base'''
        self.assertTrue(issubclass(Rectangle, Base))
# **************************************************************************
# Check the existing of all the attributes

    def test_attributs(self):
        '''test that attributes exists'''
        r1 = Rectangle(10, 2)
        self.assertTrue(hasattr(r1, 'width'))
        self.assertTrue(hasattr(r1, 'height'))
        self.assertTrue(hasattr(r1, 'x'))
        self.assertTrue(hasattr(r1, 'y'))
        self.assertTrue(hasattr(r1, 'id'))
# **************************************************************************
# Check Validation of all setters about type

    def test_validation_Width_type(self):
        '''Test the validation of width of type'''
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r1 = Rectangle("str", 2)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r1 = Rectangle(True, 2)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r1 = Rectangle(None, 2)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r1 = Rectangle([10], 2)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r1 = Rectangle((10, ), 2)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r1 = Rectangle({'str': 10}, 2)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r1 = Rectangle(10.52, 2)

    def test_validation_height_type(self):
        '''Test the validation of height of type'''
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            r1 = Rectangle(10, "str")
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            r1 = Rectangle(10, True)
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            r1 = Rectangle(10, None)
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            r1 = Rectangle(10, [10])
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            r1 = Rectangle(10, (10, ))
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            r1 = Rectangle(10, {'str': 10})
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            r1 = Rectangle(10, 2.52)

    def test_validation_x_type(self):
        '''Test the validation of x of type'''
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            r1 = Rectangle(10, 2, "str")
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            r1 = Rectangle(10, 2, True)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            r1 = Rectangle(10, 2, None)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            r1 = Rectangle(10, 2, [10])
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            r1 = Rectangle(10, 2, (10, ))
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            r1 = Rectangle(10, 2, {'str': 10})
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            r1 = Rectangle(10, 2, 10.25)

    def test_validation_y_type(self):
        '''Test the validation of y of type'''
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            r1 = Rectangle(10, 2, 3, "str")
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            r1 = Rectangle(10, 2, 3, True)
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            r1 = Rectangle(10, 2, 3, None)
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            r1 = Rectangle(10, 2, 3, [10])
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            r1 = Rectangle(10, 2, 3, (10, ))
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            r1 = Rectangle(10, 2, 3, {'str': 10})
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            r1 = Rectangle(10, 2, 3, 10.25)
# **************************************************************************
# Check Validation of all setters about value

    def test_validation_width_value(self):
        '''Test the validation of width of value'''
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            r1 = Rectangle(0, 2)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            r1 = Rectangle(-10, 2)

    def test_validation_height_value(self):
        '''Test the validation of height of value'''
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            r1 = Rectangle(10, 0)
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            r1 = Rectangle(10, -2)

    def test_validation_x_value(self):
        '''Test the validation of x of value'''
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            r1 = Rectangle(10, 2, -2)

    def test_validation_y_value(self):
        '''Test the validation of y of value'''
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            r1 = Rectangle(10, 2, 3, -2)
# **************************************************************************
# Check with different number of arguments

    def test_TwoTipicalArgs(self):
        '''Testing the case of two typical arguments'''
        r1 = Rectangle(10, 2)
        self.assertEqual(r1.id, 1)
        self.assertEqual(r1.width, 10)
        self.assertEqual(r1.height, 2)
        self.assertEqual(r1.x, 0)
        self.assertEqual(r1.y, 0)

        r2 = Rectangle(2, 10)
        self.assertEqual(r2.id, 2)
        self.assertEqual(r2.width, 2)
        self.assertEqual(r2.height, 10)
        self.assertEqual(r2.x, 0)
        self.assertEqual(r2.y, 0)

    def test_ThreeArgs(self):
        '''Testing the case of three typical arguments'''
        r1 = Rectangle(10, 2, 3)
        self.assertEqual(r1.id, 1)
        self.assertEqual(r1.width, 10)
        self.assertEqual(r1.height, 2)
        self.assertEqual(r1.x, 3)
        self.assertEqual(r1.y, 0)

    def test_FourArgs(self):
        '''Testing the case of four typical arguments'''
        r1 = Rectangle(10, 2, 3, 4)
        self.assertEqual(r1.id, 1)
        self.assertEqual(r1.width, 10)
        self.assertEqual(r1.height, 2)
        self.assertEqual(r1.x, 3)
        self.assertEqual(r1.y, 4)

    def test_FiveArgs(self):
        '''Testing the case of five typical arguments'''
        r1 = Rectangle(10, 2, 3, 4, 15)
        self.assertEqual(r1.id, 15)
        self.assertEqual(r1.width, 10)
        self.assertEqual(r1.height, 2)
        self.assertEqual(r1.x, 3)
        self.assertEqual(r1.y, 4)

    def test_MoreThanFiveArgs(self):
        '''Testing the case of three typical arguments'''
        with self.assertRaises(TypeError):
            r1 = Rectangle(10, 2, 3, 4, 15, 20)
# ***************************************************************************
# Check for area method

    def test_areaMethodTypical(self):
        '''Testing the normal cases of using the area method'''
        r1 = Rectangle(3, 2)
        r2 = Rectangle(2, 10)
        r3 = Rectangle(8, 7, 0, 0, 12)
        self.assertEqual(r1.area(), 6)
        self.assertEqual(r2.area(), 20)
        self.assertEqual(r3.area(), 56)

    def test_passArg(self):
        '''Testing when passing arguments'''
        r1 = Rectangle(3, 2)
        with self.assertRaises(TypeError):
            r1.area(10)
# ***************************************************************************
# Test the display method

    def test_nomal(self):
        '''Testing the normal cases of using the display method'''
        r1 = Rectangle(4, 6)
        expected = '####\n####\n####\n####\n####\n####\n'
        with patch("sys.stdout", new = StringIO()) as output:
            r1.display()
            self.assertEqual(output.getvalue(), expected)

        r2 = Rectangle(2, 2)
        expected = '##\n##\n'
        with patch("sys.stdout", new = StringIO()) as output:
            r2.display()
            self.assertEqual(output.getvalue(), expected)

    def test_handleXY(self):
        '''Test how the function handle x and y'''
        r1 = Rectangle(2, 3, 2, 2)
        expected = "\n\n  ##\n  ##\n  ##\n"
        with patch("sys.stdout", new = StringIO()) as output:
            r1.display()
            self.assertEqual(output.getvalue(), expected)

        r2 = Rectangle(3, 2, 1, 0)
        expected = " ###\n ###\n"
        with patch("sys.stdout", new = StringIO()) as output:
            r2.display()
            self.assertEqual(output.getvalue(), expected)
# ***************************************************************************
# Test the __str__ method

    def test_strMethodNormal(self):
        '''test the return str of the method'''
        r1 = Rectangle(4, 6, 2, 1, 12)
        self.assertEqual(str(r1), "[Rectangle] (12) 2/1 - 4/6")

        r2 = Rectangle(5, 5, 1)
        self.assertEqual(str(r2), "[Rectangle] (1) 1/0 - 5/5")
# ***************************************************************************
# Test the update method in case of no-keyword arguments

    def test_update_all(self):
        '''Testing the normal cases of using the update method'''
        r1 = Rectangle(10, 10, 10, 10)
        r1.update(89, 2, 3, 4, 5)
        self.assertEqual(str(r1), "[Rectangle] (89) 4/5 - 2/3")
    
    def test_update_4attrs(self):
        r1 = Rectangle(10, 10, 10, 10)
        r1.update(89, 2, 3, 4)
        self.assertEqual(str(r1), "[Rectangle] (89) 4/10 - 2/3")

    def test_update_3attrs(self):
        r1 = Rectangle(10, 10, 10, 10)
        r1.update(89, 2, 3)
        self.assertEqual(str(r1), "[Rectangle] (89) 10/10 - 2/3")

    def test_update_2attrs(self):
        r1 = Rectangle(10, 10, 10, 10)
        r1.update(89, 2)
        self.assertEqual(str(r1), "[Rectangle] (89) 10/10 - 2/10")

    def test_update_1attrs(self):
        r1 = Rectangle(10, 10, 10, 10)
        r1.update(89)
        self.assertEqual(str(r1), "[Rectangle] (89) 10/10 - 10/10")
# ***************************************************************************
# Test the update method in case of key-worded arguments

    def test_update_1attrs(self):
        r1 = Rectangle(10, 10, 10, 10)
        r1.update(height=1)
        self.assertEqual(str(r1), "[Rectangle] (1) 10/10 - 10/1")

        r1.update(width=1)
        self.assertEqual(str(r1), "[Rectangle] (1) 10/10 - 1/1")

    def test_update_2arrtrs(self):
        r1 = Rectangle(10, 10, 10, 10)
        r1.update(width=1, x=2)
        self.assertEqual(str(r1), "[Rectangle] (1) 2/10 - 1/10")

        r1.update(height=5, y=3)
        self.assertEqual(str(r1), "[Rectangle] (1) 2/3 - 1/5")

    def test_update_3arrtrs(self):
        r1 = Rectangle(10, 10, 10, 10)
        r1.update(width=1, x=2, id=89)
        self.assertEqual(str(r1), "[Rectangle] (89) 2/10 - 1/10")

        r1.update(height=1, y=2, id=8)
        self.assertEqual(str(r1), "[Rectangle] (8) 2/2 - 1/1")

    def test_update_all(self):
        r1 = Rectangle(10, 10, 10, 10)
        r1.update(x=1, height=2, y=3, width=4, id=89)
        self.assertEqual(str(r1), "[Rectangle] (89) 1/3 - 4/2")
# ***************************************************************************
# Test the update method in case of key-worded and no-keyword arguments
    
    def test_update_kwargsANDargs(self):
        r1 = Rectangle(10, 10, 10, 10)
        r1.update(5, 3, width=1, x=2, id=89)
        self.assertEqual(str(r1), "[Rectangle] (5) 10/10 - 3/10")

    def test_update_kwargsANDemptyargs(self):
        r1 = Rectangle(10, 10, 10, 10)
        args = tuple()
        r1.update(*args, width=1, x=2, id=89)
        self.assertEqual(str(r1), "[Rectangle] (89) 2/10 - 1/10")
