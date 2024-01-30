#!/usr/bin/python3


import unittest
from models.base import Base


class TestBaseClass(unittest.TestCase):
    '''Test class for Base class'''

    def setUp(self):
        '''Befor each test'''
        Base._Base__nb_objects = 0

    def tearDown(self):
        '''After each test'''
        Base._Base__nb_objects = 0

    def test_id_increament(self):
        '''Testing that id is increamented each call'''
        b1 = Base()
        self.assertEqual(b1.id, 1)
        b2 = Base()
        self.assertEqual(b2.id, 2)
        b3 = Base()
        self.assertEqual(b3.id, 3)

    def test_assigningTo_id(self):
        '''Typical cases of assigning a id value when instantiation'''
        b1 = Base(12)
        self.assertEqual(b1.id, 12)
        b2 = Base(646612)
        self.assertEqual(b2.id, 646612)

    def test_raisingError(self):
        '''WE DO NOT have to test the type of id'''
        b1 = Base()
        with self.assertRaises(AttributeError):
            b1.__nb_objects
        with self.assertRaises(AttributeError):
            b1.nb_objects
