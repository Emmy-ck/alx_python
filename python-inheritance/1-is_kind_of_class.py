"""Function that returns True if object is an instance of class inheried from
"""

def is_kind_of_class(obj, a_class):
    """Check if an object is an instance of, or if the object
    is an instance of the class inherited from    

    Args:
        obj: Object to be checked
        a_class: Class to check against
    
    Returns:
        True: If obj is an instance of a_class or inherits from it, else False
    """
    return isinstance(obj, a_class)