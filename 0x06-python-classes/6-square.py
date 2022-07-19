#!/usr/bin/python3


class Square():

    def __init__(self, size=0, position=(0, 0)):
        self.size = size
        self.position = position

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
            for x in range(self.__position[0]):
                print("")
            for j in range(self.__size):
                print("#", end='')
            print("")
        if (self.__size == 0):
            print("")

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if not type(value[0]) == int and type(value[1]) == int:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__posiition = value
