# Author: Jingze Dai
# Email Address: daij24@mcmaster.ca or david1147062956@163.com
# Github: https://github.com/daijingz
# Linkedin: https://www.linkedin.com/in/jingze-dai/
# Description: Graph implementation 1

class InappropriateNode(Exception):
    """! Exception when we have inappropriate nodes"""
    pass


class UndirectedGraph:
    def __init__(self):
        """! The UndirectedGraph class initializer.
        @return  An empty undirected graph object
        """
        self.__startNode = None
        self.__node = []
        self.__body = []

    def __repr__(self):
        """! Return a printable representation of object """
        return str(self)

    def __str__(self):
        """! Return a description string of the current object"""
        str1 = "Undirected graph with start node " + str(self.getStartNode())
        str2 = ", which has length " + str(len(self))
        str3 = " with nodes " + str(self.getNode())
        str4 = " with body " + str(self.getBody())
        return str1 + str2 + str3 + str4

    def __len__(self):
        """! Return the length of object"""
        try:
            return len(self.getBody())
        except:
            raise Exception()

    def getStartNode(self):
        """! Return the start node"""
        if self.getStartNode() is not None:
            return self.getStartNode()
        else:
            raise Exception()

    def getNode(self):
        """! Return the node list of object"""
        try:
            return self.__node
        except:
            raise Exception()

    def getBody(self):
        """! Return body values of object"""
        try:
            return self.__body
        except:
            raise Exception()

    def setStartNode(self, str1: str):
        """! Change the start node"""
        if len(str1) > 5:
            raise InappropriateNode()
        elif len(str1) == 0:
            raise InappropriateNode()
        self.__startNode = str1

    def addNode(self, node: str):
        """! Add new node to the node list"""
        if len(node) > 5:
            raise InappropriateNode()
        elif len(node) == 0:
            raise InappropriateNode()
        elif self.__node.count(node) == 0:
            self.__node += [node]

    def addEdge(self, edge: tuple):
        """! Add edge to the body"""
        if len(edge) != 2:
            raise ValueError()
        self.addNode(edge[0])
        self.addNode(edge[1])
        if self.__node.count(edge[0]) == 0 or self.__node.count(edge[1]) == 0:
            self.__body += [edge]

    def emptyGraph(self):
        """! Empty the object's graph"""
        self.__startNode = None
        self.__node = []
        self.__body = []


class DirectedGraph:
    def __init__(self):
        """! The DirectedGraph class initializer.
        @return  An empty directed graph object
        """
        self.__startNode = None
        self.__node = []
        self.__body = []

    def __str__(self):
        """! Return a description string of the current object"""
        str1 = "Directed graph with start node " + str(self.getStartNode())
        str2 = ", which has length " + str(len(self))
        str3 = " with nodes " + str(self.getNode())
        str4 = " with body " + str(self.getBody())
        return str1 + str2 + str3 + str4

    def __len__(self):
        """! Return the length of object"""
        try:
            return len(self.getBody())
        except:
            raise Exception()

    def getStartNode(self):
        """! Return the start node"""
        if self.getStartNode() is not None:
            return self.getStartNode()
        else:
            raise Exception()

    def getNode(self):
        """! Return the node list of object"""
        try:
            return self.__node
        except:
            raise Exception()

    def getBody(self):
        """! Return body values of object"""
        try:
            return self.__body
        except:
            raise Exception()

    def setStartNode(self, str1: str):
        """! Change the start node"""
        if len(str1) > 5:
            raise InappropriateNode()
        elif len(str1) == 0:
            raise InappropriateNode()
        self.__startNode = str1

    def addNode(self, node: str):
        """! Add new node to the node list"""
        if len(node) > 5:
            raise InappropriateNode()
        elif len(node) == 0:
            raise InappropriateNode()
        elif self.__node.count(node) == 0:
            self.__node += [node]

    def addEdge(self, edge: tuple):
        """! Add edge to the body"""
        if len(edge) != 2:
            raise ValueError()
        self.addNode(edge[0])
        self.addNode(edge[1])
        if self.__node.count(edge[0]) == 0 or self.__node.count(edge[1]) == 0:
            self.__body += [edge]

    def emptyGraph(self):
        """! Empty the object's graph"""
        self.__startNode = None
        self.__node = []
        self.__body = []