#!/usr/bin/python3
""" return True if an object is an  instance of a class inherited """

def inherits_from(obj, a_class):
    """

    return True if an object is an instance of a class

    """
    if isinstance(obj, a_class) and type(obj) != a_class:
        return True
    else:
        return False
