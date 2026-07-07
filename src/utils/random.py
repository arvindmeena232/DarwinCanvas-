
import random as rnd


def random_int(min_val, max_val):
    """Return a random integer between min_val and max_val inclusive."""
    return rnd.randint(min_val, max_val)


def random_float(min_val, max_val):
    """Return a random float between min_val and max_val."""
    return rnd.uniform(min_val, max_val)


def random_color():
    """Return a random RGB color tuple."""
    return (random_int(0, 255), random_int(0, 255), random_int(0, 255))


def random_alpha():
    """Return a random alpha value within constraints."""
    from src.genome.constraints import ALPHA_MIN, ALPHA_MAX
    return random_int(ALPHA_MIN, ALPHA_MAX)


def random_thickness():
    """Return a random thickness within constraints."""
    from src.genome.constraints import THICKNESS_MIN, THICKNESS_MAX
    return random_int(THICKNESS_MIN, THICKNESS_MAX)


def random_coord():
    """Return a random coordinate within canvas bounds."""
    from src.genome.constraints import CANVAS_WIDTH, CANVAS_HEIGHT
    return random_int(0, CANVAS_WIDTH - 1), random_int(0, CANVAS_HEIGHT - 1)