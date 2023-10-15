"""Function that returns True if object is exactly an instance of specified class, else False
"""

def is_same_class(obj, a_class):
    """Check if object is exactly an instance of the specified class

    Args:
        obj: Object to be checked
        a_class: Class to check the object against

    Returns:
        True: if object is an instance of a_class, else False
    """
    return type(obj) is a_class