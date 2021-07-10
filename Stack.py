# Author: Jingze Dai
# Email Address: daij24@mcmaster.ca or david1147062956@163.com
# Github: https://github.com/daijingz
# Linkedin: https://www.linkedin.com/in/jingze-dai/
# Description: Self database 1: Stack

class Stack:
    def __init__(self):
        """! Initializes the program.

        @param body     stock body (empty value)

        """
        self.__body = []

    def getBody(self):
        """! Getters for returning objects' bodies"""
        try:
            return self.__body
        except:
            raise Exception()

    def appendBody(self, list1: list):
        """! Appending new lists into objects' bodies"""
        try:
            self.__body += list1
        except:
            raise Exception()

    def isEmpty(self):
        """! Checking whether a stack is an empty stack"""
        try:
            return len(self.getBody()) == 0
        except:
            raise Exception()

    def makeEmpty(self):
        """! Make a stack becomes an empty stack"""
        try:
            self.__body = []
        except:
            raise Exception()

    def size(self):
        """! Return size of stacks"""
        try:
            return len(self.getBody())
        except:
            raise Exception()

    def push(self, element):
        """! Push an element to stack"""
        if type(element) == list:
            raise TypeError()
        elif element is None:
            raise ValueError()
        self.__body += [element]

    def pop(self):
        """! Delete an element from stack and return it"""
        if len(self.__body) == 0:
            raise Exception("Error: Underflow")
        self.__body = self.__body[:-1]
        return self.__body[-1]

    def delete(self):
        """! Delete an element from stack"""
        if len(self.__body) == 0:
            raise Exception("Error: Underflow")
        self.__body = self.__body[:-1]


class AdvancedStack:
    def __init__(self):
        self.__body = []
        self.__boolean = 0
        self.__digit = 0
        self.__string = 0

    def get_body(self):
        try:
            return self.__body
        except:
            raise Exception()

    def get_boolean(self):
        try:
            return self.__boolean
        except:
            raise Exception()

    def get_digit(self):
        try:
            return self.__digit
        except:
            raise Exception()

    def get_string(self):
        try:
            return self.__string
        except:
            raise Exception()