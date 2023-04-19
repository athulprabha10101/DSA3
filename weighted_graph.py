class W_graph:
    def __init__(self):
        self.adjacency_dict = {}

    def add_vertex(self, vertex):
        if vertex not in self.adjacency_dict.keys():
            self.adjacency_dict[vertex] = []

    def add_edge(self, v1, v2, weight):
        if v1 not in self.adjacency_dict.keys():
            self.add_vertex(v1)
        if v2 not in self.adjacency_dict.keys():
            self.add_vertex(v2)

        self.adjacency_dict[v1].add({"Node": v2, "Weight": weight})
        self.adjacency_dict[v2].add({"Node": v1, "Weight": weight})

    def remove_edge(self, v1, v2):
        if v1 in self.adjacency_dict.keys():
            self.adjacency_dict[v1] = [neighbor for neighbor in self.adjacency_dict[v1] if neighbor["Node"] != v2]
        if v2 in self.adjacency_dict.keys():
            self.adjacency_dict[v2] = [neighbor for neighbor in self.adjacency_dict[v2] if neighbor["Node"] != v1]

    def remove_vertex(self, vertex):
        if vertex in self.adjacency_dict.keys():
            for neighbor in self.adjacency_dict[vertex]:
                self.adjacency_dict[neighbor["Node"]] = [n for n in self.adjacency_dict[neighbor["Node"]] if n !=

