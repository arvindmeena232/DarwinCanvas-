
def clamp(value, min_val, max_val):
    """Clamp a value to the range [min_val, max_val]."""
    return max(min_val, min(value, max_val))


def clamp_coords(x, y, width, height):
    """Clamp coordinates to canvas bounds."""
    x_clamped = clamp(x, 0, width - 1)
    y_clamped = clamp(y, 0, height - 1)
    return x_clamped, y_clamped
