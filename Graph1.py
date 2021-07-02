import itertools
# Author: Jingze Dai
# Email Address: daij24@mcmaster.ca or david1147062956@163.com
# Github: https://github.com/daijingz
# Linkedin: https://www.linkedin.com/in/jingze-dai/
# Description: Graph implementation 1 with brute force algorithm (version 1)


class Graph:
    def __init__(self, Amount_Node):
        """! Initializes the program.

        Amount_Node type: integer ()
        Node type: string (include digits, letters and others)
        Edge type: A length-2 list containing 2 Strings nodes (should be included into)

        """
        self.Amount_Node = Amount_Node # Time Complexity: O(1)
        self.Node = [] # Time Complexity: O(1)
        self.Edge = [] # Time Complexity: O(1)

    # Method Time Complexity: O(1) + O(1) + O(1), which is O(1)

    def get_Amount_Node(self):
        """! Getters of Amount of Nodes (State variable: Integers)"""
        try:
            return self.Amount_Node # Time Complexity: O(1)
        except:
            raise Exception()

    # Method Total Time Complexity: O(1), which is O(1)

    def get_Node(self):
        """! Getters of Node List (State variable: List)"""
        try:
            return self.Node # Time Complexity: O(1)
        except:
            raise Exception()

    # Method Total Time Complexity: O(1), which is O(1)

    def get_Edge(self):
        """! Getters of Edge List (State variable: List)"""
        try:
            return self.Edge # Time Complexity: O(1)
        except:
            raise Exception()

    # Method Total Time Complexity: O(1), which is O(1)

    def add_Node(self, new_Node):
        """!

        Methods for adding a node to a "graph" object
        Adding a node to node list, at the same time update amount of nodes

        """
        try:
            self.Node += [new_Node] # Time Complexity: O(1)
            self.Amount_Node = len(self.Node) # Time Complexity: O(1)
        except:
            raise Exception()

    # Method Total Time Complexity: O(1) + O(1), which is O(1)

    def add_Edge(self, new_Edge):
        """!

        Methods for adding an edge to a "graph" object
        Adding an edge to "Graph" object's edge list

        """
        try:
            self.Edge += [new_Edge] # Time Complexity: O(1)
        except:
            raise Exception()

    # Method Total Time Complexity: O(1), which is O(1)

    def get_Sublist(self):
        """!

        Methods for getting all sub-lists of objects
        Output is the output (a list containing all possible non-empty cases of vertex cover)
        Those cases are possible but not necessary becoming a vertex cover

        """
        Output = [] # Time Complexity: O(1)
        a = 1 # Time Complexity: O(1)
        # Loop used to find non-empty sub-lists with different lengths
        while a < len(self.Node) + 1: # Single Loop with index "a" adding, with Time Complexity O(n)
            Output += list(map(list, itertools.combinations(self.Node, a))) # Time Complexity O(n)
            a += 1 # Time Complexity: O(1)
        return Output # Time Complexity: O(1)

    # Method Total Time Complexity: O(n ^ 2) (This is dominant parts)

    def get_Vertex_Cover(self):
        """!

        Methods for selecting vertex cover from all sub-lists
        For all sub-lists contained, have function calls to check each sub-list

        """
        Output = [] # Time Complexity: O(1)
        Possible_Cases = self.get_Sublist() # Time Complexity: O(n ^ 2) for get_Sublist() method
        for i in Possible_Cases: # Time Complexity: O(n * lg n)
            if self.check_Vertex_Cover(i): # Time Complexity: O(lg n)
                Output += [i]
        return Output # Time Complexity: O(1)

    # Method Total Time Complexity: O(n ^ 2)

    def check_Vertex_Cover(self, Input):
        """!

        Methods for checking sub-lists are vertex cover cases
        Checking whether every edge has at least one node in the node list
        It will return True if it is a vertex cover, else False

        """
        for i in self.Edge: # Time Complexity: O(lg n)
            if Input.count(i[0]) == 0 and Input.count(i[1]) == 0:
                return False
        return True # Time Complexity: O(1)

    # Method Total Time Complexity: O(lg n) + O(1) = O(lg n)

    def get_Minimum_Vertex_Cover(self):
        """!

        To find the minimum-length
        Step 1: Find minimum length of vertex cover
        Step 2: find all vertex covers with minimum length

        """
        Output = [] # Time Complexity: O(1)
        minimum_length = 200 # Time Complexity: O(1)
        for i in self.get_Vertex_Cover(): # Time Complexity: O(n ^ 2)
            if len(i) < minimum_length:
                minimum_length = len(i)

        for j in self.get_Vertex_Cover(): # Time Complexity: O(n ^ 2)
            if len(j) == minimum_length:
                Output += [j]
        return Output # Time Complexity: O(1)

    # Method Total Time Complexity: O(n ^ 2)

    def get_Range_Vertex_Cover(self, number):
        """!

        Check all vertex cover cases on whether each case is smaller than provided range
        Output is a list with vertex cover cases whose size is lower than or equals

        """
        Output = [] # Time Complexity: O(1)
        for j in self.get_Vertex_Cover(): # Time complexity: O(n ^ 2)
            if len(j) == number or len(j) < number:
                Output += [j]
        return Output # Time Complexity: O(1)

    # Method Total Time Complexity: O(n ^ 2)