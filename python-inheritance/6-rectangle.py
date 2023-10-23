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
        super().__init()
        self.__width = width
        self.__height = height
        
    def __str__(self):
        return f"[Rectangle] {self.__width}/{self.__height}"
    
    def area(self):
        return self.__width * self.__height
    
    def display(self):
        """Displays the rectangle using # character
        """
        for i in range(self.__height):
            print('#' * self.__width)
            
    def __str__(self):
        return f"[Rectangle] {self.__width}/{self.__height}"