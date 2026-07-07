import random
import copy
from src.genome.individual import Individual
from src.genome.constraints import CANVAS_WIDTH

def crossover(parent1, parent2):
    """
    Hybrid Crossover:
    - 50% chance: Spatial Crossover (Splits image vertically)
    - 50% chance: Blending Crossover (Mixes strokes stochastically)
    """

    # --- STRATEGY 1: SPATIAL CROSSOVER (Structure Preserving) ---
    if random.random() < 0.4:
        # 1. Randomly inherit background color
        bg_color = parent1.bg_color if random.random() < 0.5 else parent2.bg_color

        # 2. Pick a random vertical line to cut the canvas
        split_x = random.randint(0, CANVAS_WIDTH)
        child_strokes = []

        # 3. Inherit "Left Side" strokes from Parent 1
        for stroke in parent1.strokes:
            center_x = (stroke.x1 + stroke.x2) // 2
            if center_x < split_x:
                child_strokes.append(copy.deepcopy(stroke))

        # 4. Inherit "Right Side" strokes from Parent 2
        for stroke in parent2.strokes:
            center_x = (stroke.x1 + stroke.x2) // 2
            if center_x >= split_x:
                child_strokes.append(copy.deepcopy(stroke))
        
        return Individual(bg_color, child_strokes)

    # --- STRATEGY 2: BLENDING CROSSOVER (Feature Mixing) ---
    else:
        # 1. Sample the blend ratio 'x' (e.g., 0.7 means 70% parent1)
        ratio = random.random()

        # 2. Determine target stroke count (Maximum of parents to allow growth)
        target_size = max(len(parent1.strokes), len(parent2.strokes))
        
        # 3. Calculate quotas
        count_p1 = int(target_size * ratio)
        count_p2 = target_size - count_p1

        # 4. Select strokes (Random Sample)
        # We limit the sample size to available strokes to avoid errors
        take_p1 = min(len(parent1.strokes), count_p1)
        take_p2 = min(len(parent2.strokes), count_p2)
        
        strokes_from_p1 = random.sample(parent1.strokes, take_p1)
        strokes_from_p2 = random.sample(parent2.strokes, take_p2)

        # 5. Combine and Shuffle
        # Shuffling is crucial so one parent doesn't dominate the top layer
        child_strokes = copy.deepcopy(strokes_from_p1 + strokes_from_p2)
        random.shuffle(child_strokes)

        # 6. Blend Background Color mathematically
        r = int(parent1.bg_color[0] * ratio + parent2.bg_color[0] * (1 - ratio))
        g = int(parent1.bg_color[1] * ratio + parent2.bg_color[1] * (1 - ratio))
        b = int(parent1.bg_color[2] * ratio + parent2.bg_color[2] * (1 - ratio))
        child_bg = (r, g, b)

        return Individual(child_bg, child_strokes)