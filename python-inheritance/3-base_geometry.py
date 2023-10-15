"""Empty class BaseGeometry
"""

class BaseGeometry:
    """Empty class that serves as the base for geometry-related classes
    """
    def __dir__(self):
        return [attr for attr in dir(type(self)) if not attr.startswith('__')]