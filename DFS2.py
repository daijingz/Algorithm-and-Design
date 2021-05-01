# Import DFS method from GeekToGeek
from collections import defaultdict


class Graph:
    def __init__(self):
        self.amount = 0
        self.graph = defaultdict(list)

    def addEdge(self, u, v):
        if self.graph[u].count(v) > 0:
            raise ValueError()
        self.graph[u].append(v)

    def DFSUtil(self, v, visited):

        # Mark the current node as visited
        # and print it
        visited.add(v)
        print(v, end=' ')

        # Recur for all the vertices
        # adjacent to this vertex
        for neighbour in self.graph[v]:
            if neighbour not in visited:
                self.DFSUtil(neighbour, visited)

    # The function to do DFS traversal. It uses
    # recursive DFSUtil()
    def DFS(self, v):

        # Create a set to store visited vertices
        visited = set()

        # Call the recursive helper function
        # to print DFS traversal
        self.DFSUtil(v, visited)