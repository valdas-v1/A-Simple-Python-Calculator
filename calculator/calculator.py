import math


class Calculator:

    """Calculator class with methods to sum, subtract, multiply, divide square and find square root"""

    def __init__(self, memory=0):
        self.memory = memory

    def reset_memory(self):
        """
        Resets the memory back to zero
        """

        self.memory = 0

    def sum(self, a, b=None):
        """
        Returns sum of two numeric values

        Parameters:
            a (float): The number to add to
            b (float): The number to be added

        Returns:
            sum (float): The sum of the provided numbers
        """

        try:
            if b == None:
                b = self.memory

            self.memory = float(a) + float(b)
            return self.memory
        except:
            return 'Invalid input'

    def subtract(self, a, b=None):
        """
        Returns subtraction result of two numeric

        Parameters:
            a (float): The number to subtract from
            b (float): The number to subtract

        Returns:
            subtraction (float): The subtraction of the provided numbers
        """

        try:
            if b == None:
                b = a
                a = self.memory

            self.memory = float(a) - float(b)
            return self.memory
        except:
            return 'Invalid input'

    def multiply(self, a, b=None):
        """
        Returns multiplication result of two numeric values

        Parameters:
            a (float): The number to multiply
            b (float): The number to multiply by

        Returns:
            multiplication (float): The multiplication of the provided numbers
        """

        try:
            if b == None:
                b = self.memory

            self.memory = float(a) * float(b)
            return self.memory
        except:
            return 'Invalid input'

    def divide(self, a, b=None):
        """
        Returns division result of two numeric values

        Parameters:
            a (float): The number to divide
            b (float): The number to divide by

        Returns:
            division (float): The division of the provided numbers
        """

        try:
            if b == None:
                b = a
                a = self.memory

            self.memory = float(a) / float(b)
            return self.memory
        except ZeroDivisionError:
            return 'Can not divide by zero.'
        except:
            return 'Invalid input'

    def square(self, a=None):
        """
        Returns square of provided numeric value

        Parameters:
            a (float): The number to be squared

        Returns:
            square (float): The square of the provided number
        """

        try:
            if a == None:
                a = self.memory

            self.memory = float(a) ** 2
            return self.memory
        except:
            return 'Invalid input'

    def sqrt(self, a=None):
        """
        Returns square root of provided numeric value

        Parameters:
            a (float): The number to find square root of

        Returns:
            square_root (float): The square root of the provided number
        """

        try:
            if a == None:
                a = self.memory

            self.memory = math.sqrt(float(a))
            return self.memory
        except:
            return 'Invalid input'
