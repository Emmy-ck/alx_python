class BaseGeometry:
    """Empty class that serves as the base for geometry-related classes"""
    def __init_subclass__(cls):
        pass

    def __dir__(self):
        attributes = super().__dir__()
        used_attr = [att for att in attributes if att != "__init_subclass__"]
        return used_attr

# You can also override __dir__ for the BaseGeometry class
BaseGeometry.__dir__ = lambda self: [att for att in super(BaseGeometry, self).__dir__() if att != "__init_subclass__"]
