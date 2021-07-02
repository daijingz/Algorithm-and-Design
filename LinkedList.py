# Author: Jingze Dai
# Email Address: daij24@mcmaster.ca or david1147062956@163.com
# Github: https://github.com/daijingz
# Linkedin: https://www.linkedin.com/in/jingze-dai/
# Description: Linked List

class NotAvailableValues(Exception):
    """! Exception when objects have unexpected values"""
    pass


class WrongIndex(Exception):
    """! Exception when indexing has errors"""
    pass


class SettingError(Exception):
    """! Exception when setting values takes place"""
    pass


class SNode:
    def __init__(self, element=None):
        """! Initializes the program.

        @param data         current node's data
        @param nextData     next linked node's data

        """
        self.__data = element
        self.__nextData = None

    def setData(self, data=None):
        """! Setting data value"""
        try:
            self.__data = data
        except:
            raise SettingError()

    def setNextData(self, nextData=None):
        """! Setting nextData value"""
        try:
            self.__nextData = nextData
        except:
            raise SettingError()

    def getData(self):
        """! Getting data value"""
        try:
            return self.__data
        except:
            raise Exception()

    def getNextData(self):
        """! Getting nextData value"""
        try:
            return self.__nextData
        except:
            raise Exception()


class SingleLinkedList:
    def __init__(self):
        """! Initializes the program.

        @param length       length of linked list (only counts )
        @param body         linked list body

        """
        self.__length = 0
        self.__body = [SNode()]

    def setLength(self, amount: int):
        """! Setting length value"""
        try:
            if amount == 0:
                raise NotAvailableValues()
            self.__length = self.__length + amount
        except:
            raise SettingError()

    def getLength(self):
        """! Getting length value"""
        try:
            return self.__length
        except:
            raise Exception()

    def getBody(self):
        """! Setting body value"""
        try:
            return self.__body
        except:
            raise Exception()

    def getRealBody(self):
        """! Setting not-None body value"""
        try:
            return self.__body[:-1]
        except:
            raise Exception()

    def append(self, node: SNode):
        """! Adding a node at the end of linked list"""
        if node.getData() is None:
            raise NotAvailableValues()
        node.setNextData(self.__body[1].getData())
        self.__body = [node] + self.__body
        self.setLength(1)

    def insert(self, index: int, node: SNode):
        """! Adding a node in the middle of linked list"""
        if self.getLength() < 1:
            raise NotAvailableValues()
        elif index <= 0 or index >= self.getLength() + 1:
            raise WrongIndex()

        data = node.getData()
        self.getBody()[index - 1].setNextData(data)
        node.setNextData(self.getBody()[index].getData())
        newNode = self.getBody()[index]
        self.getBody()[index] = node
        self.getBody()[index + 1] = newNode

    def delete(self):
        """! Deleting a node from the end of linked list"""
        if self.getLength() == 0:
            self.__body = self.getBody()
        else:
            self.__body = self.getBody()[1:]


class DBegin:
    def __init__(self):
        self.__data = None
        self.__nextData = None

    def setNextData(self, data):
        try:
            self.__nextData = data
        except:
            raise Exception()

    def getData(self):
        try:
            return self.__data
        except:
            raise Exception()

    def getNextData(self):
        try:
            return self.__nextData
        except:
            raise Exception()


class DEnd:
    def __init__(self):
        self.__data = None
        self.__prevData = None

    def setPrevData(self, data):
        self.__prevData = data

    def getData(self):
        try:
            return self.__data
        except:
            raise Exception()

    def getPrevData(self):
        try:
            return self.__prevData
        except:
            raise Exception()


class DNode:
    def __init__(self):
        self.__data = None
        self.__prevData = None
        self.__nextData = None

    def getData(self):
        try:
            return self.__data
        except:
            raise Exception()

    def getPrevData(self):
        try:
            return self.__prevData
        except:
            raise Exception()

    def getNextData(self):
        try:
            return self.__nextData
        except:
            raise Exception()

    def setData(self, data):
        self.__data = data

    def setPrevData(self, data):
        self.__prevData = data

    def setNextData(self, data):
        self.__nextData = data


class DoubleEdgeLinkedList:
    def __init__(self, begin: DBegin, end: DEnd):
        self.__length = 0
        self.__body = []
        self.__begin = begin
        self.__end = end

    def get_length(self):
        try:
            return self.__length
        except:
            raise Exception()

    def get_body(self):
        try:
            return self.__body
        except:
            raise Exception()

    def get_begin(self):
        try:
            return self.__begin
        except:
            raise Exception()

    def get_end(self):
        try:
            return self.__end
        except:
            raise Exception()


class CNode:
    def __init__(self, value: int, nextV: int):
        self.__value = value
        self.__nextV = nextV

    def get_Value(self):
        try:
            return self.__value
        except:
            raise Exception()

    def get_nextV(self):
        try:
            return self.__nextV
        except:
            raise Exception()

    def set_Value(self, value: int):
        try:
            self.__value = value
        except:
            raise Exception()

    def set_nextV(self, nextV: int):
        try:
            self.__nextV = nextV
        except:
            raise Exception()


class CircularLinkedList:
    def __init__(self, node1: CNode, node2: CNode):
        value1 = node1.get_Value()
        value2 = node2.get_Value()
        node1.set_nextV(value2)
        node2.set_nextV(value1)
        self.__nodes = [node1, node2]

    def get_nodes(self):
        try:
            return self.__nodes
        except:
            raise Exception()