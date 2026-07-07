import copy  # <--- Add this import

def apply_elitism(population, fitness_values, elite_size):
    paired = list(zip(population, fitness_values))
    paired.sort(key=lambda x: x[1])  # lower score = better
    
    # OLD CODE (References only):
    # elites = [ind for ind, score in paired[:elite_size]]
    
    # NEW CODE (Actual Backups):
    # We use deepcopy to create a completely new, independent clone of the object
    elites = [copy.deepcopy(ind) for ind, score in paired[:elite_size]]
    
    return elites
