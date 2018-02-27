#! /usr/bin/env python3

import unittest
import rpn

class TestBasics(unittest.TestCase):
    def test_add(self):
        result = rpn.calculate("1 1 +", output=False)
        self.assertEqual(2, result)

    def test_subtract(self):
        result = rpn.calculate("5 3 -", output=False)
        self.assertEqual(2, result,)

    def test_multiply(self):
        result = rpn.calculate("5 3 *", output=False)
        self.assertEqual(15, result)

    def test_true_divide(self):
        result = rpn.calculate("6 3 /", output=False)
        self.assertEqual(2, result)

    def test_floor_divide(self):
        self.assertEqual(2, rpn.calculate("9 4 //", output=False))

    def test_expon(self):
        self.assertEqual(81, rpn.calculate("3 4 ^", output=False))
        self.assertEqual(0, rpn.calculate("0 1 ^", output=False))
        self.assertEqual(144, rpn.calculate("12 2 ^", output=False))
        self.assertEqual(169, rpn.calculate("13 2 ^", output=False))
        self.assertEqual(256, rpn.calculate("2 8 ^", output=False))

    # Implement and, or, and neg
    def test_bitwise_and(self):
        self.assertEqual(0, rpn.calculate("0 0 &", output=False))
        self.assertEqual(7, rpn.calculate("7 15 &", output=False))
        self.assertEqual(7, rpn.calculate("15 7 &", output=False))
        self.assertEqual(65535, rpn.calculate("131071 65535 &", output=False))

    def test_bitwise_or(self):
        self.assertEqual(-1, rpn.calculate("-1 0 |", output=False))
        self.assertEqual(15, rpn.calculate("7 15 |", output=False))
        self.assertEqual(15, rpn.calculate("15 7 |", output=False))
        self.assertEqual(127, rpn.calculate("63 127 |", output=False))
        self.assertEqual(31, rpn.calculate("20 11 |", output=False))

    def test_bitwise_neg(self):
        self.assertEqual(-2, rpn.calculate("-1 ~", output=False))
        self.assertEqual(-1, rpn.calculate("-2 ~", output=False))
        self.assertEqual(0, rpn.calculate("0 ~", output=False))
        self.assertEqual(101, rpn.calculate("-102 ~", output=False))

