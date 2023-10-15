""" Function that returns True if object is instace of lass, directly or indirectly, from specified class
"""

def inherits_from(obj, a_class):
    """Check if object is an instance of a class that inherited
    (directly or indirectly) from the specified class

    Args:
        obj: Object to be checked
        a_class: Class to check if object inherits from

    Returns:
        True: If object is an instance of a class that inherited from a_class, else False
    """
    return issubclass(type(obj), a_class)