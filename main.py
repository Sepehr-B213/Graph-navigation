from Graph import Graph

g = Graph(10)
g.addEdge(0, 1, 3)
g.addEdge(0, 6, 5)
g.addEdge(0, 5, 1)
g.addEdge(1, 6, 30)
g.addEdge(2, 8, 12)
g.addEdge(3, 9, 20)
g.addEdge(4, 9, 38)
g.addEdge(5, 7, 18)
g.addEdge(5, 6, 3)
g.addEdge(6, 4, 42)
g.addEdge(6, 2, 3)
g.addEdge(7, 1, 12)
g.addEdge(8, 6, 5)
g.addEdge(8, 3, 3)


def create():
    global g

    warning = input("Warning: Creating a new graph will replace current graph. Is this okay? y/n ")

    if warning == "y":
        nodes = int(input("How many nodes? "))
        g = Graph(nodes)

        creating = "y"
        print("\nGraph is created by creating edges. Will enter start node, end node, and the weight between them\n")

        while creating == "y":
            start = int(input("Enter starting node: "))
            end = int(input("Enter ending node: "))
            weight = int(input("Enter edge weight: "))
            g.addEdge(start, end, weight)

            creating = input("Add another edge? y/n ")


def runPrim():
    global g
    start = int(input("Which node is the start node? "))
    end = int(input("Which node is the end node? "))
    if g != None:
        g.prims(start, end)


def runkruskal():
    global g
    start = int(input("Which node is the start node? "))
    end = int(input("Which node is the end node? "))

    if g != None:
        g.Kruskal_Algorithm(start, end)


def rundijkstra():
    global g

    start = int(input("Which node is the start node? "))
    end = int(input("Which node is the end node? "))

    if g != None:
        g.dijkstra(start, end)


def showGraph():
    global g

    if g != None:
        g.draw(graph=g.graph, title="Main Graph")


def primVSkruskal():
    global g

    if g != None:
        g.printresult(g.finalprim, g.primweight, "Prim Graph")
        g.find(g.finalprim, g.Pstart, g.Pend)

        g.printresult(g.finalkeruskal, g.keruskalweight, "Keruskal Graph")
        g.find(g.finalkeruskal, g.Kstart, g.Kend)


def primVSdijkstra():
    global g

    if g != None:
        g.printresult(g.finalprim, g.primweight, "Prim Graph")
        g.find(g.finalprim, g.Pstart, g.Pend)

        g.printresult(g.finaldijkstra, g.dijkstrawieght, "Dijkstra Graph")
        g.find(g.finaldijkstra, g.Dstart, g.Dend)


def kruskalVSdijkstra():
    global g

    if g != None:
        g.printresult(g.finalkeruskal, g.keruskalweight, "Keruskal Graph")
        g.find(g.finalkeruskal, g.Kstart, g.Kend)

        g.printresult(g.finaldijkstra, g.dijkstrawieght, "Dijkstra Graph")
        g.find(g.finaldijkstra, g.Dstart, g.Dend)


def Comparison():
    global g

    if g != None:
        g.printresult(g.finalkeruskal, g.keruskalweight, "Keruskal Graph")
        g.find(g.finalkeruskal, g.Kstart, g.Kend)

        g.printresult(g.finalprim, g.primweight, "Prim Graph")
        g.find(g.finalprim, g.Pstart, g.Pend)

        g.printresult(g.finaldijkstra, g.dijkstrawieght, "Dijkstra Graph")
        g.find(g.finaldijkstra, g.Dstart, g.Dend)


def run():
    while True:
        option = input(
            """Select an algorithm:
    1. Create Graph
    2. Show main Graph
    3. Kruskal
    4. Prim's 
    5. Dijkstra
    6. prim Vs keruskal
    7. Prim Vs Dijkstra
    8. Keruskal Vs Dijkstra
    9. Compare of 3 algorithm
    x. Quit
    : """)
        if option == "1":
            create()
        elif option == "2":
            showGraph()
        elif option == "3":
            runkruskal()
        elif option == "4":
            runPrim()
        elif option == "5":
            rundijkstra()
        elif option == "6":
            primVSkruskal()
        elif option == "7":
            primVSdijkstra()
        elif option == "8":
            kruskalVSdijkstra()
        elif option == "9":
            Comparison()
        elif option == "x":
            return


if __name__ == "__main__":
    run()
