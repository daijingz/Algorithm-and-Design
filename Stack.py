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

    def empty(self):
        """! Checking whether a stack is an empty stack"""
        try:
            return len(self.getBody()) == 0
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
        self.__body += [element]

    def pop(self):
        """! Delete an element from stack and return it"""
        if len(self.__body) == 0:
            raise Exception("Error: Underflow")
        self.__body = self.__body[:-1]
        return self.__body[-1]


class A(enumerate):
    Add = 1
    Sub = 2


class NoneOfTypes(Exception):
    pass


class AStack:
    def __init__(self, input1):
        self.__body = []

        if type(input1) == str:
            self.__unitType = 'str'
        elif type(input1) in [int, float]:
            self.__unitType = 'num'
        elif type(input1) == bool:
            self.__unitType = 'bool'
        else:
            raise NoneOfTypes()

        self.__type = None

    def get_body(self):
        try:
            return self.__body
        except:
            raise Exception

    def get_unitType(self):
        try:
            return self.__unitType
        except:
            raise Exception

    def get_type(self):
        try:
            return self.__type
        except:
            raise Exception