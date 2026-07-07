from PIL import Image, ImageDraw
from src.genome.constraints import CANVAS_WIDTH, CANVAS_HEIGHT
from src.render.utils import clamp_coords

def draw_stroke(canvas, stroke):
    """
    Draw a single stroke on the canvas using Alpha Compositing.
    """
    # 1. Clamp coordinates
    x1, y1 = clamp_coords(stroke.x1, stroke.y1, CANVAS_WIDTH, CANVAS_HEIGHT)
    x2, y2 = clamp_coords(stroke.x2, stroke.y2, CANVAS_WIDTH, CANVAS_HEIGHT)

    # 2. Create a temporary transparent layer (The Overlay)
    # We create a new empty image the same size as the canvas
    overlay = Image.new('RGBA', canvas.size, (0, 0, 0, 0))
    draw = ImageDraw.Draw(overlay)

    # 3. Draw the stroke on the overlay
    # This stroke is floating in empty space, so no blending issues here
    r, g, b = stroke.color
    fill = (r, g, b, stroke.alpha)
    draw.line([(x1, y1), (x2, y2)], fill=fill, width=stroke.thickness)

    # 4. Merge the overlay onto the main canvas
    # alpha_composite implements proper "Painter's Algorithm" blending
    # It ensures the background remains opaque (255 alpha)
    canvas.alpha_composite(overlay)