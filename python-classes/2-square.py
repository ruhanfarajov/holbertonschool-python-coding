#!/usr/bin/python3
"""Defines a square class"""


class Square:
    """Represents a Square"""
    def __init__(self, size=0):
        """Initialize a new square with validation"""

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Returns the areas of the square"""
        return self.__size**2
    
    def size(self):
        """Retrieves the size of the object"""
        return self.__size

    def set_size(self, name=None):
        """allows setiing size for the self__size variable"""
        self.__size = name
