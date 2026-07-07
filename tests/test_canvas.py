from src.render.canvas import create_canvas

def test_create_canvas():
    img = create_canvas((100, 150, 200))
    img.show()

if __name__ == "__main__" :
    test_create_canvas()
