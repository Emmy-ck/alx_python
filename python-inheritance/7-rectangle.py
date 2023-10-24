"""Class BaseGeometry that inherits from rectangle class
"""

BaseGeometry = __import__('6-rectangle').BaseGeometry

class Rectangle(BaseGeometry):
    """
    Initialize a Rectangle with width and height.

    Args:
        width (int): The width of the rectangle.
        height (int): The height of the rectangle.
    """

    def __init__(self, width, height):
        super().integer_validator("width", width)
        super().integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """
        Calculate and return the area of the rectangle.

        Returns:
            int: The area of the rectangle.
        """
        return self.__width * self.__height

    def __str__(self):
        return f"[Rectangle] {self.__width}/{self.__height}"
    
    # Removing the __init_subclass__ method from default method
    def __dir__(self):
        return [attribute for attribute in super().__dir__() if attribute != "__init_subclass__"]