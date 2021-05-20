# Author: Jingze Dai
# Date: 16/02/2021
# Email Address: daij24@mcmaster.ca or david1147062956@163.com

class NotAvailableValues(Exception):
    pass


class WrongIndex(Exception):
    pass


class SNode:
    def __init__(self, element=None):
        self.__data = element
        self.__nextData = None

    def setData(self, data=None):
        self.__data = data

    def setNextData(self, nextData=None):
        self.__nextData = nextData

    def getData(self):
        return self.__data

    def getNextData(self):
        return self.__nextData


class SingleLinkedList:
    def __init__(self):
        self.__length = 0
        self.__body = [SNode()]

    def setLength(self, amount: int):
        if amount == 0:
            raise NotAvailableValues()
        self.__length = self.__length + amount

    def getLength(self):
        return self.__length

    def getBody(self):
        return self.__body

    def getRealBody(self):
        return self.__body[:-1]

    def append(self, node: SNode):
        if node.getData() is None:
            raise NotAvailableValues()
        node.setNextData(self.__body[1].getData())
        self.__body = [node] + self.__body
        self.setLength(1)

    def insert(self, index: int, node: SNode):
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


class DBegin:
    def __init__(self):
        self.__data = None
        self.__nextData = None

    def setNextData(self, data):
        self.__nextData = data

    def getData(self):
        return self.__data

    def getNextData(self):
        return self.__nextData


class DEnd:
    def __init__(self):
        self.__data = None
        self.__prevData = None

    def setPrevData(self, data):
        self.__prevData = data

    def getData(self):
        return self.__data

    def getPrevData(self):
        return self.__prevData


class DNode:
    def __init__(self):
        self.__data = None
        self.__prevData = None
        self.__nextData = None

    def getData(self):
        return self.__data

    def getPrevData(self):
        return self.__prevData

    def getNextData(self):
        return self.__nextData

    def setData(self, data):
        self.__data = data

    def setPrevData(self, data):
        self.__prevData = data

    def setNextData(self, data):
        self.__nextData = data