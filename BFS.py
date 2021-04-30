class BFS:
    def __init__(self):
        self.node = set()
        self.edge = []

    def get_node(self):
        return self.node

    def get_edge(self):
        return self.edge

    def add_Edge(self, tup: tuple):
        if len(tup) != 2:
            raise ValueError()
        elif self.edge.count(tup[0]) > 0 and self.edge.count(tup[1]) > 0:
            raise ValueError()
        elif tup[0] == tup[1]:
            raise ValueError()

        self.edge += [tup]
        self.node.add(tup[0])
        self.node.add(tup[1])

    def check_Available_Graph(self):
        for i in self.node:
            count = 0
            for j in self.edge:
                if j.count(i) > 0:
                    count += 1

            if count == 0:
                return False
        return True