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
        # if not isinstance(size, int):
        #     raise TypeError("size must be an integer")

        super().integer_validator("size", size)  # Call the constructor of the base class (Rectangle)
        self.__size = size # set private size attribute
        Square = 0

    def area(self):
        """
        Calculate and return the area of the square.

        Returns:
            int: The area of the square.
        """
        return self.__size ** 2  # Since it's a square, width and height are the same
    def __str__(self):
        return Square.area
    
    def __dir__(cls):
        return [attribute for attribute in super().__dir__()
                if attribute != "__init_subclass__"]
    # def __dir__(self):
    #     # Exclude '__init_subclass__' from the list of attributes
    #     return [attribute for attribute in super().__dir() if attribute != '__init_subclass__']

# if __name__ == "__main__":
#     attributes = dir(Square)
#     for attr in attributes:
#         print(attr)