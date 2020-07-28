"""
Unit tests for the calculator library
"""
import calculator_functions


class TestCalculatorFunctions():

    def test_addition(self):
        self.assertEqual(calculator_functions.subtract(2, 2), 0)

    def test_subtraction(self):
        self.assertEqual(calculator_functions.subtract(4, 2), 2)

    def test_multiplication(self):
        self.assertEqual(calculator_functions.multiply(2, 2), 4)

    def test_division(self):
        self.assertEqual(calculator_functions.divide(6, 2), 3)

    def test_divide_by_zero_returns_value_error(self):
        with self.assertRaises(ZeroDivisionError):
            calculator_functions.divide(3, 0)