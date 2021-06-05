import itertools


# Jingze Dai Date: 2020/09/22
# Part 2 Algorithm: Brute-Force Algorithms (Exhaustive Computing)
# Undirected graphs are represented as "Improved_Graph" object
class Improved_Graph:
    def __init__(self):
        """! Initializes the program.

        Improved_Graph Constructor with Improved_Graph()
        State variable: Node (Graph's node list)
        State variable: Edge (Graph's edge list)

        """
        self.Node = []  # Time Complexity: O(1)
        self.Edge = []  # Time Complexity: O(1)

    # Method Time Complexity: O(1) + O(1), which is O(1)

    def get_Node(self):
        """! Getters to get Node list from objects"""
        try:
            return self.Node  # Time Complexity: O(1)
        except:
            raise Exception()

    # Method Time Complexity: O(1) = O(1)

    def get_Edge(self):
        """! Getters to get Edge list from objects"""
        try:
            return self.Edge  # Time Complexity: O(1)
        except:
            raise Exception()

    # Method Time Complexity: O(1) = O(1)

    def get_Node_Amount(self):
        """! Getters to get amounts of node"""
        try:
            return len(self.Node)  # Time Complexity: O(1)
        except:
            raise Exception()

    # Method Time Complexity: O(1) = O(1)

    def add_Node(self, new_Node):
        """! Add node to a graph's node list"""
        try:
            self.Node = self.Node + [new_Node] # Time Complexity: O(1)
            self.Edge = self.Edge + [[]] # Time Complexity: O(1)
        except:
            raise Exception()

    # Method Time Complexity: O(1)

    def add_Edge(self, new_Edge):
        """! Add edge to a graph's edge list"""
        try:
            self.Edge[self.Node.index(new_Edge[0])] += [new_Edge[1]] # Time Complexity: O(1)
            self.Edge[self.Node.index(new_Edge[1])] += [new_Edge[0]] # Time Complexity: O(1)
        except:
            raise Exception()

    # Method Time Complexity: O(1) + O(1), which is O(1)

    def get_Sublist(self):
        """! Initializes the program.

        Getting all sub-lists of node lists
        Output is the output (a list containing all possible non-empty cases of vertex cover)
        Those cases are possible but not necessary becoming a vertex cover

        """
        Output = [] # Time Complexity: O(1)
        a = 1 # Time Complexity: O(1)
        # Loop used to find non-empty sub-lists with different lengths
        while a < len(self.Node) + 1: # Time Complexity: O(n ^ 2)
            Output += list(map(list, itertools.combinations(self.Node, a)))
            a += 1 # Time Complexity: O(1)
        return Output # Time Complexity: O(1)

    # Method Time Complexity: 3 * O(1) + O(n ^ 2) = O(n ^ 2)

    def get_Vertex_Cover(self):
        """! Initializes the program.

        Methods for checking sub-lists are vertex cover cases
        Checking whether every edge has at least one node in the node list
        it will return True if it is a vertex cover, else False

        """
        Vertex_Cover_List = [] # Time Complexity: O(1)
        Sub_List = self.get_Sublist()# Time Complexity: O(n ^ 2)
        for i in Sub_List: # Time Complexity: O(n * lg n)
            Cover = set()
            for j in i: # Time Complexity: O(lg n)
                Cover.update(self.Edge[self.Node.index(j)]) # Time Complexity: O(1)
                if set(self.Node) == Cover:
                    Vertex_Cover_List += [i] # Time Complexity: O(1)
        return Vertex_Cover_List # Time Complexity: O(1)

    # Method Time Complexity: O(n ^ 2)

    def get_Minimum_Vertex_Cover(self):
        """! Initializes the program.

        To find the minimum-length
        Step 1: Get minimum length of vertex cover
        Step 2: find all vertex covers with minimum length and output it

        """
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

    # Method Time Complexity: O(n ^ 2)

    def get_Range_Vertex_Cover(self, Range_Length):
        """! Initializes the program.

        Check all vertex cover cases on whether each case is smaller than provided range
        Output is a list with vertex cover cases whose size is lower than or equals

        """
        Vertex_Cover_List = self.get_Vertex_Cover() # Time Complexity: O(n ^ 2)
        Range_Vertex_Cover_List = [] # Time Complexity: O(1)
        for i in Vertex_Cover_List: # Time Complexity: O(n)
            if len(i) <= Range_Length:
                Range_Vertex_Cover_List += [i]
        return Range_Vertex_Cover_List # Time Complexity: O(1)

    # Method Time Complexity: O(n ^ 2)