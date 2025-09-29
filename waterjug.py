from collections import deque

def water_jug_problem(jug1_capacity, jug2_capacity, goal):
    visited = set()
    queue = deque()
    
    # Each state: (jug1_amount, jug2_amount, path)
    queue.append((0, 0, []))
    visited.add((0, 0))
    
    while queue:
        jug1, jug2, path = queue.popleft()
        current_path = path + [(jug1, jug2)]
        
        if jug1 == goal:
            print("Solution path:")
            for step in current_path:
                print(step)
            return
        
        next_states = []
        # Fill jug1
        next_states.append((jug1_capacity, jug2))
        # Fill jug2
        next_states.append((jug1, jug2_capacity))
        # Empty jug1
        next_states.append((0, jug2))
        # Empty jug2
        next_states.append((jug1, 0))
        # Pour jug1 -> jug2
        pour_to_jug2 = min(jug1, jug2_capacity - jug2)
        next_states.append((jug1 - pour_to_jug2, jug2 + pour_to_jug2))
        # Pour jug2 -> jug1
        pour_to_jug1 = min(jug2, jug1_capacity - jug1)
        next_states.append((jug1 + pour_to_jug1, jug2 - pour_to_jug1))
        
        for state in next_states:
           if (state[0], state[1]) not in visited:
                queue.append((state[0], state[1], current_path))
                visited.add((state[0], state[1]))

    print("No solution found.")

# Corrected example: Jug1 = 5L, Jug2 = 3L, Goal = 4L
water_jug_problem(5, 3, 4)