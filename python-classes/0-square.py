#!/usr/bin/python3
"""
This module defines a Square class with private size attribute.
"""
class Square:
    """
    A class that defines a square by its size.

    Attributes:
        __size (int): The size of the square (private)
    """
    def __init__(self, size):
        """
        Initializes a new Square instance.

        Args:
            size (int): The size of the square
        """
        self.__size = size
