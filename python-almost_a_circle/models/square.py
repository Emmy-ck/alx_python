#!/usr/bin/python3
""" Square Module
"""
from models.rectangle import Rectangle

class Square(Rectangle):
    """
    Square class that inherits from the Recctangle class.
    
    """
    
    def __init__(self, size, x=0, y=0, id=None):
        """ Initialize a Square instance

        Args:
            size (int): size of the square
            x (int): x-coordinate position of the square. Defaults to 0.
            y (int): y-coordinate position of the square. Defaults to 0.
            id (int): id for the instance. Defaults to None.
        """
        super().__init__(size, size, x, y, id)
    
    @property
    def size(self):
        """ Getter for size attribute
        """
        
    @size.setter
    def size(self, value):
        """ Setter for the size attribute
        """
        self.width = value
        self.height = value
    
    def __str__(self):
        """ 
        Returns the string representation of the Square
        """
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y, self.width)
    
if __name__ == "__main__":
    pass
