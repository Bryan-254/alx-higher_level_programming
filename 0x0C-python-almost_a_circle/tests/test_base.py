#!/usr/bin/python3
"""Unittest for the Base class file"""


import unittest
from models import base
from models.base import Base
Base = Base
to_json_string = Base.to_json_string
save_to_file = Base.save_to_file
from_json_string = Base.from_json_string
create = Base.create
load_from_file = Base.load_from_file


class TestBaseClass(unittest.TestCase):

    """Class for unittest of Base class"""

    def test_documentation(self):
        """Test documentation"""

        self.assertTrue(len(base.__doc__) > 0)

    def test_class_doc(self):
        """Test documentation"""

        self.assertTrue(len(Base.__doc__) > 0)

    def test_json_string_doc(self):
        """Test documentation"""

        self.assertTrue(len(to_json_string.__doc__) > 0)

    def test_save_file(self):
        """Test documentation"""

        self.assertTrue(len(save_to_file.__doc__) > 0)

    def test_from_json(self):
        """Test documentation"""

        self.assertTrue(len(from_json_string.__doc__) > 0)

    def test_create(self):
        """Test documentation"""

        self.assertTrue(len(create.__doc__) > 0)

    def test_load_file(self):
        """Test documentation"""

        self.assertTrue(len(load_from_file.__doc__) > 0)

    def test_id(self):
        """Test ids"""

        b1 = Base()
        self.assertEqual(b1.id, 1)

        b2 = Base()
        self.assertEqual(b2.id, 2)

        b3 = Base()
        self.assertEqual(b3.id, 3)

        b4 = Base(12)
        self.assertEqual(b4.id, 12)

        b5 = Base()
        self.assertEqual(b5.id, 4)

if __name__ == '__main__':
    unittest.main()
