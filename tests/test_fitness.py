from src.genome.individual import Individual
from src.genome.stroke import Stroke
from src.genome.constraints import MIN_STROKES, MAX_STROKES
from src.utils.random import random_color, random_int, random_coord, random_thickness, random_alpha
from src.render.renderer import Renderer
from src.fitness.combined import combined_fitness
from src.utils.image_io import load_image, save_image


def create_random_individual():
    """Create a random individual for testing."""
    bg_color = random_color()
    num_strokes = random_int(MIN_STROKES, MAX_STROKES)
    strokes = []
    for _ in range(num_strokes):
        x1, y1 = random_coord()
        x2, y2 = random_coord()
        thickness = random_thickness()
        color = random_color()
        alpha = random_alpha()
        strokes.append(Stroke(x1, y1, x2, y2, thickness, color, alpha))
    return Individual(bg_color, strokes)


def test_fitness():
    # Load target image and resize to canvas size
    target = load_image('data/target/target.jpg')
    from src.genome.constraints import CANVAS_WIDTH, CANVAS_HEIGHT
    target = target.resize((CANVAS_WIDTH, CANVAS_HEIGHT))
    print(f"Target image size: {target.size}, mode: {target.mode}")

    # Show target
    target.show()

    # Create renderer
    renderer = Renderer()

    # Generate and test a few random individuals
    for i in range(3):
        ind = create_random_individual()
        img = renderer.render(ind)
        score = combined_fitness(img, target)
        print(f"Random individual {i}: fitness = {score:.4f}, strokes = {ind.num_strokes()}")
        save_image(img, f'data/outputs/random_{i}.png')
        # img.show()  # Uncomment to show each rendered image

    print("Fitness tests completed. Check data/outputs/ for saved images.")


if __name__ == "__main__":
    test_fitness()