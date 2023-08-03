"""
This module defines the Square class.

The Square class represents a square and has a private instance attribute `__size`, which stores the size of the square.
The class provides instantiation with an optional size argument. If the size is provided, it must be an integer.
If the size is not provided, the default value is 0.

Attributes:
    __size (int): The size of the square.

Methods:
    __init__(self, size=0):
        Initializes a new Square instance with the given size (default: 0).
        Raises:
            TypeError: If the provided size is not an integer.
            ValueError: If the provided size is less than 0.
    size(self):
        Getter method to retrieve the size of the square.
        Returns:
            int: The size of the square.
    size(self, value):
        Setter method to set the size of the square.
        Args:
            value (int): The size of the square.
        Raises:
            TypeError: If the provided size is not an integer.
            ValueError: If the provided size is less than 0.
    area(self):
        Calculates the area of the square.
        Returns:
            int: The area of the square.
    my_print(self):
        Prints the square with '#' characters to the standard output.
        If the size is 0, prints an empty line.
"""


class Square:
    """
    This class represents a square.

    Attributes:
        __size (int): The size of the square.

    Methods:
        __init__(self, size=0):
            Initializes a new Square instance with the given size (default: 0).
            Raises:
                TypeError: If the provided size is not an integer.
                ValueError: If the provided size is less than 0.
        size(self):
            Getter method to retrieve the size of the square.
            Returns:
                int: The size of the square.
        size(self, value):
            Setter method to set the size of the square.
            Args:
                value (int): The size of the square.
            Raises:
                TypeError: If the provided size is not an integer.
                ValueError: If the provided size is less than 0.
        area(self):
            Calculates the area of the square.
            Returns:
                int: The area of the square.
        my_print(self):
            Prints the square with '#' characters to the standard output.
            If the size is 0, prints an empty line.
    """

    def __init__(self, size=0):
        """
        Initializes a new Square instance.

        Args:
            size (int): The size of the square.
        Raises:
            TypeError: If the provided size is not an integer.
            ValueError: If the provided size is less than 0.
        """
        self.__size = size

    @property
    def size(self):
        """
        Retrieves the size of the square.

        Returns:
            int: The size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Sets the size of the square.

        Args:
            value (int): The size of the square.
        Raises:
            TypeError: If the provided size is not an integer.
            ValueError: If the provided size is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """
        Calculates the area of the square.

        Returns:
            int: The area of the square.
        """
        return self.__size**2

    def my_print(self):
        """
        Prints the square with '#' characters to the standard output.

        If the size is 0, prints an empty line.
        """
        if self.__size == 0:
            print()
        else:
            for _ in range(self.__size):
                print("#" * self.__size)