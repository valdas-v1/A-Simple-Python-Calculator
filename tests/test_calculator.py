import pytest

from calculator import Calculator

c = Calculator()

def test_sum():
    assert c.sum(1,1) == 2

def test_subtract():
    assert c.subtract(0,1) == -1

def test_multiply():
    assert c.multiply(10,0) == 0

def test_division():
    assert c.divide(1,0) == 'Can not divide by zero.'

def test_square_root():
    print(c.sqrt(-4))
    assert c.sqrt(-4) == 'Invalid input'

def test_invalid_value():
    assert c.sum('a','b') == 'Invalid input'
    assert c.subtract('a', 'b') == 'Invalid input'
    assert c.multiply('a','b') == 'Invalid input'
    assert c.divide('a','b') == 'Invalid input'
    assert c.square('a') == 'Invalid input'
    assert c.sqrt('a') == 'Invalid input'
