
from src.render.canvas import create_canvas
from src.render.stroke_draw import draw_stroke


class Renderer:
    """Responsible for converting an Individual into an image."""
    def render(self, individual):
        """
        Render an individual into a PIL Image.

        Parameters
        ----------
        individual : Individual
            The individual to render

        Returns
        -------
        PIL.Image.Image
            The rendered image
        """
        # Create canvas with background color
        canvas = create_canvas(individual.bg_color)

        # Draw each stroke
        for stroke in individual.strokes:
            draw_stroke(canvas, stroke)

        return canvas
