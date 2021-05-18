# Author: Jingze Dai
# Date: 16/02/2021
# Email Address: daij24@mcmaster.ca or david1147062956@163.com

class Stack:
    # Object Constructor (Setting an empty stack)
    def __init__(self):
        # Setting up Empty body
        self.__body = []

    # Getters for returning objects' bodies
    def getBody(self):
        return self.__body

    # Function on checking whether a stack is an empty stack
    def empty(self):
        return len(self.getBody()) == 0

    # Return size of stacks
    def size(self):
        return len(self.getBody())

    def push(self, element):
        self.__body += [element]

    def pop(self):
        if len(self.__body) == 0:
            raise Exception("Error: Underflow")
        self.__body = self.__body[:-1]