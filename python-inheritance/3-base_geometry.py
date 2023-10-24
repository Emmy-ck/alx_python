"""
Empty class definition for BaseGeometry.
"""


class BaseGeometry:
    """
    Empty class representing the base geometry.
    """
    def __init_subclass__(cls):
        pass

    def __dir__(self):
        return [attr for attr in dir(self) if attr != '__init_subclass__']
