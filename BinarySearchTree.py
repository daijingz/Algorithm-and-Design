# Author: Jingze Dai
# Email Address: daij24@mcmaster.ca or david1147062956@163.com
# Github: https://github.com/daijingz
# Linkedin: https://www.linkedin.com/in/jingze-dai/
# Description: Binary Search Tree (BST)


class BinarySearchTree:
    def __init__(self, data=None):
        if data is not None:
            if type(data) not in [int, str]:
                raise Exception()
            self.__data = data
            self.__type = type(data)
        else:
            self.__data = None
            self.__type = None

        self.__left = None
        self.__right = None

    def get_data(self):
        try:
            return self.__data
        except:
            raise Exception()

    def get_type(self):
        try:
            return self.__type
        except:
            raise Exception()

    def get_left(self):
        try:
            return self.__left
        except:
            raise Exception()

    def get_right(self):
        try:
            return self.__right
        except:
            raise Exception()

    def set_data(self, data):
        try:
            if type(data) != self.__type:
                raise Exception
            self.__data = data
        except:
            raise Exception()

    def set_type(self, new_type):
        try:
            if new_type not in [int, str]:
                raise Exception()
            self.__type = new_type
            self.__data = None
            self.__left = None
            self.__right = None
        except:
            raise Exception()

    def set_left(self, left):
        if not isinstance(left, BinarySearchTree):
            raise Exception()
        self.__left = left

    def set_right(self, right):
        if not isinstance(right, BinarySearchTree):
            raise Exception()
        self.__left = right