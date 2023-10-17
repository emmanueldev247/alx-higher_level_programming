#!/usr/bin/python3
"""Unittest for base.p.py"""

import unittest
from models.base import Base


class TestBaseClass(unittest.TestCase):
    def test_auto_id_increment(self):
        b1 = Base()
        b2 = Base()
        b3 = Base()

        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 2)
        self.assertEqual(b3.id, 3)

    def test_custom_id(self):
        b4 = Base(10)
        b5 = Base(20)

        self.assertEqual(b4.id, 10)
        self.assertEqual(b5.id, 20)


if __name__ == "__main__":
    unittest.main()
