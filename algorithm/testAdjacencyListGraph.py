import unittest
from .adjacencylistgraph import *
import os

class TestVertex(unittest.TestCase):
    def test_init(self):
        vertex = Vertex('A')
        self.assertEqual(vertex.data, 'A')
        # self.assertEqual(vertex.edges, None)

class TestEdge(unittest.TestCase):
    def test_init(self):
        edge = Edge('B', 8)
        self.assertEqual(edge.next, None)
        self.assertEqual(edge.weight, 8)
        self.assertEqual(edge.adjacentVertex, 'B')

class TestAdjacencyListGraph(unittest.TestCase):
    def test_initGraph0(self):
        graph = Graph()
        graph.initGraph("./graph.txt")
        pass

    def test_TopologicalSort0(self):
        graph = Graph()
        graph.initGraph("./graph.txt")
        graph.topologicalSort()
        pass

    def test_MCPS_Prim_0(self):
        graph = Graph()
        graph.initGraph("./prim.txt")
        mc = graph.MCST_Prim('0')
        self.assertEqual(mc, 99)

    def test_MCPS_Prim_1(self):
        graph = Graph()
        graph.initGraph("./prim.txt")
        mc = graph.MCST_Prim('1')
        self.assertEqual(mc, 99)

    def test_MCPS_Prim_7(self):
        graph = Graph()
        graph.initGraph("./prim.txt")
        mc = graph.MCST_Prim('7')
        self.assertEqual(mc, 99)

    def test_MCPS_Kruskal(self):
        graph = Graph()
        graph.initGraph("./prim.txt")
        mc = graph.MCST_Kruskal()
        self.assertEqual(mc, 99)

    def test_CriticalPath(self):
        graph = Graph()
        graph.initGraph("./critical.txt")
        graph.CriticalPath()
        self.assertEqual(True,True)


