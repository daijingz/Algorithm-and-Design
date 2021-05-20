# Author: Jingze Dai
# Date: 16/02/2021
# Email Address: daij24@mcmaster.ca or david1147062956@163.com

class InappropriateNode(Exception):
    pass


class UndirectedGraph:
    def __init__(self):
        self.__startNode = None
        self.__node = []
        self.__body = []

    def __str__(self):
        str1 = "Undirected graph with start node " + str(self.getStartNode())
        str2 = ", which has length " + str(len(self))
        str3 = " with nodes " + str(self.getNode())
        str4 = " with body " + str(self.getBody())
        return str1 + str2 + str3 + str4

    def __len__(self):
        try:
            return len(self.getBody())
        except:
            raise Exception()

    def getStartNode(self):
        if self.getStartNode() is not None:
            return self.getStartNode()
        else:
            raise Exception()

    def getNode(self):
        try:
            return self.__node
        except:
            raise Exception()

    def getBody(self):
        try:
            return self.__body
        except:
            raise Exception()

    def setStartNode(self, str1: str):
        if len(str1) > 5:
            raise InappropriateNode()
        elif len(str1) == 0:
            raise InappropriateNode()
        self.__startNode = str1

    def addNode(self, node: str):
        if len(node) > 5:
            raise InappropriateNode()
        elif len(node) == 0:
            raise InappropriateNode()
        elif self.__node.count(node) == 0:
            self.__node += [node]

    def addEdge(self, edge: tuple):
        if len(edge) != 2:
            raise ValueError()
        self.addNode(edge[0])
        self.addNode(edge[1])
        if self.__node.count(edge[0]) == 0 or self.__node.count(edge[1]) == 0:
            self.__body += [edge]

    def emptyGraph(self):
        self.__startNode = None
        self.__node = []
        self.__body = []


class DirectedGraph:
    def __init__(self):
        self.__startNode = None
        self.__node = []
        self.__body = []

    def __str__(self):
        str1 = "Directed graph with start node " + str(self.getStartNode())
        str2 = ", which has length " + str(len(self))
        str3 = " with nodes " + str(self.getNode())
        str4 = " with body " + str(self.getBody())
        return str1 + str2 + str3 + str4

    def __len__(self):
        try:
            return len(self.getBody())
        except:
            raise Exception()

    def getStartNode(self):
        if self.getStartNode() is not None:
            return self.getStartNode()
        else:
            raise Exception()

    def getNode(self):
        try:
            return self.__node
        except:
            raise Exception()

    def getBody(self):
        try:
            return self.__body
        except:
            raise Exception()

    def setStartNode(self, str1: str):
        if len(str1) > 5:
            raise InappropriateNode()
        elif len(str1) == 0:
            raise InappropriateNode()
        self.__startNode = str1

    def addNode(self, node: str):
        if len(node) > 5:
            raise InappropriateNode()
        elif len(node) == 0:
            raise InappropriateNode()
        elif self.__node.count(node) == 0:
            self.__node += [node]

    def addEdge(self, edge: tuple):
        if len(edge) != 2:
            raise ValueError()
        self.addNode(edge[0])
        self.addNode(edge[1])
        if self.__node.count(edge[0]) == 0 or self.__node.count(edge[1]) == 0:
            self.__body += [edge]

    def emptyGraph(self):
        self.__startNode = None
        self.__node = []
        self.__body = []