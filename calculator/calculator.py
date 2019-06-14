"""
Calculator class containing basic math operations.
"""


class Calculator(object):
    def __init__(self):
        pass

    def add(self, first_term, second_term):
        return first_term + second_term

    def subtract(self, first_term, second_term):
        return first_term - second_term

    def divide(self, first_term, second_term):
        if second_term == 0:
            raise ZeroDivisionError("Cannot divide by zero")
        return first_term / second_term

    def multiply(self, first_term, second_term):
        return first_term * second_term
