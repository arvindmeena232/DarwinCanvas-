from PIL import Image
from src.genome.constraints import CANVAS_WIDTH, CANVAS_HEIGHT


def create_canvas(bg_color):
    """
    Create a blank RGBA canvas filled with background color.

    Parameters
    ----------
    bg_color : tuple(int, int, int)
        Background color as (R, G, B)

    Returns
    -------
    PIL.Image.Image
        RGBA image canvas
    """

    # Validate background color
    if len(bg_color) != 3:
        raise ValueError("Background color must be an (R, G, B) tuple")

    r, g, b = bg_color
    if not all(0 <= v <= 255 for v in (r, g, b)):
        raise ValueError("Background color values must be in range 0–255")

    # Convert RGB → RGBA (full opacity)
    rgba_color = (r, g, b, 255)

    # Create canvas
    canvas = Image.new(
        mode="RGBA",
        size=(CANVAS_WIDTH, CANVAS_HEIGHT),
        color=rgba_color
    )

    return canvas
