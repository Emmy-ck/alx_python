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

        super().__init__(size, size)  # Call the constructor of the base class (Rectangle)
        self.__width = size # set private width attribute
    def area(self):
        """
        Calculate and return the area of the square.

        Returns:
            int: The area of the square.
        """
        return self.__width * self.__width  # Since it's a square, width and height are the same
    def __str__(self):
        return f"[Retangle] {self._size}/{self._size}"
    def __dir__(cls):
         return [attribute for attribute in
                super().__dir__() if attribute != '__init_subclass__']