#!/usr/bin/python3

"""Base module
"""
class Base:
    """
    Base class for managing id attribute in all preceding/ future classes
    """
    __nb_objects = 0
    
    def __init__(self, id=None):
        """
        Initialize a Base instance

        Args:
            id (int): Optional ID for the instance. Defaults to None.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
            
if __name__ == "__main__":
    pass