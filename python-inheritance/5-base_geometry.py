"""Class BaseGeometry with two public instance classes
"""
class BaseGeometry:
    """
    Public instance method to calculate the area of the geometry.

    Raises:
        Exception: This method should be implemented in the derived class.
    """
    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Public instance method to validate an integer value.

        Args:
            name (str): The name of the value.
            value (int): The value to be validated.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than or equal to 0.
        """
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")

    # def __dir__(self):
    #     return [attr for attr in dir(type(self)) if attr != '__init_subclass__']