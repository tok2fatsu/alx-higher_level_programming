#!/usr/bin/python3
"""This module creates a rectangle"""

class Rectangle:
    """
    class that generate a rectangle
    """
    def __init__(self, height=0, width=0):
        """Constructor initialize the class rectangle
        Keyword Arguments:
            width {int} -- width of the rectangle (default: {0})
            height {int} -- height of the rectangle (default: {0})
        """
        self.height = height
        self.width = width

    @property
    def height(self):
        """Getter function of height
        Returns:
            int -- height of the rectangle
        """
        return self.__height

    @height.setter
    def height(self, value):
        """Setter function to height
        Arguments:
            value {int} -- [value of height]
        Raises:
            TypeError: height must be an integer
            ValueError: height must be >= 0
        """
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")

        self.__height = value

        @property
        def width(self):
            """Getter function to width
            Returns:
                int -- width of the rectangle
            """
            return self.__width

        @width.setter
        def width(self, value):
            """Setter function of width
            Arguments:
                value {int} -- value of width
            Raises:
                TypeError: width must be an integer
                ValueError: width must be >= 0
            """
            if type(value) != int:
                raise TypeError("width must be an integer")
            if value < 0:
                raise ValueError("width must be >= 0")

            self.__width = value
