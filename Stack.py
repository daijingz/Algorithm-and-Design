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

    def setBody(self, list1: list, isAssert=False):
        """! Combining or setting new lists into objects' bodies"""
        try:
            if not isAssert:
                self.__body += list1
            elif isAssert:
                self.__body = list1
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

    def __len__(self):
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
    def __init__(self, repeated: bool):
        """! Constructor of Stack object"""
        self.__body = []
        self.__boolean = 0
        self.__digit = 0
        self.__string = 0
        self.__other = 0
        self.__repeated = repeated

    def get_body(self):
        """! Getters for returning objects' bodies"""
        try:
            return self.__body
        except:
            raise Exception()

    def get_boolean(self):
        """! Getters for returning objects' number of booleans"""
        try:
            return self.__boolean
        except:
            raise Exception()

    def get_digit(self):
        """! Getters for returning objects' number of digital numbers"""
        try:
            return self.__digit
        except:
            raise Exception()

    def get_string(self):
        """! Getters for returning objects' number of strings"""
        try:
            return self.__string
        except:
            raise Exception()

    def get_other(self):
        """! Getters for returning objects' number of other types' data"""
        try:
            return self.__other
        except:
            raise Exception()

    def get_repeated(self):
        """! Getters for returning whether an object allows repeating elements"""
        try:
            return self.__body
        except:
            raise Exception()

    def setBody(self, list1: list, isAssert=False):
        """! Combining or setting new lists into objects' bodies"""
        try:
            if not isAssert:
                self.__body += list1
            elif isAssert:
                self.__body = list1
        except:
            raise Exception()

    def isEmpty(self):
        """! Checking whether a stack is an empty stack"""
        try:
            return len(self.get_body()) == 0
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
            return len(self.get_body())
        except:
            raise Exception()

    def __len__(self):
        """! Return size of stacks"""
        try:
            return len(self.get_body())
        except:
            raise Exception()

    def push(self, element):
        """! Push an element to stack"""
        if type(element) == list:
            raise TypeError()
        elif element is None:
            raise ValueError()

        self.__body += [element]

        if type(element) in [int, float]:
            self.__digit += 1
        elif type(element) == str:
            self.__string += 1
        elif type(element) == bool:
            self.__boolean += 1
        else:
            self.__other += 1

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