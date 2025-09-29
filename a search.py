import heapq

def a_star_search(start, goal, graph, h):
    """
    start: starting node
    goal: goal node
    graph: adjacency list with edge costs {node: [(neighbor, cost), ...]}
    h: heuristic function {node: estimated cost to goal}
    """
    open_set = []
    heapq.heappush(open_set, (h[start], 0, start, [start]))  # (f, g, node, path)
    visited = set()
    
    while open_set:
        f, g, node, path = heapq.heappop(open_set)
        
        if node == goal:
            return path, g  # path and total cost
        
        if node in visited:
            continue
        visited.add(node)
        
        for neighbor, cost in graph.get(node, []):
            if neighbor not in visited:
                g_new = g + cost
                f_new = g_new + h.get(neighbor, 0)
                heapq.heappush(open_set, (f_new, g_new, neighbor, path + [neighbor]))
    
    return None, float('inf')

# Example graph
graph = {
    'A': [('B', 1), ('C', 3)],
    'B': [('D', 3), ('E', 1)],
    'C': [('F', 5)],
    'D': [],
    'E': [('F', 2)],
    'F': []
}

# Heuristic (estimated cost to goal F)
h = {
    'A': 5,
    'B': 4,
    'C': 2,
    'D': 6,
    'E': 2,
    'F': 0
}

start_node = 'A'
goal_node = 'F'

path, cost = a_star_search(start_node, goal_node, graph, h)
print(f"Path: {path}")
print(f"Total cost: {cost}")
