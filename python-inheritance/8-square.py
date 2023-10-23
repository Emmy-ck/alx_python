"""Class Square that inherits from Rectangle
"""

Rectangle = __import__('7-rectangle').Rectangle

class Square(Rectangle):
    """
    Initialize a Square with a side length.

    Args:
        size (int): The side length of the square.
    """
    def __init__(self, size):
        self.integer_validator("size", size)  # Validate size as a positive integer
        super().__init__(size, size)  # Call the constructor of the base class (Rectangle)

    def area(self):
        """
        Calculate and return the area of the square.

        Returns:
            int: The area of the square.
        """
        return self.__width * self.__height  # Access the width and height from the base class

    def __str__(self):
        return "[Square] {}/{}".format(self.__width, self.__height)