from collections import defaultdict
from sys import maxsize
from queue import PriorityQueue
import networkx as nx
import matplotlib.pyplot as plt


class Graph:

    def __init__(self, vertices):
        self.graph = defaultdict(list)
        self.graph2 = []
        self.graph3 = [[-1 for column in range(vertices)]
                       for row in range(vertices)]
        self.size = vertices
        self.finalprim = [] * self.size
        self.primweight = 0
        self.finalkeruskal = [] * self.size
        self.keruskalweight = 0
        self.finaldijkstra = [] * self.size
        self.dijkstrawieght = 0
        self.Pstart = 0
        self.Pend = 0
        self.Kstart = 0
        self.Kend = 0
        self.Dstart = 0
        self.Dend = 0

    def addEdge(self, u, v, w):
        self.graph[u].append([v, w])
        self.graph2.append([u, v, w])
        self.graph3[u][v] = w
        self.graph3[v][u] = w

    def search(self, parent, i):
        if parent[i] == i:
            return i
        return self.search(parent, parent[i])

    def connection(self, parent, rank, x, y):
        xroot = self.search(parent, x)
        yroot = self.search(parent, y)

        if rank[xroot] < rank[yroot]:
            parent[xroot] = yroot
        elif rank[xroot] > rank[yroot]:
            parent[yroot] = xroot

        else:
            parent[yroot] = xroot
            rank[xroot] += 1

    def printresult(self, finallist, sumweight, name):
        print()
        print("Total weight for minimal %s:" % name, sumweight)
        print()
        for edge in finallist:
            print(edge[0], " --> ", edge[1], " == ", edge[2])
        print()

    def printdijkstra(self, finalgraph, start, paths):
        for vertex in finalgraph:
            print("Distance from vertex %d to vertex" % start, vertex, "is", finalgraph[vertex])
            print(*paths[vertex], sep=" --> ")
            print()
        print()

    def Kruskal_Algorithm(self, start, end):

        result = []
        i = 0
        e = 0
        self.graph2 = sorted(self.graph2,
                             key=lambda item: item[2])

        parent = []
        rank = []

        for node in range(self.size):
            parent.append(node)
            rank.append(0)

        while e < self.size - 1:
            u, v, w = self.graph2[i]
            i = i + 1
            x = self.search(parent, u)
            y = self.search(parent, v)

            if x != y:
                e = e + 1
                result.append([u, v, w])
                self.connection(parent, rank, x, y)

        totalweight = 0
        for i in result:
            totalweight += i[2]

        self.finalkeruskal = result
        self.keruskalweight = totalweight
        self.Kstart = start
        self.Kend = end
        title = "Kruskal Graph"
        self.printresult(result, totalweight, title)
        self.find(result, start, end)

        finalgraph = defaultdict(list)
        for i in result:
            finalgraph[i[0]].append((i[1], i[2]))

        self.draw(finalgraph, title)

    def dijkstra(self, start_vertex, end_vertex):
        global weight
        weight = 0
        self.visited = []
        D = {v: float('inf') for v in range(self.size)}
        D[start_vertex] = 0

        pq = PriorityQueue()
        pq.put((0, start_vertex))

        paths = [[] for i in range(self.size)]
        paths[start_vertex].append(start_vertex)

        finalTree = []

        while not pq.empty():
            (dist, current_vertex) = pq.get()
            self.visited.append(current_vertex)

            for neighbor in range(self.size):
                if self.graph3[current_vertex][neighbor] != -1:
                    distance = self.graph3[current_vertex][neighbor]
                    if neighbor not in self.visited:
                        old_cost = D[neighbor]
                        new_cost = D[current_vertex] + distance
                        if new_cost < old_cost:
                            pq.put((new_cost, neighbor))
                            D[neighbor] = new_cost
                            paths[neighbor] = paths[current_vertex][:]
                            paths[neighbor].append(neighbor)
                            for edge in finalTree:
                                if edge[1] == neighbor:
                                    finalTree.remove(edge)
                            finalTree.append([current_vertex, neighbor, distance])

        sumweight = 0
        for i in finalTree:
            sumweight = sumweight + i[2]

        self.printresult(finalTree, sumweight, "Dijkstra Graph")
        self.find(finalTree, start_vertex, end_vertex)
        self.printdijkstra(D, start_vertex, paths)

        self.finaldijkstra = finalTree
        self.dijkstrawieght = sumweight
        self.Dstart = start_vertex
        self.Dend = end_vertex

        title = "Dijkstra Graph"
        finalgraph = defaultdict(list)
        for i in finalTree:
            finalgraph[i[0]].append((i[1], i[2]))

        self.draw(finalgraph, title)

    def prims(self, start, end):
        selectedVertices = []
        selectedVertices.append(start)

        totalWeight = 0
        finalTree = []

        while len(selectedVertices) < self.size:
            minNode = None
            minWeight = maxsize
            f = []

            for vertex in selectedVertices:
                for edge in self.graph2:
                    if (edge[0] == vertex) and (edge[1] not in selectedVertices) and (edge[2] < minWeight):
                        minNode = edge[1]
                        minWeight = edge[2]
                        f = edge[:]
                    elif (edge[1] == vertex) and (edge[0] not in selectedVertices) and (edge[2] < minWeight):
                        minNode = edge[0]
                        minWeight = edge[2]
                        f = edge[:]

            finalTree.append(f)
            selectedVertices.append(minNode)
            totalWeight += minWeight

        self.finalprim = finalTree
        self.primweight = totalWeight
        self.Pstart = start
        self.Pend = end

        title = "Prim Graph"
        self.printresult(finalTree, totalWeight, title)
        self.find(finalTree, start, end)

        finalgraph = defaultdict(list)
        for i in finalTree:
            finalgraph[i[0]].append((i[1], i[2]))

        self.draw(finalgraph, title)

    def find(self, tree, start, end):
        total_weight = 0
        path = []
        path.append(start)
        selected_edges = []
        while path[-1] != end:
            f = True
            for edge in tree:
                if edge in selected_edges:
                    continue
                if edge[0] == path[-1]:
                    path.append(edge[1])
                    selected_edges.append(edge)
                    total_weight += edge[2]
                    f = False
                    break
                elif edge[1] == path[-1]:
                    path.append(edge[0])
                    selected_edges.append(edge)
                    total_weight += edge[2]
                    f = False
                    break

            if f:
                path.pop(-1)
                total_weight -= selected_edges[-1][2]
                tree.remove(selected_edges.pop(-1))

        print("total weight of %d to %d:" % (start, end), total_weight)
        print()
        print("Path from %d to %d :" % (start, end))
        print(*path, sep=" --> ")
        print()

    def draw(self, graph, title):
        G = nx.Graph()
        edges = []
        for startNode in graph:
            for edge in graph[startNode]:
                edges.append([startNode, edge[0], edge[1]])

        G.add_weighted_edges_from(edges)
        pos = nx.shell_layout(G)
        plt.figure()
        plt.title(title)
        options = {
            "font_size": 15,
            "node_size": 1000,
            "node_color": "#2460A7FF",
            "linewidths": 3,
            "width": 3,
            "edge_color": "#B3C7D6FF",
            "font_color": "whitesmoke",
        }
        nx.draw_networkx(G, pos, **options)
        nx.draw_networkx_edge_labels(G, pos, edge_labels={(i[0], i[1]): i[2] for i in edges})
        plt.axis('off')
        plt.show()
