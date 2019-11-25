"""
Calculator class containing basic math operations.
This version introduces a sleep that would mean our code takes a long time to run.
To test this we would not wish to wait for the sleep to finish before testing, instead we will 'mock' the sleep function.
"""
import time


class Calculator(object):
    def __init__(self):
        pass

    def add(self, first_term, second_term):
        time.sleep(10)  # wait 10 seconds
        return first_term + second_term

    def subtract(self, first_term, second_term):
        time.sleep(10)
        return first_term - second_term

    def multiply(self, first_term, second_term):
        time.sleep(10)
        return first_term * second_term

    def divide(self, first_term, second_term):
        time.sleep(10)
        return first_term / second_term
