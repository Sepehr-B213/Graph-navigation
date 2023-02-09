from collections import defaultdict


class Graph:

    def __init__(self):
        self.graph = defaultdict(list)

    def addEdge(self, u, v):
        self.graph[u].append(v)


    def dfs(self, start, target, path=None, visited=None):
        if visited is None:
            visited = set()
        if path is None:
            path = []
        path.append(start)
        visited.add(start)
        if start == target:
            return path
        for (neighbour) in self.graph[start]:
            self.print_result(visited,path)
            if neighbour not in visited:
                result = self.dfs(neighbour, target, path, visited)
                if result is not None:
                    return result

        #path.pop()
        return None

    def print_result(self,Visited, Path):
        print("visited nodes:", Visited)
        print("Path of graph:")
        print(*Path, sep=" --> ")
        print("------"*10)



g = Graph()

g.addEdge(1, 2)
g.addEdge(1, 3)
g.addEdge(2, 4)
g.addEdge(2, 5)
g.addEdge(3, 6)
g.addEdge(3, 7)
g.addEdge(4, 8)
g.addEdge(4, 9)
g.addEdge(5, 10)
g.addEdge(5, 11)
g.addEdge(6, 12)
g.addEdge(6, 13)
g.addEdge(7, 14)
g.addEdge(7, 15)
g.addEdge(8, 16)
g.addEdge(8, 17)
g.addEdge(9, 18)
g.addEdge(9, 19)
g.addEdge(16, 20)
g.addEdge(16, 21)
g.addEdge(17, 22)
g.addEdge(17, 23)
g.addEdge(20, 24)
g.addEdge(20, 25)

traversal_path = []
traversal_path = g.dfs(1, 18)
print("Final path:")
print(*traversal_path, sep=" --> ")
