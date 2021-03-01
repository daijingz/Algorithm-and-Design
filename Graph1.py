import itertools


# Jingze Dai Date: 2020/09/22
# Part 1 Algorithm: Brute-Force Algorithms (Exhaustive Computing)
# Undirected graphs are represented as "Graph" object
class Graph:
    # Amount_Node type: integer ()
    # Node type: string (include digits, letters and others)
    # Edge type: A length-2 list containing 2 Strings nodes (should be included into)
    def __init__(self, Amount_Node): # Method Time Complexity: O(1) + O(1) + O(1), which is O(1)
        self.Amount_Node = Amount_Node # Time Complexity: O(1)
        self.Node = [] # Time Complexity: O(1)
        self.Edge = [] # Time Complexity: O(1)

    # Getters of Amount of Nodes (State variable: Integers)
    def get_Amount_Node(self): # Method Time Complexity: O(1), which is O(1)
        return self.Amount_Node # Time Complexity: O(1)

    # Getters of Node List (State variable: List)
    def get_Node(self): # Method Time Complexity: O(1), which is O(1)
        return self.Node # Time Complexity: O(1)

    # Getters of Edge List (State variable: List)
    def get_Edge(self): # Method Time Complexity: O(1), which is O(1)
        return self.Edge # Time Complexity: O(1)

    # Methods for adding a node to a "graph" object
    # Adding a node to node list, at the same time update amount of nodes
    def add_Node(self, new_Node): # Method Time Complexity: O(1) + O(1), which is O(1)
        self.Node += [new_Node] # Time Complexity: O(1)
        self.Amount_Node = len(self.Node) # Time Complexity: O(1)

    # Methods for adding an edge to a "graph" object
    # Adding an edge to "Graph" object's edge list
    def add_Edge(self, new_Edge): # Method Time Complexity: O(1), which is O(1)
        self.Edge += [new_Edge] # Time Complexity: O(1)

    # Methods for getting all sub-lists of objects'
    def get_Sublist(self): # Method Time Complexity: O(n ^ 2) (This is dominant parts)
        # Output is the output (a list containing all possible non-empty cases of vertex cover)
        # Those cases are possible but not necessary becoming a vertex cover
        Output = [] # Time Complexity: O(1)
        a = 1 # Time Complexity: O(1)
        # Loop used to find non-empty sub-lists with different lengths
        while a < len(self.Node) + 1: # Single Loop with index "a" adding, with Time Complexity O(n)
            Output += list(map(list, itertools.combinations(self.Node, a))) # Time Complexity O(n)
            a += 1 # Time Complexity: O(1)
        return Output # Time Complexity: O(1)

    # Methods for selecting vertex cover from all sub-lists
    # For all sub-lists contained, have function calls to check each sub-list
    def get_Vertex_Cover(self): # Method Time Complexity: O(n ^ 2)
        Output = [] # Time Complexity: O(1)
        Possible_Cases = self.get_Sublist() # Time Complexity: O(n ^ 2) for get_Sublist() method
        for i in Possible_Cases: # Time Complexity: O(n * lg n)
            if self.check_Vertex_Cover(i): # Time Complexity: O(lg n)
                Output += [i]
        return Output # Time Complexity: O(1)

    # Methods for checking sub-lists are vertex cover cases
    # Checking whether every edge has at least one node in the node list
    # it will return True if it is a vertex cover, else False
    def check_Vertex_Cover(self, Input): # Method Time Complexity: O(lg n) + O(1) = O(lg n)
        for i in self.Edge: # Time Complexity: O(lg n)
            if Input.count(i[0]) == 0 and Input.count(i[1]) == 0:
                return False
        return True # Time Complexity: O(1)

    # To find the minimum-length
    # Step 1: Find minimum length of vertex cover
    # Step 2: find all vertex covers with minimum length
    def get_Minimum_Vertex_Cover(self): # Method Time Complexity: O(n ^ 2)
        Output = [] # Time Complexity: O(1)
        minimum_length = 200 # Time Complexity: O(1)
        for i in self.get_Vertex_Cover(): # Time Complexity: O(n ^ 2)
            if len(i) < minimum_length:
                minimum_length = len(i)

        for j in self.get_Vertex_Cover(): # Time Complexity: O(n ^ 2)
            if len(j) == minimum_length:
                Output += [j]
        return Output # Time Complexity: O(1)

    # Check all vertex cover cases on whether each case is smaller than provided range
    # Output is a list with vertex cover cases whose size is lower than or equals
    def get_Range_Vertex_Cover(self, number): # Method Complexity: O(n ^ 2)
        Output = [] # Time Complexity: O(1)
        for j in self.get_Vertex_Cover(): # Time complexity: O(n ^ 2)
            if len(j) == number or len(j) < number:
                Output += [j]
        return Output # Time Complexity: O(1)
# Below are test cases: A graph object has a number of nodes and edges.
# If you want to use other test cases, modify all lines of codes below


G1 = Graph(5)
G1.add_Node("1")
G1.add_Node("2")
G1.add_Node("3")
G1.add_Node("4")
G1.add_Node("5")
G1.add_Edge(["1", "2"])
G1.add_Edge(["1", "3"])
G1.add_Edge(["3", "5"])
G1.add_Edge(["2", "4"])
G1.add_Edge(["3", "4"])
print(G1.Node)
print(G1.Edge)
print(G1.get_Sublist())
print(G1.get_Vertex_Cover())
print(G1.get_Minimum_Vertex_Cover())
print(G1.get_Range_Vertex_Cover(3))