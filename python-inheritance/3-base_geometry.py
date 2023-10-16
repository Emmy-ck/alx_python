"""Empty class BaseGeometry
"""

class BaseGeometry:
    """Empty class that serves as the base for geometry-related classes
    """
    def _init_subclass__(cls):
        pass
    
    def __dir__(self):
        attributes = super().__dir__()
        used_attr = [att for att in attributes if att != "__init_subclass__"]
        return used_attr