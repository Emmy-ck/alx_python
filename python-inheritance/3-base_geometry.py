"""Empty class BaseGeometry
"""

from collections.abc import Iterable


class BaseGeometry(type):
    """Empty class that serves as the base for geometry-related classes
    """
    def __dir__(self):
        attributes = super().__dir__()
        attr = [att for att in attributes if att != "__init_subclass__"]
        return attr
    
class BaseGeometry(metaclass=BaseGeometryMeta):
    """Primary class for creating geometry-related classes

    Args:
        metaclass: Defaults to BaseGeometryMeta.
    """
    
    def __dir__(self):
        attibutes = super().__dir__()
        attr = [att for att in attributes if att != "__init_subclass__"]
        return attr