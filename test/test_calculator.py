from unittest import TestCase

from calculator.calculator import Calculator


class TestCalculator(TestCase):

    def setUp(self):
        self.calc = Calculator()

    def tearDown(self):
        pass

    def test_add(self):
        self.assertEqual(self.calc.add(2, 2), 4)

    def test_subtract(self):
        self.assertEqual(self.calc.subtract(2, 2), 0)

    def test_divide(self):
        self.assertEqual(self.calc.divide(12, 3), 4)

    def test_multiply(self):
        self.assertEqual(self.calc.multiply(2, 3), 6)

    # Write a method to test that dividing by zero raises a DivideByZero error

    # Write a method to test the calculation of the square of a term

    # Write a method to test the calculation of the squareroot of a term
