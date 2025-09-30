import random

# Parameters
POP_SIZE = 6         # Population size
GENE_LENGTH = 5      # Bits to represent x (0-31)
MUTATION_RATE = 0.1
GENERATIONS = 5

# Fitness function
def fitness(x):
    return x**2

# Convert binary to decimal
def binary_to_decimal(binary):
    return int(binary, 2)

# Create initial population
def create_population():
    population = []
    for _ in range(POP_SIZE):
        gene = ''.join(random.choice('01') for _ in range(GENE_LENGTH))
        population.append(gene)
    return population

# Selection (roulette wheel)
def select(population):
    fitness_scores = [fitness(binary_to_decimal(gene)) for gene in population]
    total = sum(fitness_scores)
    probs = [f/total for f in fitness_scores]
    selected = random.choices(population, probs, k=2)
    return selected

# Crossover (single point)
def crossover(parent1, parent2):
    point = random.randint(1, GENE_LENGTH-1)
    child1 = parent1[:point] + parent2[point:]
    child2 = parent2[:point] + parent1[point:]
    return child1, child2

# Mutation
def mutate(gene):
    gene = list(gene)
    for i in range(len(gene)):
        if random.random() < MUTATION_RATE:
            gene[i] = '1' if gene[i] == '0' else '0'
    return ''.join(gene)

# Main GA loop
population = create_population()
print("Initial Population:", population)

for gen in range(GENERATIONS):
    new_population = []
    while len(new_population) < POP_SIZE:
        parent1, parent2 = select(population)
        child1, child2 = crossover(parent1, parent2)
        new_population.append(mutate(child1))
        if len(new_population) < POP_SIZE:
            new_population.append(mutate(child2))
    population = new_population
    best = max(population, key=lambda g: fitness(binary_to_decimal(g)))
    print(f"Generation {gen+1}: Best gene = {best}, Value = {binary_to_decimal(best)}, Fitness = {fitness(binary_to_decimal(best))}")

# Final best solution
best_gene = max(population, key=lambda g: fitness(binary_to_decimal(g)))
best_value = binary_to_decimal(best_gene)
print("\nBest solution found:")
print(f"Gene: {best_gene}, Value: {best_value}, Fitness: {fitness(best_value)}")
