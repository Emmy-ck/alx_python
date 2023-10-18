#!/usr/bin/python3
"""Class BaseGeometry based on 3-base_geometry.py file
"""
class BaseGeometry:
    """Base class for geometry-related classes."""

    def __init_subclass__(cls):
        pass

    def __dir__(self):
        attributes = super().__dir__()
        used_attr = [att for att in attributes if att != "__init_subclass__"]
        return used_attr

BaseGeometry.__dir__ = lambda self: [att for att in super(BaseGeometry, self).__dir__() if att != "__init_subclass__"]

class BaseGeometryWithArea(BaseGeometry):
    def area(self):
        raise Exception("area() is not implemented")

bg = BaseGeometryWithArea()

# try:
print(bg.area())
# except Exception as e:
#     print("[{}] {}".format(e.__class__.__name__, e))