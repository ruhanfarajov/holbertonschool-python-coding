#!/usr/bin/python3
"""Defines a square class"""


class Square:
    """Represents a Square"""
    def __init__(self, size=0):
        """Initialize a new square with validation"""

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be positive")
        self.__size = size
