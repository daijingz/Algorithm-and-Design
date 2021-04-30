# Author: Jingze Dai
# Date: 16/02/2021
# Email Address: daij24@mcmaster.ca or david1147062956@163.com

class Tree:
    # Setting an empty tree with a central node (including values)
    def __init__(self, data):
        self.__leftBranch = None
        self.__rightBranch = None
        self.__data = data

    # get central node's data at the top
    def getData(self, printed=True):
        if printed:
            print(str(self.__data))
        return self.__data

    def getLeftBranch(self):
        return self.__leftBranch

    def getRightBranch(self):
        return self.__rightBranch

    def addBranch(self, inputData, isLeft=True, isRight=False):
        if isLeft == isRight:
            raise ValueError()
        elif type(inputData) != Tree:
            raise TypeError()

        if isLeft:
            self.__leftBranch = inputData
        elif isRight:
            self.__rightBranch = inputData

    def countLeaf(self):
        if self.__leftBranch is None and self.__rightBranch is None:
            return 1
        elif self.__leftBranch is None:
            return self.__rightBranch.countLeaf()

        if self.__rightBranch is None:
            return self.__leftBranch.countLeaf()
        else:
            return self.__leftBranch.countLeaf() + self.__rightBranch.countLeaf()

    def countNode(self):
        if self.__leftBranch is None and self.__rightBranch is None:
            return 0
        else:
            if self.__leftBranch is None:
                return 1 + self.__rightBranch.countNode()
            elif self.__rightBranch is None:
                return 1 + self.__leftBranch.countNode()
            else:
                return 1 + self.__leftBranch.countNode() + self.__rightBranch.countNode()

    def findDepth(self):
        if self.__leftBranch is None and self.__rightBranch is None:
            return 0
        elif self.__leftBranch is None:
            return self.__rightBranch.findDepth()

        if self.__rightBranch is None:
            return self.__leftBranch.findDepth()
        else:
            return 1 + max(self.__leftBranch.findDepth(), self.__rightBranch.findDepth())

    def sumUp(self):
        if type(self.__data) != int:
            raise TypeError()

        if self.__leftBranch is None:
            output1 = 0
        else:
            output1 = self.__leftBranch.sumUp()
        if self.__rightBranch is None:
            output2 = 0
        else:
            output2 = self.__rightBranch.sumUp()

        return output1 + self.__data + output2

    def isElement(self, data):
        if self.__leftBranch is None and self.__rightBranch is None:
            return data == self.__data
        else:
            if self.__leftBranch is None:
                return self.__rightBranch.isElement(data) and data == self.__data
            elif self.__rightBranch is None:
                return self.__leftBranch.isElement(data) and data == self.__data
            else:
                return self.__leftBranch.isElement(data) and self.__rightBranch.isElement(data) and data == self.__data

    def flattenTree(self):
        if self.__leftBranch is None and self.__rightBranch is None:
            return [self.__data]
        else:
            if self.__leftBranch is None:
                return [self.__data] + self.__rightBranch.flattenTree()
            elif self.__rightBranch is None:
                return self.__leftBranch.flattenTree() + [self.__data]
            else:
                return self.__leftBranch.flattenTree() + [self.__data] + self.__rightBranch.flattenTree()

    # rotate tree's left part with right part
    # For example
    #        1                         1
    #       /  \                     /   \
    #      2    3         ->        3     2
    #     / \  / \                 / \    / \
    #    4  5  6  7               7   6   5  4
    def rotateTree(self):
        if self.__leftBranch is not None:
            self.__leftBranch.rotateTree()
        else:
            self.__leftBranch = None
        if self.__rightBranch is not None:
            self.__rightBranch.rotateTree()
        else:
            self.__leftBranch = None

        leftPart = self.__leftBranch
        rightPart = self.__rightBranch

        self.__rightBranch = leftPart
        self.__leftBranch = rightPart

    # Returns all leaves at the bottom (with no branch)
    def baseLeaf(self):
        if self.__leftBranch is None and self.__rightBranch is None:
            return [self.__data]
        elif self.__leftBranch is None:
            return self.__rightBranch.baseLeaf()
        if self.__rightBranch is None:
            return self.__leftBranch.baseLeaf()
        else:
            return self.__leftBranch.baseLeaf() + self.__rightBranch.baseLeaf()
