# Author: Jingze Dai
# Email Address: daij24@mcmaster.ca or david1147062956@163.com
# Github: https://github.com/daijingz
# Linkedin: https://www.linkedin.com/in/jingze-dai/
# Description: Tree

class Tree:
    def __init__(self, data: int):
        """! Setting an empty tree with a central node (including values) """
        self.__leftBranch = None
        self.__rightBranch = None
        self.__data = data

    def __abs__(self):
        """! Finding sum of leaves' value """
        if self is None:
            return 0
        elif self.__leftBranch is None:
            return self.__data + abs(self.getLeftBranch())
        elif self.__rightBranch is None:
            return self.__data + abs(self.getRightBranch())
        else:
            return self.__data + abs(self.getLeftBranch()) + abs(self.getRightBranch())

    def __len__(self):
        """! Count node amount """
        if self.__leftBranch is None and self.__rightBranch is None:
            return 0
        else:
            if self.__leftBranch is None:
                return 1 + self.__rightBranch.countNode()
            elif self.__rightBranch is None:
                return 1 + self.__leftBranch.countNode()
            else:
                return 1 + self.__leftBranch.countNode() + self.__rightBranch.countNode()

    def treeType(self):
        """! Finding tree types """
        if self.__leftBranch is None and self.__rightBranch is None:
            return type(self.__data)
        return None

    def __repr__(self):
        """! Return a printable representation of object """
        return str(self)

    def __str__(self):
        """! Give a description string about functions """
        if self.__leftBranch is None and self.__rightBranch is None:
            return "( " + str(self.__data) + " )"
        elif self.__leftBranch is None:
            return "( " + str(self.__data) + " " + str(self.__rightBranch) + " )"
        elif self.__rightBranch is None:
            return "( " + str(self.__leftBranch) + " " + str(self.__data) + " )"
        else:
            return "( " + str(self.__leftBranch) + " " + str(self.__data) + " " + str(self.__rightBranch) + " )"

    def getData(self):
        """! Get central node's data at the top """
        try:
            return self.__data
        except:
            raise Exception

    def getLeftBranch(self):
        """! Get left branch part of a branch """
        try:
            return self.__leftBranch
        except:
            raise Exception

    def getRightBranch(self):
        """! Get right branch part of a branch """
        try:
            return self.__rightBranch
        except:
            raise Exception

    def addBranch(self, inputData, isLeft=True, isRight=False):
        """! Add branch to the tree """
        if isLeft == isRight:
            raise ValueError()
        elif type(inputData) != Tree:
            raise TypeError()

        if isLeft:
            self.__leftBranch = inputData
        elif isRight:
            self.__rightBranch = inputData

    def countLeaf(self):
        """! Count leaf amount """
        if self.__leftBranch is None and self.__rightBranch is None:
            return 1
        elif self.__leftBranch is None:
            return self.__rightBranch.countLeaf()

        if self.__rightBranch is None:
            return self.__leftBranch.countLeaf()
        else:
            return self.__leftBranch.countLeaf() + self.__rightBranch.countLeaf()

    def countNode(self):
        """! Count node amount """
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
        """! Find depth of tree """
        if self.__leftBranch is None and self.__rightBranch is None:
            return 0
        elif self.__leftBranch is None:
            return self.__rightBranch.findDepth()

        if self.__rightBranch is None:
            return self.__leftBranch.findDepth()
        else:
            return 1 + max(self.__leftBranch.findDepth(), self.__rightBranch.findDepth())

    def sumUp(self):
        """! Sum up all elements in the tree """
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
        """! Check whether a leaf is a part of tree or not """
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
        """! Flatten a tree into a list """
        if self.__leftBranch is None and self.__rightBranch is None:
            return [self.__data]
        else:
            if self.__leftBranch is None:
                return [self.__data] + self.__rightBranch.flattenTree()
            elif self.__rightBranch is None:
                return self.__leftBranch.flattenTree() + [self.__data]
            else:
                return self.__leftBranch.flattenTree() + [self.__data] + self.__rightBranch.flattenTree()

    # For example
    #        1                         1
    #       /  \                     /   \
    #      2    3         ->        3     2
    #     / \  / \                 / \    / \
    #    4  5  6  7               7   6   5  4
    def rotateTree(self):
        """! Rotate tree's left part with right part """
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

    def baseLeaf(self):
        """! Returns all leaves at the bottom (with no branch) """
        if self.__leftBranch is None and self.__rightBranch is None:
            return [self.__data]
        elif self.__leftBranch is None:
            return self.__rightBranch.baseLeaf()
        if self.__rightBranch is None:
            return self.__leftBranch.baseLeaf()
        else:
            return self.__leftBranch.baseLeaf() + self.__rightBranch.baseLeaf()