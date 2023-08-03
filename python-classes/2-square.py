"""
Square module.

This module defines the Square class, which represents a square with a private size attribute.
"""


class Square:
    """
    This class represents a square

    Attributes:
        __size (int): Size of the square.

    Methods:
        area(self): Calculate the area of the square.
        __init__(self, size=0): Initialize the Square instance with an optional size.

    Raises:
        TypeError: If size is not an int.
        ValueError: If size is less than 0.
    """

    def __init__(self, size=0):
        """
        Initialize the Square instance with an optional size.

        Args:
            size (int, optional): Size of the square. Defaults to 0.
        
        Raises:
            TypeError: If size is not an int.
            ValueError: If size is less than 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """
        Calculate the area of the square.

        Returns:
            int: Area of the square.
        """
        return self.__size ** 2