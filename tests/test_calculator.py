import pytest

from calculator.calculator import Calculator

c = Calculator()


def test_sum():
    assert c.sum(1, 1) == 2


def test_subtract():
    assert c.subtract(0, 1) == -1


def test_multiply():
    assert c.multiply(10, 0) == 0


def test_division():
    assert c.divide(1, 0) == 'Can not divide by zero.'


def test_square_root():
    assert c.sqrt(-4) == 'Invalid input'


def test_invalid_value():
    assert c.sum('a', 'b') == 'Invalid input'
    assert c.subtract('a', 'b') == 'Invalid input'
    assert c.multiply('a', 'b') == 'Invalid input'
    assert c.divide('a', 'b') == 'Invalid input'
    assert c.square('a') == 'Invalid input'
    assert c.sqrt('a') == 'Invalid input'


def test_memory():
    c.reset_memory()

    assert c.sum(0) == 0
    assert c.sum(1) == 1
    assert c.sum(1) == 2

    c.reset_memory()

    assert c.subtract(0) == 0
    assert c.subtract(1) == -1
    assert c.subtract(1) == -2

    c.reset_memory()

    assert c.multiply(1, 1) == 1
    assert c.multiply(2) == 2
    assert c.multiply(2) == 4

    c.reset_memory()

    assert c.divide(20, 2) == 10
    assert c.divide(2) == 5
    assert c.divide(5) == 1

    c.reset_memory()

    assert c.square(2) == 4
    assert c.square() == 16
    assert c.square() == 256

    c.reset_memory()

    assert c.sqrt(256) == 16
    assert c.sqrt() == 4
    assert c.sqrt() == 2
