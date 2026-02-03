def is_kind_of_class(obj, a_class):
    """Checks if an object is an instance of a class or its subclass.

    Args:
        obj (any): The object to check.
        a_class (type): The class to compare against.

    Returns:
        bool: True if obj is an instance of a_class or its subclass, False otherwise.
    """
    return isinstance(obj, a_class)
