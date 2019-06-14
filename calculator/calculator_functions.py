"""
Calculator containing basic math operations with funcions rather than a class structure.
"""


def add(first_term, second_term):
    return first_term + second_term


def subtract(first_term, second_term):
    return first_term - second_term


def divide(first_term, second_term):
    if second_term == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    return first_term / second_term


def multiply(first_term, second_term):
    return first_term * second_term


# Write a function to calculate the square of a term (ie term * term)
# def square(term):
#    return term * term

# Write a function to calculate the square root of a term (i.e. term ** 0.5) note: ** represents power
# def square_root(term):
#    return term ** 0.5
