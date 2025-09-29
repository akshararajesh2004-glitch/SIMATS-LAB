import matplotlib.pyplot as plt
import networkx as nx

# Create a graph
G = nx.Graph()

# Add edges (including a separate component)
edges = [
    ('A', 'B'), ('A', 'C'), ('A', 'D'),
    ('B', 'E'), ('B', 'F'), ('F', 'H'),
    ('D', 'G'),
    ('X', 'Y')  # separate component
]

G.add_edges_from(edges)

# DFS Traversal
def dfs(G, start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)
    print(start, end=" ")
    for neighbor in G.neighbors(start):
        if neighbor not in visited:
            dfs(G, neighbor, visited)
    return visited

# DFS for all components
visited_all = set()
print("DFS Traversal:")
for node in G.nodes():
    if node not in visited_all:
        print(f"\nStarting new component from {node}: ", end="")
        visited = dfs(G, node)
        visited_all.update(visited)

# Draw the graph
pos = nx.spring_layout(G)  # positions for all nodes
plt.figure(figsize=(8,6))
nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=1000, font_size=12, font_weight='bold')
plt.title("Graph Visualization")
plt.show()
