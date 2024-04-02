# test_math_functions.py

import unittest
from math_functions import add, subtract, multiply, divide

class TestMathFunctions(unittest.TestCase):

    def test_add(self):
        self.assertEqual(add(1, 2), 3)

    def test_subtract(self):
        self.assertEqual(subtract(4, 2), 2)

    def test_multiply(self):
        self.assertEqual(multiply(3, 4), 12)

    def test_divide(self):
        self.assertEqual(divide(8, 2), 4)
        with self.assertRaises(ValueError):
            divide(8, 0)

if __name__ == '__main__':
    unittest.main()
