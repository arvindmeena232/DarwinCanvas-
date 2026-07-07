from .stroke import Stroke
from .constraints import MIN_STROKES, MAX_STROKES

class Individual:
    """
    A genome consisting of:
    - background color (r, g, b)
    - a list of Stroke objects
    """

    def __init__(self, bg_color, strokes):
        self.bg_color = tuple(bg_color)  # (r, g, b)
        self.strokes = strokes  # list[Stroke]

    def num_strokes(self):
        return len(self.strokes)

    def clone(self):
        """Return a deep copy of the entire individual."""
        new_strokes = [s.clone() for s in self.strokes]
        return Individual(self.bg_color, new_strokes)

    def validate(self):
        """
        Ensures this individual follows genome constraints.
        Call after crossover or mutation.
        """
        # Keep stroke count within limits
        if len(self.strokes) < MIN_STROKES:
            raise ValueError("Too few strokes")
        if len(self.strokes) > MAX_STROKES:
            raise ValueError("Too many strokes")

        # Background color must be valid
        r, g, b = self.bg_color
        assert 0 <= r <= 255 and 0 <= g <= 255 and 0 <= b <= 255
        
        # Ensure each stroke is valid
        for s in self.strokes:
            assert 0 <= s.x1 <= 64 and 0 <= s.y1 <= 64
            assert 0 <= s.x2 <= 64 and 0 <= s.y2 <= 64
            assert 1 <= s.thickness <= 10
            pr, pg, pb = s.color
            assert 0 <= pr <= 255 and 0 <= pg <= 255 and 0 <= pb <= 255
            assert 80 <= s.alpha <= 255
