import math


class Calculator:

    '''Calculator class with methods to sum, subtract, multiply, divide square and find square root'''

    def sum(self, a, b):
        '''Returns sum of two numeric values'''

        try:
            return float(a) + float(b)
        except:
            return 'Invalid input'

    def subtract(self, a, b):
        '''Returns subtraction result of two numeric values'''

        try:
            return float(a) - float(b)
        except:
            return 'Invalid input'

    def multiply(self, a, b):
        '''Returns multiplication result of two numeric values'''

        try:
            return float(a) * float(b)
        except:
            return 'Invalid input'

    def divide(self, a, b):
        '''Returns division result of two numeric values'''

        try:
            return float(a) / float(b)
        except ZeroDivisionError:
            return 'Can not divide by zero.'
        except:
            return 'Invalid input'

    def square(self, a):
        '''Returns square of provided numeric value'''

        try:
            return float(a) ** 2
        except:
            return 'Invalid input'

    def sqrt(self, a):
        '''Returns square root of provided numeric value'''

        try:
            return math.sqrt(float(a))
        except:
            return 'Invalid input'
