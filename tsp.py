import random
import math
import matplotlib.pyplot as plt

# Cities coordinates
cities = [(0,0), (2,3), (5,2), (6,6), (8,3)]

POP_SIZE = 6
GENERATIONS = 10
MUTATION_RATE = 0.2

# Distance function
def distance(a, b):
    return math.sqrt((a[0]-b[0])**2 + (a[1]-b[1])**2)

def total_distance(path):
    dist = 0
    for i in range(len(path)-1):
        dist += distance(path[i], path[i+1])
    dist += distance(path[-1], path[0])
    return dist

# Create initial population
def create_population():
    population = []
    for _ in range(POP_SIZE):
        individual = cities[:]
        random.shuffle(individual)
        population.append(individual)
    return population

# Tournament selection
def select(population):
    tournament = random.sample(population, 2)
    tournament.sort(key=total_distance)
    return tournament[0], tournament[1]

# Ordered crossover
def crossover(parent1, parent2):
    start, end = sorted(random.sample(range(len(parent1)), 2))
    child = [None]*len(parent1)
    child[start:end+1] = parent1[start:end+1]
    p2_genes = [city for city in parent2 if city not in child]
    pointer = 0
    for i in range(len(child)):
        if child[i] is None:
            child[i] = p2_genes[pointer]
            pointer += 1
    return child

# Mutation (swap two cities)
def mutate(individual):
    if random.random() < MUTATION_RATE:
        i, j = random.sample(range(len(individual)), 2)
        individual[i], individual[j] = individual[j], individual[i]
    return individual

# Plot path
def plot_path(path, gen):
    x = [c[0] for c in path] + [path[0][0]]
    y = [c[1] for c in path] + [path[0][1]]
    plt.figure(figsize=(5,5))
    plt.plot(x, y, 'o-', color='blue')
    for i, city in enumerate(path):
        plt.text(city[0]+0.1, city[1]+0.1, f"C{i}")
    plt.title(f"Generation {gen}")
    plt.show()

# GA main loop
population = create_population()
for gen in range(GENERATIONS):
    new_population = []
    while len(new_population) < POP_SIZE:
        parent1, parent2 = select(population)
        child = crossover(parent1, parent2)
        child = mutate(child)
        new_population.append(child)
    population = new_population
    best = min(population, key=total_distance)
    print(f"Generation {gen+1}: Best distance = {total_distance(best):.2f}")

# Final best path
best_path = min(population, key=total_distance)
print("\nBest path found:")
for i, city in enumerate(best_path):
    print(f"C{i}: {city}")
print(f"Total distance: {total_distance(best_path):.2f}")

# Plot final path
plot_path(best_path, "Final")
