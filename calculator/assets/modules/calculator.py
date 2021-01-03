import math

class Calculator():
    def sum(self, a, b):
        return a+b

    def subtract(self, a, b):
        return a-b

    def multiply(self, a, b):
        return a*b

    def divide(self, a, b):
        try:
            return a/b
        except ZeroDivisionError:
            return 'Can not divide by zero.'

    def sqrt(self, a):
        try:
            return math.sqrt(a)
        except:
            return 'invalid input'