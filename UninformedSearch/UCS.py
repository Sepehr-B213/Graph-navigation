from queue import PriorityQueue

verticelist = {
    'S': {'A': 3, 'D': 4},
    'A': {'D': 5},
    'D': {'E': 2},
    'B': {'A': 4, 'E': 5, 'C': 4},
    'C': {},
    'E': {'F': 4},
    'F': {'G': 3},
    'G': {}
}



def ucs(graph, start, target):
    global totalweight
    expanded = []
    q = PriorityQueue()
    q.put((0, start))
    visited = set()

    while q:

        weight, vertex = q.get()
        current = vertex[-1]


        print("Visited nodes:",visited, "\n",
              "Current node:",current, "\n",
              "-------" * 10)

        if current not in visited:
            visited.add(current)
            expanded.append(
                current)

            if current == target:
                return vertex, expanded

            children = graph[current]
            for i in children:
                if i not in visited:
                    totalweight = weight + children[i]
                    q.put((totalweight,
                           vertex + i))
        print("totalweight of path:",totalweight)



final_path, visited = ucs(verticelist, 'S', 'G')
print('The final path is ----> ', final_path)
print("The visited nodes in path: ---->", visited)
print("The final totalweight of path:",totalweight)

