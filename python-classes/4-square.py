#!/usr/bin/python3
"""Square class module"""


class Square:
    """Square class that defines a square with size validation"""

    def __init__(self, size=0):
        """
        Initialize a new Square

        Args:
            size (int): The size of the square (default is 0)
        """
        self.size = size

    @property
    def size(self):
        """Getter method for size attribute"""
        return self.__size

    @size.setter
    def size(self, value):
        """
        Setter method for size attribute with validation

        Args:
            value (int): The new size value

        Raises:
            TypeError: If value is not an integer
            ValueError: If value is less than 0
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """
        Calculate and return the area of the square

        Returns:
            int: The area of the square (size * size)
        """
        return self.__size * self.__size

    def my_print(self):
        """
        Print the square with the character #

        If size is 0, print an empty line
        """
        if self.__size == 0:
            print()
        else:
            for i in range(self.__size):
                print("#" * self.__size)
