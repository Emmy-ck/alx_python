"""
Empty class definition for BaseGeometry.
"""


class metaGeometry(type):
    def __dir__(cls):
        return [attribute for attribute in super().__dir__() if attribute != '__init_subclass__']

    """This is an empty class"""
class BaseGeometry(metaclass=metaGeometry):
    """This class is empty"""
    def __dir__(cls):
        return [attribute for attribute in super().__dir__() if attribute != '__init_subclass__']