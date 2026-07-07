import random
import math  # <--- Needed for sin/cos
from src.genome.individual import Individual
from src.genome.stroke import Stroke
from src.genome.constraints import (
    MIN_STROKES, MAX_STROKES,
    THICKNESS_MIN, THICKNESS_MAX,
    MIN_LENGTH, MAX_LENGTH,  # <--- Using these now
    ALPHA_MIN, ALPHA_MAX,
    CANVAS_WIDTH, CANVAS_HEIGHT,
)

def generate_random_stroke():
    # 1. Pick a random starting point
    x1 = random.randint(0, CANVAS_WIDTH - 1)
    y1 = random.randint(0, CANVAS_HEIGHT - 1)

    # 2. Pick a random length and angle
    length = random.uniform(MIN_LENGTH, MAX_LENGTH)
    angle = random.uniform(0, 2 * math.pi)  # 0 to 360 degrees in radians

    # 3. Calculate end point using trigonometry
    # x2 = x1 + length * cos(angle)
    x2 = x1 + int(length * math.cos(angle))
    y2 = y1 + int(length * math.sin(angle))

    # 4. Clamp the values to keep them inside the canvas
    # (Note: If a stroke hits the edge, this might make it slightly shorter 
    # than MIN_LENGTH, but that is acceptable for avoiding crashes)
    x2 = min(max(x2, 0), CANVAS_WIDTH - 1)
    y2 = min(max(y2, 0), CANVAS_HEIGHT - 1)

    return Stroke(
        x1=x1,
        y1=y1,
        x2=x2,
        y2=y2,
        thickness=random.randint(THICKNESS_MIN, THICKNESS_MAX),
        color=(
            random.randint(0, 255),
            random.randint(0, 255),
            random.randint(0, 255)
        ),
        alpha=random.randint(ALPHA_MIN, ALPHA_MAX)
    )

# ... (rest of your code remains the same)
def generate_random_individual():
    bg_color = (
        random.randint(0, 255),
        random.randint(0, 255),
        random.randint(0, 255)
    )

    num_strokes = random.randint(MIN_STROKES, MAX_STROKES)
    strokes = [generate_random_stroke() for _ in range(num_strokes)]

    return Individual(bg_color, strokes)


def initialize_population(pop_size):
    return [generate_random_individual() for _ in range(pop_size)]
