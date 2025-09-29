from collections import defaultdict, deque

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    # Add edge (u → v)
    def add_edge(self, u, v, directed=False):
        self.graph[u].append(v)
        if not directed:   # for undirected graphs
            self.graph[v].append(u)

    # BFS with distance tracking
    def bfs(self, start):
        visited = set()
        queue = deque([start])
        distance = {start: 0}   # store distance from start

        while queue:
            node = queue.popleft()
            if node not in visited:
                print(f"Node: {node}, Distance: {distance[node]}")
                visited.add(node)

                for neighbor in self.graph[node]:
                    if neighbor not in visited and neighbor not in queue:
                        queue.append(neighbor)
                        distance[neighbor] = distance[node] + 1

        return distance

    # Run BFS for all components
    def bfs_all_components(self):
        visited = set()
        all_distances = {}
        for node in self.graph:
            if node not in visited:
                print(f"\nStarting new component from {node}")
                dist = self.bfs(node)
                visited.update(dist.keys())
                all_distances.update(dist)
        return all_distances


# Example usage
g = Graph()
edges = [
    ('A', 'B'), ('A', 'C'),
    ('B', 'D'), ('B', 'E'),
    ('C', 'F'),
    ('E', 'F'),
    ('G', 'H')   # separate component
]

for u, v in edges:
    g.add_edge(u, v)

print("BFS Traversal with Distances:")
all_distances = g.bfs_all_components()
print("\nFinal Distances:", all_distances)
