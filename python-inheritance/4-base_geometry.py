#!/usr/bin/python3

class BaseGeometry:
    def area(self):
        """
        Public instance method to calculate the area of the geometry.

        Raises:
            Exception: This method should be implemented in the derived class.
        """
        raise Exception("area() is not implemented")

    def __dir__(self):
        return [attr for attr in dir(type(self)) if attr != '__init_subclass__']