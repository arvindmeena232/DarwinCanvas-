import random

def tournament_selection(population, fitness_values, k):
    selected = random.sample(list(zip(population, fitness_values)), k)
    best_individual, _ = min(selected, key=lambda x: x[1])  # lower fitness = better
    return best_individual
