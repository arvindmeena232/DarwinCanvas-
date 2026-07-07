from PIL import Image


def load_image(path):
    """
    Load an image from file.

    Parameters
    ----------
    path : str
        Path to the image file

    Returns
    -------
    PIL.Image.Image
        Loaded image
    """
    return Image.open(path)


def save_image(img, path):
    """
    Save an image to file.

    Parameters
    ----------
    img : PIL.Image.Image
        Image to save
    path : str
        Path to save the image
    """
    img.save(path)
