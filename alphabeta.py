import math

# Example game tree as nested lists (leaves are scores)
# Internal nodes are lists: [child1, child2, ...]
game_tree = [[3,5,[6,9]], [1,2], [0,[4,7]]]

def alpha_beta(node, depth, alpha, beta, maximizing):
    if not isinstance(node, list) or depth == 0:
        return node
    if maximizing:
        value = -math.inf
        for child in node:
            value = max(value, alpha_beta(child, depth-1, alpha, beta, False))
            alpha = max(alpha, value)
            if alpha >= beta: break
        return value
    else:
        value = math.inf
        for child in node:
            value = min(value, alpha_beta(child, depth-1, alpha, beta, True))
            beta = min(beta, value)
            if alpha >= beta: break
        return value

# Run Alpha-Beta pruning
best_value = alpha_beta(game_tree, depth=3, alpha=-math.inf, beta=math.inf, maximizing=True)
print("Best value for maximizer:", best_value)
