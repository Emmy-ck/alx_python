"""
Square module

This module defines a square by a private size attribute.
"""
class Square:
    """Represents a square with a private size attribute.

    Attributes:
        __size (int): The size of the square.

    Methods:
        __init__(self, size=0): Initialize the Square instance with an optional size.
        area(self): Calculate the area of the square.

    Raises:
        TypeError: If the size is not an integer.
        ValueError: If the size is less than 0.
    """

    def __init__(self, size=0):
        """Initialize the Square instance with an optional size.

        Args:
            size (int, optional): The size of the square. Defaults to 0.
        
        Raises:
            TypeError: If the size is not an integer.
            ValueError: If the size is less than 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Calculate the area of the square.

        Returns:
            int: The area of the square.
        """
        return self.__size ** 2