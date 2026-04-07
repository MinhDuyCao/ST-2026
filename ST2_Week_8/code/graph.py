# === graph.py ===

class Graph:
    def __init__(self, directed=False, weighted=False):
        self.graph = {}
        self.weights = {}
        self.directed = directed
        self.weighted = weighted

    def add_vertex(self, vertex):
        if vertex not in self.graph:
            self.graph[vertex] = []

    def add_edge(self, vertex1, vertex2, weight=0):
        if vertex1 in self.graph and vertex2 in self.graph:
            self.graph[vertex1].append(vertex2)

            if self.weighted:
                self.weights[(vertex1, vertex2)] = weight

            if not self.directed:
                self.graph[vertex2].append(vertex1)
                if self.weighted:
                    self.weights[(vertex2, vertex1)] = weight
        else:
            print("One or both vertices not found in graph.")

    def remove_edge(self, v1, v2):
        if v1 in self.graph and v2 in self.graph[v1]:
            self.graph[v1].remove(v2)
        if not self.directed and v2 in self.graph and v1 in self.graph[v2]:
            self.graph[v2].remove(v1)

    def remove_vertex(self, v):
        if v in self.graph:
            del self.graph[v]
        for key in self.graph:
            if v in self.graph[key]:
                self.graph[key].remove(v)

    def print_graph(self):
        for v in self.graph:
            print(f"{v} -> {self.graph[v]}")

    # BFS
    def bfs(self, start):
        visited = []
        queue = [start]

        while queue:
            v = queue.pop(0)
            if v not in visited:
                visited.append(v)
                for nbr in self.graph[v]:
                    if nbr not in visited:
                        queue.append(nbr)
        return visited

    # DFS
    def dfs(self, start):
        visited = []
        stack = [start]

        while stack:
            v = stack.pop()
            if v not in visited:
                visited.append(v)
                for nbr in reversed(self.graph[v]):
                    if nbr not in visited:
                        stack.append(nbr)
        return visited

    # Undirected cycle detection
    def has_undirected_cycle(self):
        visited = set()

        def dfs(v, parent):
            visited.add(v)
            for nbr in self.graph[v]:
                if nbr not in visited:
                    if dfs(nbr, v):
                        return True
                elif nbr != parent:
                    return True
            return False

        for v in self.graph:
            if v not in visited:
                if dfs(v, None):
                    return True
        return False
# === graph_tester.py ===
from graph import Graph

print("=== Undirected Graph Test ===")
g = Graph()
g.add_vertex('A')
g.add_vertex('B')
g.add_vertex('C')
g.add_edge('A', 'B')
g.add_edge('B', 'C')
g.print_graph()

print("\n=== Directed Graph Test ===")
g = Graph(directed=True)
g.add_vertex('A')
g.add_vertex('B')
g.add_vertex('C')
g.add_edge('A', 'B')
g.add_edge('B', 'C')
g.print_graph()

print("\n=== Weighted Directed Graph Test ===")
g = Graph(weighted=True, directed=True)
g.add_vertex('A')
g.add_vertex('B')
g.add_vertex('C')
g.add_edge('A', 'B', 15)
g.add_edge('B', 'C', 34)
g.print_graph()

print("\n=== Removal Test ===")
removal_test = Graph()
removal_test.add_vertex('A')
removal_test.add_vertex('B')
removal_test.add_vertex('C')
removal_test.add_edge('A', 'B')
removal_test.add_edge('B', 'C')
removal_test.print_graph()

removal_test.remove_edge('A', 'B')
removal_test.print_graph()

removal_test.remove_vertex('C')
removal_test.print_graph()