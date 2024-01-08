#!/usr/bin/python3
""" A function that returns same class or inherit from a class """

def is_kind_of_class(obj, a_class):
    """
    return True if the object is an instance of, or if the object is an instance of a class that inherited from, the specified class
    """
    if isinstance(obj, a_class):
        return True
    else:
        return False
