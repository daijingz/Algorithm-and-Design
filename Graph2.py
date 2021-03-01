import itertools


# Jingze Dai Date: 2020/09/22
# Part 2 Algorithm: Brute-Force Algorithms (Exhaustive Computing)
# Undirected graphs are represented as "Improved_Graph" object
class Improved_Graph:
    # Improved_Graph Constructor with Improved_Graph()
    # State variable: Node (Graph's node list)
    # State variable: Edge (Graph's edge list)
    def __init__(self):  # Method Time Complexity: O(1) + O(1), which is O(1)
        self.Node = []  # Time Complexity: O(1)
        self.Edge = []  # Time Complexity: O(1)

    # Getters to get Node list from objects
    def get_Node(self):  # Method Time Complexity: O(1) = O(1)
        return self.Node  # Time Complexity: O(1)

    # Getters to get Edge list from objects
    def get_Edge(self):  # Method Time Complexity: O(1) = O(1)
        return self.Edge  # Time Complexity: O(1)

    # Getters to get amounts of node
    def get_Node_Amount(self):  # Method Time Complexity: O(1) = O(1)
        return len(self.Node)  # Time Complexity: O(1)

    # Add node to a graph's node list
    def add_Node(self, new_Node):  # Method Time Complexity: O(1)
        self.Node = self.Node + [new_Node] # Time Complexity: O(1)
        self.Edge = self.Edge + [[]] # Time Complexity: O(1)

    # Add edge to a graph's edge list
    def add_Edge(self, new_Edge):  # Method Time Complexity: O(1) + O(1), which is O(1)
        self.Edge[self.Node.index(new_Edge[0])] += [new_Edge[1]] # Time Complexity: O(1)
        self.Edge[self.Node.index(new_Edge[1])] += [new_Edge[0]] # Time Complexity: O(1)

    # Getting all sub-lists of node lists
    def get_Sublist(self): # Method Time Complexity: 3 * O(1) + O(n ^ 2) = O(n ^ 2)
        # Output is the output (a list containing all possible non-empty cases of vertex cover)
        # Those cases are possible but not necessary becoming a vertex cover
        Output = [] # Time Complexity: O(1)
        a = 1 # Time Complexity: O(1)
        # Loop used to find non-empty sub-lists with different lengths
        while a < len(self.Node) + 1: # Time Complexity: O(n ^ 2)
            Output += list(map(list, itertools.combinations(self.Node, a)))
            a += 1 # Time Complexity: O(1)
        return Output # Time Complexity: O(1)

    # Methods for checking sub-lists are vertex cover cases
    # Checking whether every edge has at least one node in the node list
    # it will return True if it is a vertex cover, else False
    def get_Vertex_Cover(self): # Method Time Complexity: O(n ^ 2)
        Vertex_Cover_List = [] # Time Complexity: O(1)
        Sub_List = self.get_Sublist()# Time Complexity: O(n ^ 2)
        for i in Sub_List: # Time Complexity: O(n * lg n)
            Cover = set()
            for j in i: # Time Complexity: O(lg n)
                Cover.update(self.Edge[self.Node.index(j)]) # Time Complexity: O(1)
                if set(self.Node) == Cover:
                    Vertex_Cover_List += [i] # Time Complexity: O(1)
        return Vertex_Cover_List # Time Complexity: O(1)

    # To find the minimum-length
    # Step 1: Get minimum length of vertex cover
    # Step 2: find all vertex covers with minimum length and output it
    def get_Minimum_Vertex_Cover(self): # Method Time Complexity: O(n ^ 2)
        Vertex_Cover_List = self.get_Vertex_Cover() # Time Complexity: O(n ^ 2)
        Minimum_Length = 100 # Time Complexity: O(1)
        Minimum_Vertex_Cover_List = [] # Time Complexity: O(1)
        for i in Vertex_Cover_List: # Time Complexity: O(n)
            if len(i) == Minimum_Length:
                Minimum_Vertex_Cover_List += [i] # Time Complexity: O(1)
            elif len(i) < Minimum_Length:
                Minimum_Length = len(i) # Time Complexity: O(1)
                Minimum_Vertex_Cover_List = [] # Time Complexity: O(1)
                Minimum_Vertex_Cover_List += [i] # Time Complexity: O(1)
        return Minimum_Vertex_Cover_List # Time Complexity: O(1)

    # Check all vertex cover cases on whether each case is smaller than provided range
    # Output is a list with vertex cover cases whose size is lower than or equals
    def get_Range_Vertex_Cover(self, Range_Length): # Method Time Complexity: O(n ^ 2)
        Vertex_Cover_List = self.get_Vertex_Cover() # Time Complexity: O(n ^ 2)
        Range_Vertex_Cover_List = [] # Time Complexity: O(1)
        for i in Vertex_Cover_List: # Time Complexity: O(n)
            if len(i) <= Range_Length:
                Range_Vertex_Cover_List += [i]
        return Range_Vertex_Cover_List # Time Complexity: O(1)
# Below are test cases: A graph object has a number of nodes and edges.
# If you want to use other test cases, modify all lines of codes below


IG = Improved_Graph()
IG.add_Node(0)
IG.add_Node(1)
IG.add_Node(2)
IG.add_Node(3)
IG.add_Node(4)
IG.add_Edge([0, 1])
IG.add_Edge([1, 4])
IG.add_Edge([0, 4])
IG.add_Edge([0, 2])
IG.add_Edge([0, 3])
IG.add_Edge([2, 3])
IG.add_Edge([3, 4])
print(IG.get_Node())
print(IG.get_Edge())
print(IG.get_Sublist())
print(IG.get_Vertex_Cover())
print(IG.get_Minimum_Vertex_Cover())
print(IG.get_Range_Vertex_Cover(3))
