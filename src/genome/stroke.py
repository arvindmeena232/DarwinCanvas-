class Stroke:
    """
    Represents a single paint stroke in an individual's genome.
    The renderer interprets these parameters into a visual stroke.
    """

    def __init__(self, x1, y1, x2, y2, thickness, color, alpha):
        self.x1 = x1  # start point
        self.y1 = y1
        self.x2 = x2  # end point
        self.y2 = y2

        self.thickness = thickness  # stroke width

        # color = (r, g, b)
        self.color = tuple(color)

        # alpha transparency (0–255)
        self.alpha = alpha

    def clone(self):
        """Return a deep copy of the stroke."""
        return Stroke(
            self.x1, self.y1,
            self.x2, self.y2,
            self.thickness,
            self.color,
            self.alpha
        )
