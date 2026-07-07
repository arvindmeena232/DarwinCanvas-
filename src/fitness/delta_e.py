import numpy as np
from skimage import color
from src.fitness.normalize import normalize

def compute_delta_e(img1, img2):
    """
    Compute the mean Delta E (CIE76) between two images.

    Parameters
    ----------
    img1 : PIL.Image.Image
        First image (rendered)
    img2 : PIL.Image.Image
        Second image (target)

    Returns
    -------
    float
        Mean Delta E value (lower = more similar)
    """
    # Convert to RGB if necessary
    if img1.mode != 'RGB':
        img1 = img1.convert('RGB')
    if img2.mode != 'RGB':
        img2 = img2.convert('RGB')

    # Convert to numpy arrays
    arr1 = np.array(img1)
    arr2 = np.array(img2)

    # Convert to Lab color space
    lab1 = color.rgb2lab(arr1)
    lab2 = color.rgb2lab(arr2)

    # Compute Delta E for each pixel (Euclidean distance in Lab)
    diff = lab1 - lab2
    delta_e_values = np.sqrt(np.sum(diff ** 2, axis=2))
    normalized_value = normalize(np.mean(delta_e_values))
    # Return mean Delta E
    return normalized_value