# Author: Jingze Dai
# Date: 16/02/2021
# Email Address: daij24@mcmaster.ca or david1147062956@163.com
from collections import defaultdict


class Graph:
    def __init__(self, directed: bool):
        """!
        @return a graph object with 3 state variables
        """
        self.__node = []
        self.__edge = defaultdict(list)
        self.__directed = directed

    def get_node(self):
        """! Getters of object's node values """
        try:
            return self.__node
        except:
            raise Exception()

    def get_edge(self):
        """! Getters of object's edge values """
        try:
            return self.__edge
        except:
            raise Exception()

    def get_directed(self):
        """! Getters of object's directed values  """
        try:
            return self.__directed
        except:
            raise Exception()

    def get_length(self):
        """! Getters of object's node amount """
        try:
            return len(self.__node)
        except:
            raise Exception()

    def get_complexity(self):
        """! Getters of object's edge amount """
        try:
            return len(self.__edge)
        except:
            raise Exception()

    def add_edge(self, edge: tuple):
        """! Add edges to this graph """
        if len(edge) != 2:
            raise Exception()
        if self.__node.count(edge[0]) == 0:
            self.__node += [edge[0]]
        elif self.__node.count(edge[1]) == 0:
            self.__node += [edge[1]]

        if not self.get_directed():
            if self.__edge[edge[0]].count(edge[1]) == 0:
                self.__edge[edge[0]].append(edge[1])
            if self.__edge[edge[1]].count(edge[0]) == 0:
                self.__edge[edge[1]].append(edge[0])
        else:
            if self.__edge[edge[0]].count(edge[1]) == 0:
                self.__edge[edge[0]].append(edge[1])

    def DFSSub(self, v, s, visited):
        """! DFS helper function """
        visited.add(v)
        s += [v]

        for neighbour in self.__edge[v]:
            if neighbour not in visited:
                self.DFSSub(neighbour, s, visited)

    def DFS(self, v):
        """! Depth First Search """
        if self.get_node().count(v) == 0:
            raise Exception()
        visited = set()
        s = []
        self.DFSSub(v, s, visited)
        return s