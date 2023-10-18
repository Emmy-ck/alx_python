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
        super().integer_validator("width", self.__width)
        super().integer_validator("height", self.__height)

if __name__ == "__main__":

    r = Rectangle(4, 5)
    print(r)
    print(dir(r))
    try:
        print(r.width)
    except AttributeError as e:
        print(e)
    try:
        r.integer_validator("height", "test")
    except TypeError as e:
        print(e)
