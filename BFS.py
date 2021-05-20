class WrongInput(Exception):
    pass


class WrongObjects(Exception):
    pass


class BFS:
    def __init__(self):
        self.__node = set()
        self.__edge = []
        self.__startNode = None

    def get_node(self):
        try:
            return self.__node
        except:
            raise Exception

    def get_edge(self):
        try:
            return self.__edge
        except:
            raise Exception

    def get_start_node(self):
        try:
            return self.__startNode
        except:
            raise Exception

    def empty_Graph(self):
        self.__edge = []
        self.__node = set()
        self.__startNode = None

    def add_Edge(self, tup: tuple, startNode: int):
        if len(tup) != 2:
            raise WrongInput()
        elif tup[0] == tup[1]:
            raise WrongInput()
        elif startNode != 0 and startNode != 1:
            raise WrongInput()

        for i in self.__edge:
            if i == tup:
                raise WrongInput()

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
            raise WrongInput()
        output = [self.__startNode]
        return output