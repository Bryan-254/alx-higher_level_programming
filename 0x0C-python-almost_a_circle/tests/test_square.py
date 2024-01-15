#!/bin/usr/python3
"""
Unittest for Square
"""
import unittest
from models.square import Square


class TestSquare(unittest.TestCase):
    """
    Class for unittest of Square class
    """

    def setUp(self):
        self.square = Square(5, 2, 3, 1)

    def test_constructor(self):
        self.assertEqual(self.square.width, 5)
        self.assertEqual(self.square.height, 5)
        self.assertEqual(self.square.x, 2)
        self.assertEqual(self.square.y, 3)
        self.assertEqual(self.square.id, 1)

    def test_str_method(self):
        self.assertEqual(str(self.square), "[Square] (1) 2/3 - 5")

    def test_size_property(self):
        self.assertEqual(self.square.size, 5)

        self.square.size = 8
        self.assertEqual(self.square.size, 8)
        self.assertEqual(self.square.width, 8)
        self.assertEqual(self.square.height, 8)

    def test_update_method(self):
        self.square.update(10, 4, 5, 2)
        self.assertEqual(str(self.square), "[Square] (10) 4/5 - 2")

        self.square.update(size=7, x=3)
        self.assertEqual(str(self.square), "[Square] (10) 3/5 - 7")

    def test_to_dictionary_method(self):
        square_dict = self.square.to_dictionary()
        expected_dict = {'id': 1, 'size': 5, 'x': 2, 'y': 3}
        self.assertEqual(square_dict, expected_dict)

if __name__ == '__main__':
    unittest.main()
