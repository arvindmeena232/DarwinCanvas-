from src.ga.selection import tournament_selection
from src.ga.crossover import crossover
from src.ga.mutation import mutate
from src.ga.elitism import apply_elitism

def evolve(population,
           fitness_values,
           pop_size,
           tournament_k,
           mutation_rate,
           elite_size,
           decay=0.5):

    new_population = []

    # elitism first
    elites = apply_elitism(population, fitness_values, elite_size)
    new_population.extend(elites)

    while len(new_population) < pop_size:
        p1 = tournament_selection(population, fitness_values, tournament_k)
        p2 = tournament_selection(population, fitness_values, tournament_k)

        child = crossover(p1, p2)
        child = mutate(child, mutation_rate, decay)

        new_population.append(child)

    return new_population
