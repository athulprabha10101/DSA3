class Graph:
    def __init__(self):
        self.adjacency_dict = {}

    def add_vertex(self, vertex):
        if vertex not in self.adjacency_dict.keys():
            self.adjacency_dict[vertex] = []

    def add_edge(self, v1, v2):
        if v1 in self.adjacency_dict.keys() and v2 in self.adjacency_dict.keys():
            self.adjacency_dict[v1].append(v2)
            self.adjacency_dict[v2].append(v1)

    def remove_edge(self, v1, v2):
        if v1 in self.adjacency_dict.keys() and v2 in self.adjacency_dict.keys():
            if v2 in self.adjacency_dict[v1]:
                self.adjacency_dict[v1].remove(v2)
            if v1 in self.adjacency_dict[v2]:
                self.adjacency_dict[v2].remove(v1)

    def remove_vertex(self, vertex):
        if vertex in self.adjacency_dict.keys():
            for other_vertex in self.adjacency_dict[vertex]:
                self.adjacency_dict[other_vertex].remove(vertex)
            del self.adjacency_dict[vertex]
            return True
        return False

    def dfs(self, start, visited=None):
        if visited is None:
            visited = set()
        visited.add(start)
        print(start, end=" ")
        for key_node in self.adjacency_dict[start]:
            if key_node not in visited:
                self.dfs(key_node, visited)

    def bfs(self, start_key):
        visited = {}
        que = []
        result = []

        visited[start_key] = True
        que.append(start_key)

        while len(que) > 0:
            current = que.pop(0)
            result.append(current)
            neighbors = self.adjacency_dict[current]

            for item in neighbors:
                if item not in visited.keys():
                    visited[item] = True
                    que.append(item)
        return result


    def print_graph(self):
        print(self.adjacency_dict)
        print()
        for vertex in self.adjacency_dict:
            print(vertex, " : ", self.adjacency_dict[vertex])



xgraph = Graph()
xgraph.add_vertex("A")
xgraph.add_vertex("B")
xgraph.add_vertex("C")
xgraph.add_vertex("D")

xgraph.add_edge("A", "B")
xgraph.add_edge("A", "C")
xgraph.add_edge("A", "D")
xgraph.add_edge("B", "D")
xgraph.add_edge("C", "D")v

# xgraph.print_graph()
# xgraph.remove_vertex("D")
xgraph.print_graph()

xgraph.dfs("A")
