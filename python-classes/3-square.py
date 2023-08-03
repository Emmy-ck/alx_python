"""
Square module.

This module defines the Square class, which represents a square with a private size attribute.
"""


class Square:
    """
    Represents a square with a private size attribute.

    Attributes:
        __size (int): The size of the square.

    Methods:
        __init__(self, size=0): Initialize the Square instance with an optional size.
        area(self): Calculate the area of the square.

    Properties:
        size (int): Getter and setter for the size attribute.

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
        self.__size = size

    @property
    def size(self):
        """
        Gets the size of the square.

        Returns:
            int: Size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Sets the size of the square.

        Args:
            value (int): New size value.

        Raises:
            TypeError: If size is not an int.
            ValueError: If size is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """
        Calculate area of the square.

        Returns:
            int: Area of the square.
        """
        return self.__size ** 2