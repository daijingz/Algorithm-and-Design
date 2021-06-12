# Author: Jingze Dai
# Date: 16/02/2021
# Email Address: daij24@mcmaster.ca or david1147062956@163.com
import unittest
import Approximation_Graph


class MyTestCase(unittest.TestCase):
    def test_FindVertexCover(self):
        """! Test Approximation_graph programs' getting-vertex-cover methods"""
        G1 = Approximation_Graph.Approximation_Graph()
        G1.addEdge(0, 1)
        G1.addEdge(1, 2)
        G1.addEdge(2, 3)
        self.assertEqual(G1.FindVertexCover(), [0, 2])

        G2 = Approximation_Graph.Approximation_Graph()
        G2.addEdge(0, 1)
        G2.addEdge(1, 2)
        G2.addEdge(2, 3)
        G2.addEdge(3, 4)
        G2.addEdge(4, 0)
        self.assertEqual(G2.FindVertexCover(), [0, 2])

        G3 = Approximation_Graph.Approximation_Graph()
        G3.addEdge(0, 1)
        G3.addEdge(2, 0)
        G3.addEdge(2, 1)
        G3.addEdge(1, 3)
        G3.addEdge(1, 4)
        G3.addEdge(4, 3)
        self.assertEqual(G3.FindVertexCover(), [0, 3])

        G4 = Approximation_Graph.Approximation_Graph()
        G4.addEdge(0, 1)
        G4.addEdge(1, 2)
        G4.addEdge(2, 3)
        G4.addEdge(1, 0)
        G4.addEdge(2, 1)
        G4.addEdge(3, 2)
        self.assertEqual(G4.FindVertexCover(), [0, 2])

        G5 = Approximation_Graph.Approximation_Graph()
        G5.addEdge(0, 1)
        G5.addEdge(1, 4)
        G5.addEdge(4, 3)
        G5.addEdge(3, 2)
        G5.addEdge(2, 1)
        self.assertEqual(G5.FindVertexCover(), [0, 2, 4])