import yaml

from src.ga.population import initialize_population
from src.ga.evolve import evolve

from src.render.renderer import Renderer
from src.fitness.combined import combined_fitness
from src.utils.image_io import load_image
import numpy as np
import matplotlib.pyplot as plt

def main():

    print("Starting Evolution Phase...")

    # load GA config
    with open("config/ga.yaml", "r") as f:
        cfg = yaml.safe_load(f)

    pop_size      = cfg["population_size"]
    generations   = cfg["generations"]
    mutation_rate = cfg["mutation_rate"]
    tournament_k  = cfg["tournament_k"]
    elite_size    = cfg["elitism"]

    # load target image
    target = load_image("data/target/target64.jpg")

    renderer = Renderer()

    # generate initial population
    population = initialize_population(pop_size)

    for gen in range(generations):

        # render each individual
        rendered_images = [
            renderer.render(individual)
            for individual in population
        ]
        decay = gen/generations
        # compute fitness for each rendered image
        fitness_values = [
            combined_fitness(img, target,decay)
            for img in rendered_images
            
        ]

        # evolve population for next generation
        population = evolve(
            population,
            fitness_values,
            pop_size,
            tournament_k,
            mutation_rate,
            elite_size,
            decay,
        )

        # report progress (best score)
        print(f"Generation {gen}: best fitness = {min(fitness_values)}")
        if(gen%100 == 0):
            best_idx = fitness_values.index(min(fitness_values))
            best_img = rendered_images[best_idx]
            best_img.save(f"data/outputs/gen{gen}_best.png")
            print(f"Generation {gen}: best image saved.")

    # after evolution loop ends
    best_idx = fitness_values.index(min(fitness_values))
    best_img = rendered_images[best_idx]
    best_img.save("data/outputs/final_best.png")
    print("Final best image saved.")


if __name__ == "__main__":
    main()
