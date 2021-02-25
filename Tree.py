# Author: Jingze Dai
# Date: 16/02/2021
# Email Address: daij24@mcmaster.ca or david1147062956@163.com

class Tree:
    def __init__(self, data):
        self.leftBranch = None
        self.rightBranch = None
        self.data = data

    def getData(self):
        return self.data

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
        if type(self.data) != int:
            raise TypeError()

        if self.leftBranch is None:
            output1 = 0
        else:
            output1 = self.leftBranch.sumUp()
        if self.rightBranch is None:
            output2 = 0
        else:
            output2 = self.rightBranch.sumUp()

        return output1 + self.data + output2

    def isElement(self, data):
        if self.leftBranch is None and self.rightBranch is None:
            return data == self.data
        else:
            if self.leftBranch is None:
                return self.rightBranch.isElement(data) and data == self.data
            elif self.rightBranch is None:
                return self.leftBranch.isElement(data) and data == self.data
            else:
                return self.leftBranch.isElement(data) and self.rightBranch.isElement(data) and data == self.data

    def flattenTree(self):
        if self.leftBranch is None and self.rightBranch is None:
            return [self.data]
        else:
            if self.leftBranch is None:
                return [self.data] + self.rightBranch.flattenTree()
            elif self.rightBranch is None:
                return self.leftBranch.flattenTree() + [self.data]
            else:
                return self.leftBranch.flattenTree() + [self.data] + self.rightBranch.flattenTree()

    def rotateTree(self):
        if self.leftBranch is not None:
            self.leftBranch.rotateTree()
        if self.rightBranch is not None:
            self.rightBranch.rotateTree()

        leftPart = self.leftBranch
        rightPart = self.rightBranch

        self.rightBranch = leftPart
        self.leftBranch = rightPart