# Author: Jingze Dai
# Date: 16/02/2021
# Email Address: daij24@mcmaster.ca or david1147062956@163.com
import unittest
import BFS


class MyTestCase(unittest.TestCase):
    def test_BFS(self):
        """! Getters of object's BFS Method """
        g1 = BFS.Graph(False)
        g1.add_edge((0, 1))
        g1.add_edge((0, 2))
        g1.add_edge((1, 2))
        g1.add_edge((2, 0))
        g1.add_edge((2, 3))
        self.assertEqual(g1.BFS(0), [0, 1, 2, 3])

        g2 = BFS.Graph(True)
        g2.add_edge((0, 1))
        g2.add_edge((1, 2))
        g2.add_edge((2, 3))
        g2.add_edge((3, 4))
        g2.add_edge((4, 0))
        self.assertEqual(g2.BFS(0), [0, 1, 2, 3, 4])

        g3 = BFS.Graph(True)
        g3.add_edge((0, 1))
        g3.add_edge((1, 0))
        g3.add_edge((0, 2))
        g3.add_edge((2, 0))
        g3.add_edge((1, 2))
        g3.add_edge((2, 1))
        g3.add_edge((2, 3))
        g3.add_edge((3, 2))
        self.assertEqual(g3.BFS(0), [0, 1, 2, 3])

        g4 = BFS.Graph(False)
        g4.add_edge((0, 1))
        g4.add_edge((0, 2))
        g4.add_edge((0, 3))
        g4.add_edge((0, 4))
        g4.add_edge((1, 3))
        g4.add_edge((2, 5))
        self.assertEqual(g4.BFS(0), [0, 1, 2, 3, 4, 5])

        g5 = BFS.Graph(False)
        g5.add_edge((0, 2))
        g5.add_edge((6, 3))
        g5.add_edge((6, 2))
        g5.add_edge((4, 5))
        g5.add_edge((6, 5))
        g5.add_edge((4, 1))
        self.assertEqual(g5.BFS(0), [0, 2, 6, 3, 5, 4, 1])

        g6 = BFS.Graph(False)
        g6.add_edge((0, 1))
        g6.add_edge((0, 2))
        g6.add_edge((0, 3))
        g6.add_edge((0, 4))
        g6.add_edge((0, 5))
        g6.add_edge((0, 6))
        g6.add_edge((1, 6))
        g6.add_edge((6, 5))
        g6.add_edge((5, 4))
        g6.add_edge((4, 3))
        g6.add_edge((3, 2))
        g6.add_edge((2, 1))
        self.assertEqual(g6.BFS(0), [0, 1, 2, 3, 4, 5, 6])