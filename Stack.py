# Author: Jingze Dai
# Date: 16/02/2021
# Email Address: daij24@mcmaster.ca or david1147062956@163.com
from enum import Enum


class Behaviour(Enum):
    ADD = 1
    SUB = 2
    MUL = 3
    DIV = 4
    MOD = 5
    EXP = 6
    INTDIV = 7
    AND = 8
    OR = 9
    NOT = 10
    IFTHENELSE = 11


class Stack:
    # Object Constructor (Setting an empty stack)
    def __init__(self):
        # Setting up Empty body
        self.__body = []
        # Setting up type
        self.__type = ()

    # Getters for returning objects' bodies
    def getBody(self):
        return self.__body

    # Getters for returning objects' types
    def getType(self):
        return self.__type

    # Function on checking whether a stack is an empty stack
    def empty(self):
        return len(self.getBody()) == 0

    # Return size of stacks
    def size(self):
        return len(self.getBody())

    def push(self, element):
        self.__body += [element]
        self.__type = (str(type(element)), self.__type)

    def pop(self):
        print("Deleted" + str(self.__body[-1]))
        self.__body = self.__body[:-1]
        self.__type = self.__type[1]