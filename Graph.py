class Graph:
    def __init__(self):
        self.adj_list = {}

    def add_vertex(self, vertex):
        if vertex not in self.adj_list.keys():
            self.adj_list[vertex] = []
            return True
        return False

    def add_edge(self, v1, v2):
        if v1 in self.adj_list.keys() and v2 in self.adj_list.keys():
            self.adj_list[v1].append(v2)
            self.adj_list[v2].append(v1)

    def print_graph(self):
        for vertex in self.adj_list:
            print(vertex, " : ",self.adj_list[vertex])

xgraph = Graph()
xgraph.add_vertex("A")
xgraph.add_vertex("B")
xgraph.add_edge("A", "B")
xgraph.print_graph()