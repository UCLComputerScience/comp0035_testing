import pytest
from calculator.calculator import Calculator

# Fixtures
@pytest.fixture
def calculator():
    return Calculator()


def test_add(calculator):
    assert calculator.add(2, 2) == 4


def test_subtract(calculator):
    assert calculator.subtract(2, 2) == 0


def test_divide(calculator):
    assert calculator.divide(12, 3) == 4


def test_divide_by_zero_returns_value_error(calculator):
    with pytest.raises(ZeroDivisionError):
        calculator.divide(3, 0)


def test_multiply(calculator):
    assert calculator.multiply(2, 3) == 6


if __name__ == '__main__':
    pytest.main([__file__])
