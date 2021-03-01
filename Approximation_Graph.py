# Jingze Dai Date: 2020/09/22
# Part 3 Algorithm: Approximation Algorithm on Vertex Cover
# Undirected graphs are represented as "Approximation_Graph" object
from collections import defaultdict


class Approximation_Graph:
    def __init__(self): # Constructor Time Complexity: O(1) + O(1) = O(1)
        self.vertices = [] # Time Complexity: O(1)
        self.graph = defaultdict(list) # Time Complexity: O(1)

    def get_vertices(self): # Method Time Complexity: O(1)
        return self.vertices # Time Complexity: O(1)

    def get_graph(self): # Method Time Complexity: O(1)
        return self.graph # Time Complexity: O(1)

    def addEdge(self, vertex1, vertex2): # Method Time Complexity: O(1) + O(1) + O(1) + O(1) = O(1)
        if self.vertices.count(vertex1) == 0: # Time Complexity: O(1)
            self.vertices += [vertex1]
        if self.vertices.count(vertex2) == 0: # Time Complexity: O(1)
            self.vertices += [vertex2]
        self.graph[vertex1].append(vertex2) # Time Complexity: O(1)
        self.graph[vertex2].append(vertex1) # Time Complexity: O(1)

    def FindVertexCover(self): # Method Time Complexity: O(V + E)
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
# Below are test cases: A graph object has a number of nodes and edges.
# If you want to use other test cases, modify all lines of codes below


Graph = Approximation_Graph()
Graph.addEdge(0, 1)
Graph.addEdge(2, 0)
Graph.addEdge(2, 1)
Graph.addEdge(1, 3)
Graph.addEdge(1, 4)
Graph.addEdge(4, 3)
print(Graph.vertices)
print(Graph.graph)
print(Graph.FindVertexCover())