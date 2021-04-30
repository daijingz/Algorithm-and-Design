class BFS:
    def __init__(self):
        self.__node = set()
        self.__edge = []
        self.__startNode = None

    def get_node(self):
        return self.__node

    def get_edge(self):
        return self.__edge

    def get_start_node(self):
        return self.__startNode

    def empty_Graph(self):
        self.__edge = []
        self.__node = set()
        self.__startNode = None

    def add_Edge(self, tup: tuple, startNode: int):
        if len(tup) != 2:
            raise ValueError()
        elif tup[0] == tup[1]:
            raise ValueError()
        elif startNode != 0 and startNode != 1:
            raise ValueError()

        for i in self.__edge:
            if i == tup:
                raise ValueError()

        if len(self.__edge) == 0:
            self.__startNode = tup[startNode]

        self.__edge += [tup]
        self.__node.add(tup[0])
        self.__node.add(tup[1])

    def check_Available_Graph(self):
        for i in self.__node:
            count = 0
            for j in self.__edge:
                if j.count(i) > 0:
                    count += 1

            if count == 0:
                return False
        return True

    def BFS(self):
        if self.__startNode is None:
            raise ValueError()
        output = [self.__startNode]
        return output