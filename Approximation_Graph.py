# Jingze Dai Date: 2020/09/22
# Part 3 Algorithm: Approximation Algorithm on Vertex Cover
# Undirected graphs are represented as "Approximation_Graph" object
from collections import defaultdict


class Approximation_Graph:
    def __init__(self):
        """!
        @return a graph object with bodies and nodes
        """
        self.vertices = [] # Time Complexity: O(1)
        self.graph = defaultdict(list) # Time Complexity: O(1)

    # Constructor Total Time Complexity: O(1) + O(1) = O(1)

    def get_vertices(self):
        """! Get vertices values of an object"""
        try:
            return self.vertices # Time Complexity: O(1)
        except:
            raise Exception()

    # Method Total Time Complexity: O(1)

    def get_graph(self):
        """! Get graph body values of an object"""
        try:
            return self.graph # Time Complexity: O(1)
        except:
            raise Exception()

    # Method Total Time Complexity: O(1)

    def __str__(self):
        """! Returns the string of all vertices"""
        try:
            return str(self.vertices)
        except:
            raise Exception()

    # Method Total Time Complexity: O(1)

    def __len__(self):
        """! Returns the length of all vertices"""
        try:
            return len(self.vertices)
        except:
            raise Exception()

    # Method Total Time Complexity: O(1)

    def addEdge(self, vertex1, vertex2):
        """! Add a new edge to a new graph object"""
        try:
            if self.vertices.count(vertex1) == 0: # Time Complexity: O(1)
                self.vertices += [vertex1]
            if self.vertices.count(vertex2) == 0: # Time Complexity: O(1)
                self.vertices += [vertex2]
            self.graph[vertex1].append(vertex2) # Time Complexity: O(1)
            self.graph[vertex2].append(vertex1) # Time Complexity: O(1)
        except:
            raise Exception()

    # Method Total Time Complexity: O(1) + O(1) + O(1) + O(1) = O(1)

    def FindVertexCover(self):
        """! Find the smallest vertex cover of an undirected graph"""
        Visited = [False] * len(self.vertices) # Initially all nodes have not been visited
        Output = [] # Output shows the vertex set of vertex cover
        for vertex in range(len(self.vertices)):
            if not Visited[vertex]:
                # Select edges that both connected vertices have not been visited
                # Reachable edges are ignored
                for edge in self.graph[vertex]:
                    if not Visited[edge]:
                        Visited[edge] = True
                        Visited[vertex] = True
                # Collect vertex to output list
                Output += [vertex]
        return Output # Time Complexity: O(1)

    # Method Total Time Complexity: O(V + E)