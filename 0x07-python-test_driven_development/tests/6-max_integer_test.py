#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    '''This class to test max_integer function'''

    def testEmptyList(self):
        '''Case of empty list passed'''

        my_list = []
        self.assertAlmostEqual(max_integer(my_list), None)

    def testTypical(self):
        '''Typical case [1, 2, 3]'''

        my_list = [1, 2, 3]
        self.assertAlmostEqual(max_integer(my_list), 3)

    def testNegative(self):
        '''Case of list of negative numbers'''

        my_list = [-1, -2, -3]
        self.assertAlmostEqual(max_integer(my_list), -1)

    def testNandP(self):
        '''Case of list of negative and positive numbers'''

        my_list = [-1, -2, -3, 1, 2]
        self.assertAlmostEqual(max_integer(my_list), 2)
    
    def testListWithString(self):
        '''Case of list contain string element'''

        my_list = [1, 2, 3, "hi"]
        self.assertRaises(TypeError, max_integer, my_list)
