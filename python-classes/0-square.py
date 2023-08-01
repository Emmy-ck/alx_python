class Square:
    """
    This is a class representing a square
    
    The 'Square' class provides attributes/ methods to worl with squares
    """
    def __init__(self, size):
        self.__size = size
        """
        This initializes a new 'Square' instance with one argument.
        The argument in this instance is 'size' 
        """
    def get_size(self):
        return self.__size
        """
        This function gets the size of the square
        
        Return:
        An integer value of the square
        """
    def area(self):
        return self.__size ** 2
    
        """
        This calculated the area of the square
        
        Return:
        An integer value of the area of the square
        """
        