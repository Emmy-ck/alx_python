"""
Square module

This module defines a square by a private size attribute.
"""
class Square:
    """
    A class representing a square.

    Attributes:
        __size (int): The size of the square.

    Methods:
        __init__(self, size=0): Initialize a new Square instance.
        size(self): Get the size of the square.
        size(self, value): Set the size of the square.

    Raises:
        TypeError: If size is not an integer.
        ValueError: If size is less than 0.
    """

    def __init__(self, size=0):
        """
        Initialize a new Square instance.

        Args:
            size (int, optional): The size of the square. Defaults to 0.
        """
        self.__size = size

    @property
    def size(self):
        """
        Get the size of the square.

        Returns:
            int: The size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Set the size of the square.

        Args:
            value (int): The new size of the square.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value