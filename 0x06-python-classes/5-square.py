#!/usr/bin/python3


class Square():

    def __init__(self, size=0):
        self.size = size

    def area(self):
        return self.__size * self.__size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if not type(value) == int:
            raise TypeError("size must be an integer")
        if (value < 0):
            raise ValueError("size must be >= 0")
        self.__size = value

    def my_print(self):
        for i in range(self.__size):
            for j in range(self.__size):
                print("#", end='')
            print("")
        if (self.__size == 0):
            print(""position must be a tuple of 2 positive integers)
