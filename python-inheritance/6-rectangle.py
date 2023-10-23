"""Class rectangle that inherits from BaseGeometry class
"""


BaseGeometry = __import__('5-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    Initialize a Rectangle with width and height.

    Args:
        width (int): The width of the rectangle.
        height (int): The height of the rectangle.
    """
    def __init__(self, width, height):
        self.__width = width
        self.__height = height
        self.integer_validator("width", self.__width)
        self.integer_validator("height", self.__height)
        
    def __dir__(self):
        return [attr for attr in dir(type(self)) if attr != '__init_subclass__']