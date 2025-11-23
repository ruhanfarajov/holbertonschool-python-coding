#!/usr/bin/python3
"""Defines a Square class with size validation and area computation."""


class Square:
    """Represents a square."""

    def __init__(self, size=0):
        """Initialize a new Square with optional size."""
        self.size = size  # Use setter to validate

    @property
    def size(self):
        """Get the current size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size of the square with validation."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Return the area of the square."""
        return self.__size * self.__size

