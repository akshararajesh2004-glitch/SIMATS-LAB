def hill_climbing_verbose_fast(initial_state, neighbors_func, heuristic_func, max_iterations=20):
    current = initial_state
    current_value = heuristic_func(current)
    
    print(f"Initial state: {current}, Heuristic value: {current_value}\n")
    
    for i in range(1, max_iterations + 1):
        neighbors = neighbors_func(current)
        if not neighbors:
            print("No neighbors to explore. Stopping.")
            break
        
        # Evaluate neighbors
        neighbor_values = [(n, heuristic_func(n)) for n in neighbors]
        # Choose best neighbor
        next_state, next_value = max(neighbor_values, key=lambda x: x[1])
        
        print(f"Iteration {i}: Current={current}, Heuristic={current_value} -> Next={next_state}, Heuristic={next_value}")
        
        if next_value <= current_value:
            print("\nNo better neighbor found. Reached peak.")
            break
        
        current, current_value = next_state, next_value
    
    print(f"\nFinal state: {current}, Maximum value: {current_value}")
    return current, current_value

# Example: maximize f(x) = -(x-3)^2 + 9
def heuristic(x):
    return -(x-3)**2 + 9

def neighbors(x):
    step = 0.5  # bigger step → fewer iterations
    return [x - step, x + step]

# Run hill climbing
initial_state = 0
hill_climbing_verbose_fast(initial_state, neighbors, heuristic)
