#!/usr/bin/python3
"""Unittest for rectangle.py"""

import unittest
from models.rectangle import Rectangle

class TestRectangleClass(unittest.TestCase):
    def test_default_constructor(self):
        r1 = Rectangle(10, 2)
        self.assertEqual(r1.width, 10)
        self.assertEqual(r1.height, 2)
        self.assertEqual(r1.x, 0)
        self.assertEqual(r1.y, 0)

    def test_custom_constructor(self):
        r = Rectangle(5, 10, 1, 2, 42)
        self.assertEqual(r.id, 42)
        self.assertEqual(r.width, 5)
        self.assertEqual(r.height, 10)
        self.assertEqual(r.x, 1)
        self.assertEqual(r.y, 2)

    def test_invalid_attributes(self):
        self.assertRaises(TypeError, Rectangle, 10, "2")
        self.assertRaises(ValueError, Rectangle, -10, 2)
        self.assertRaises(TypeError, Rectangle, {10}, "2")
        self.assertRaises(ValueError, Rectangle, 10, 2, 3, -1)

if __name__ == "__main__":
    unittest.main()
