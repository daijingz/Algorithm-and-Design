# Author: Jingze Dai
# Date: 16/02/2021
# Email Address: daij24@mcmaster.ca or david1147062956@163.com

class Tree:
    # Setting an empty tree with a central node (including values)
    def __init__(self, data):
        self.leftBranch = None
        self.rightBranch = None
        self.__data = data

    # get central node's data at the top
    def getData(self, printed=True):
        if printed:
            print(str(self.__data))
        return self.__data

    def getLeftBranch(self):
        return self.leftBranch

    def getRightBranch(self):
        return self.rightBranch

    def addBranch(self, inputData, isLeft=True, isRight=False):
        if isLeft == isRight:
            raise ValueError()
        elif type(inputData) != Tree:
            raise TypeError()

        if isLeft:
            self.leftBranch = inputData
        elif isRight:
            self.rightBranch = inputData

    def countLeaf(self):
        if self.leftBranch is None and self.rightBranch is None:
            return 1
        elif self.leftBranch is None:
            return self.rightBranch.countLeaf()

        if self.rightBranch is None:
            return self.leftBranch.countLeaf()
        else:
            return self.leftBranch.countLeaf() + self.rightBranch.countLeaf()

    def countNode(self):
        if self.leftBranch is None and self.rightBranch is None:
            return 0
        else:
            if self.leftBranch is None:
                return 1 + self.rightBranch.countNode()
            elif self.rightBranch is None:
                return 1 + self.leftBranch.countNode()
            else:
                return 1 + self.leftBranch.countNode() + self.rightBranch.countNode()

    def findDepth(self):
        if self.leftBranch is None and self.rightBranch is None:
            return 0
        elif self.leftBranch is None:
            return self.rightBranch.findDepth()

        if self.rightBranch is None:
            return self.leftBranch.findDepth()
        else:
            return 1 + max(self.leftBranch.findDepth(), self.rightBranch.findDepth())

    def sumUp(self):
        if type(self.__data) != int:
            raise TypeError()

        if self.leftBranch is None:
            output1 = 0
        else:
            output1 = self.leftBranch.sumUp()
        if self.rightBranch is None:
            output2 = 0
        else:
            output2 = self.rightBranch.sumUp()

        return output1 + self.__data + output2

    def isElement(self, data):
        if self.leftBranch is None and self.rightBranch is None:
            return data == self.__data
        else:
            if self.leftBranch is None:
                return self.rightBranch.isElement(data) and data == self.__data
            elif self.rightBranch is None:
                return self.leftBranch.isElement(data) and data == self.__data
            else:
                return self.leftBranch.isElement(data) and self.rightBranch.isElement(data) and data == self.__data

    def flattenTree(self):
        if self.leftBranch is None and self.rightBranch is None:
            return [self.__data]
        else:
            if self.leftBranch is None:
                return [self.__data] + self.rightBranch.flattenTree()
            elif self.rightBranch is None:
                return self.leftBranch.flattenTree() + [self.__data]
            else:
                return self.leftBranch.flattenTree() + [self.__data] + self.rightBranch.flattenTree()

    # rotate tree's left part with right part
    # For example
    #        1                         1
    #       /  \                     /   \
    #      2    3         ->        3     2
    #     / \  / \                 / \    / \
    #    4  5  6  7               7   6   5  4
    def rotateTree(self):
        if self.leftBranch is not None:
            self.leftBranch.rotateTree()
        else:
            self.leftBranch = None
        if self.rightBranch is not None:
            self.rightBranch.rotateTree()
        else:
            self.leftBranch = None

        leftPart = self.leftBranch
        rightPart = self.rightBranch

        self.rightBranch = leftPart
        self.leftBranch = rightPart

    # Returns all leaves at the bottom (with no branch)
    def baseLeaf(self):
        if self.leftBranch is None and self.rightBranch is None:
            return [self.__data]
        elif self.leftBranch is None:
            return self.rightBranch.baseLeaf()
        if self.rightBranch is None:
            return self.leftBranch.baseLeaf()
        else:
            return self.leftBranch.baseLeaf() + self.rightBranch.baseLeaf()
