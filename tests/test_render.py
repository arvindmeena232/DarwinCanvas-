from src.render.renderer import Renderer
from src.genome.individual import Individual
from src.genome.stroke import Stroke

def test_render():
    # Create a simple individual
    bg_color = (255, 255, 255)  # white background
    strokes = [
        Stroke(10, 10, 50, 50, 5, (255, 0, 0), 255),  # red line
        Stroke(20, 20, 40, 40, 3, (0, 255, 0), 200),  # green line with alpha
    ]
    individual = Individual(bg_color, strokes)

    # Render
    renderer = Renderer()
    img = renderer.render(individual)

    # Show the image (optional, for visual check)
    img.show()

    # Basic checks
    assert img.size == (64, 64)
    assert img.mode == "RGBA"

    print("Render test passed!")

if __name__ == "__main__":
    test_render()