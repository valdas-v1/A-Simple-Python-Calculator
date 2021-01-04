import math


class Calculator:
    """Calculator class with methods to sum, subtract, multiply, divide square and find square root"""

    def sum(self, a, b):
        """
        Returns sum of two numeric values

        Parameters:
            a (float): The number to add to
            b (float): The number to be added

        Returns:
            sum (float): The sum of the provided numbers
        """

        try:
            return float(a) + float(b)
        except:
            return 'Invalid input'

    def subtract(self, a, b):
        """
        Returns subtraction result of two numeric

        Parameters:
            a (float): The number to subtract from
            b (float): The number to subtract

        Returns:
            subtraction (float): The subtraction of the provided numbers
        """

        try:
            return float(a) - float(b)
        except:
            return 'Invalid input'

    def multiply(self, a, b):
        """
        Returns multiplication result of two numeric values

        Parameters:
            a (float): The number to multiply
            b (float): The number to multiply by

        Returns:
            multiplication (float): The multiplication of the provided numbers
        """

        try:
            return float(a) * float(b)
        except:
            return 'Invalid input'

    def divide(self, a, b):
        """
        Returns division result of two numeric values

        Parameters:
            a (float): The number to divide
            b (float): The number to divide by

        Returns:
            division (float): The division of the provided numbers
        """

        try:
            return float(a) / float(b)
        except ZeroDivisionError:
            return 'Can not divide by zero.'
        except:
            return 'Invalid input'

    def square(self, a):
        """
        Returns square of provided numeric value

        Parameters:
            a (float): The number to be squared

        Returns:
            square (float): The square of the provided number
        """

        try:
            return float(a) ** 2
        except:
            return 'Invalid input'

    def sqrt(self, a):
        """
        Returns square root of provided numeric value

        Parameters:
            a (float): The number to find square root of

        Returns:
            square_root (float): The square root of the provided number
        """

        try:
            return math.sqrt(float(a))
        except:
            return 'Invalid input'
