from collections import deque

class Vertex(object):
    """
    Define a vertex in a Graph using adjacency List.
    """
    def __init__(self, data):
        self.inDegree = 0
        self.data = data
        self.edges = []
        # Add etv、ltv to calculate Critical Path.
        self.etv = 0
        self.ltv = 0

    def incInDegree(self):
        self.inDegree += 1

    def addEdge(self, edge):
        if self.edges is None:
            self.edges = edge
        else:
            first = self.edges
            self.edges = edge
            edge.next = first

class Edge(object):
    """
    Define an edge in a Graph using adjacency List.
    """
    def __init__(self, adjacent, weight):
        self.adjacentVertex = adjacent
        self.weight = weight
        self.next = None
        # Add ete、lte to calculate Critical Path.
        self.ete = 0
        self.lte = 0

class Graph(object):
    """
    Define a graph using adjacency List.
    """
    def __init__(self):
        self.Vertexs = {}
        # Add list of edge to implement MCST_Kruskal()
        self.Edges = []
        self.numVertex = 0
        self. numEdge = 0


    def readFile(self, file):
        try:
            data = open(file, "r").read()
            lines = data.split('\n')
            return lines
        except Exception as e:
            print(str(e))
            return None

    def initGraph(self, file):
        try:
            lines = self.readFile(file)
            if lines is None:
                return False
            for line in lines:
                start, end, weight = line.split(',')
                vertex_s = None
                vertex_e = None
                if start not in self.Vertexs:
                    vertex_s = Vertex(start)
                    self.Vertexs[start] = vertex_s
                else:
                    vertex_s = self.Vertexs[start]
                if end not in self.Vertexs:
                    vertex_e = Vertex(end)
                    self.Vertexs[end] = vertex_e
                else:
                    vertex_e = self.Vertexs[end]
                vertex_e.incInDegree()
                edge = Edge(end, float(weight))
                if (end, start, float(weight)) not in self.Edges:
                    self.Edges.append((start, end, float(weight)))
                vertex_s.edges.append(edge)
            self.numVertex = len(self.Vertexs)
        except Exception as e:
            print(str(e))

    def topologicalSort(self):
        stack = []
        count = 0
        # Add the below to calculate Critical Path
        topo_sort = []
        # end
        try:
            for value in self.Vertexs.values():
                if value.inDegree == 0:
                    stack.append(value)
            while len(stack) > 0:
                vertex = stack.pop()

                # Add the below to calculate Critical Path
                topo_sort.append(vertex)
                # end

                count += 1
                print(vertex.data)
                for edge in vertex.edges:
                    self.Vertexs[edge.adjacentVertex].inDegree -= 1

                    # Add the below to calculate Critical Path
                    self.Vertexs[edge.adjacentVertex].etv = max(self.Vertexs[edge.adjacentVertex].etv,
                                                                vertex.etv + edge.weight)
                    # end

                    if self.Vertexs[edge.adjacentVertex].inDegree == 0:
                        stack.append(self.Vertexs[edge.adjacentVertex])

            return topo_sort
        except Exception as e:
            print(str(e))

        return None


    def MCST_Prim(self, start):
        lowcost = {}
        adjvertex = {}
        min = 65535
        edges = []
        mc  = 0
        for key in self.Vertexs.keys():
            if key == start:
                lowcost[key] = 0
                adjvertex[key] = start
            else:
                lowcost[key] = min
                adjvertex[key] = start

        for i in range(0, self.numVertex):
            for edge in self.Vertexs[start].edges:
                if edge.weight < lowcost[edge.adjacentVertex]:
                    lowcost[edge.adjacentVertex] = edge.weight
                    adjvertex[edge.adjacentVertex] = start
            min_ver = None
            min = 65535
            for key in lowcost.keys():
                if lowcost[key] != 0 and lowcost[key] < min:
                    min = lowcost[key]
                    min_ver = key
            if min_ver is None:
                break
            lowcost[min_ver] = 0
            edges.append((adjvertex[min_ver], min_ver, min))
            start = min_ver
            mc += min
        print(edges)
        return mc

    def Find(self, parents, vex):
        while parents[vex] is not None:
            vex = parents[vex]
        return vex


    def MCST_Kruskal(self):
        edges = []
        mc = 0
        self.Edges.sort(key=lambda x:x[2])
        self.numEdge = len(self.Edges)
        parents = {}
        for key in self.Vertexs.keys():
            parents[key] = None
        for edge in self.Edges:
            start = self.Find(parents, edge[0])
            end = self.Find(parents, edge[1])
            if start != end:
                parents[start] = end
                edges.append(edge)
                mc += edge[2]

        return mc

    def CriticalPath(self):
        topo_sort = self.topologicalSort()
        for vertex in self.Vertexs.values():
            vertex.ltv = topo_sort[-1].etv
        while len(topo_sort) > 0:
            vertex = topo_sort.pop()
            for edge in vertex.edges:
                vertex.ltv = min(vertex.ltv, self.Vertexs[edge.adjacentVertex].ltv - edge.weight)
