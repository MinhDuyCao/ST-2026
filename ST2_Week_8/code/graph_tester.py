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

print("\nBFS starting from vertex 'A':")
visited_bfs = g.bfs('A')
print("Visited vertices in BFS order:", visited_bfs)

print("\nDFS starting from vertex 'A':")
visited_dfs = g.dfs('A')
print("Visited vertices in DFS order:", visited_dfs)

print("\n=== Cycle Detection Tests ===")

cycle_graph = Graph(directed=False)
for v in ['A', 'B', 'C']:
    cycle_graph.add_vertex(v)
cycle_graph.add_edge('A', 'B')
cycle_graph.add_edge('B', 'C')
cycle_graph.add_edge('C', 'A')

print("Cycle graph has cycle:", cycle_graph.has_undirected_cycle())

acyclic_graph = Graph(directed=False)
for v in ['X', 'Y', 'Z']:
    acyclic_graph.add_vertex(v)
acyclic_graph.add_edge('X', 'Y')
acyclic_graph.add_edge('Y', 'Z')

print("Acyclic graph has cycle:", acyclic_graph.has_undirected_cycle())

wg = Graph(directed=True, weighted=True)
for v in ['A', 'B', 'C']:
    wg.add_vertex(v)

wg.add_edge('A', 'B', weight=15)
wg.add_edge('B', 'C', weight=34)
wg.add_edge('A', 'C', weight=50)

print("\nWeighted Directed Graph:")
wg.print_graph()