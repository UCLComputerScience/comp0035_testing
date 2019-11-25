import unittest
from test import test_calculator, test_calculator_functions


def suite():
    suite = unittest.TestSuite()
    # Alternatively you can add individual tests to the suite
    suite.addTest(unittest.makeSuite(test_calculator.TestCalculator))
    suite.addTest(unittest.makeSuite(test_calculator_functions.TestCalculatorFunctions))
    unittest.TextTestRunner(verbosity=2).run(suite)


suite()
