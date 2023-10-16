#!/usr/bin/python3
"""Empty class BaseGeometry"""
class BaseGeometry:
    """Empty class that serves as the base for geometry-related classes"""
    def __init_subclass__(cls):
        pass

    def __dir__(self):
        return [att for att in dir(type(self)) if att != "__init_subclass__"]
    
    def __class__(self):
        return type(self)

BaseGeometry.__dir__ = lambda self: [att for att in super(BaseGeometry, self).__dir__() if att != "__init_subclass__"]
