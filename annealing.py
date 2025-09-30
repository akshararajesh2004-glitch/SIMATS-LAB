import random
import math
import matplotlib.pyplot as plt
import numpy as np

# Objective function
def f(x):
    return x**2 + 4*math.sin(5*x) + 2*math.cos(3*x)

# Neighbor solution (small random step)
def neighbor(x):
    return x + random.uniform(-0.5, 0.5)

def simulated_annealing(T0=100, alpha=0.98, max_iter=1000, min_T=1e-3):
    current = random.uniform(-10, 10)  # start randomly
    current_cost = f(current)
    best = current
    best_cost = current_cost
    T = T0
    history = []

    for i in range(max_iter):
        candidate = neighbor(current)
        cand_cost = f(candidate)
        delta = cand_cost - current_cost

        # Accept if better, else with probability
        if delta < 0 or random.random() < math.exp(-delta/T):
            current, current_cost = candidate, cand_cost
            if current_cost < best_cost:
                best, best_cost = current, current_cost

        history.append(best_cost)
        T *= alpha
        if T < min_T:
            break
    return best, best_cost, history

# Run
best_x, best_val, history = simulated_annealing()

print(f"Best x found: {best_x:.4f}")
print(f"Function minimum value: {best_val:.4f}")

# Plot convergence
plt.plot(history)
plt.xlabel("Iteration")
plt.ylabel("Best f(x)")
plt.title("Simulated Annealing Convergence")
plt.show()

# Plot function and minimum
X = np.linspace(-10, 10, 400)
Y = [f(x) for x in X]
plt.plot(X, Y, label="f(x)")
plt.plot(best_x, best_val, 'ro', label="Best found")
plt.legend()
plt.title("Function Minimization using SA")
plt.show()
 