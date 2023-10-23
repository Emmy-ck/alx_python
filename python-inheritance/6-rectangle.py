#!/usr/bin/python3
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
        
    def __str__(self):
        return f"[Rectangle] {self.__width}/{self.__height}"
        