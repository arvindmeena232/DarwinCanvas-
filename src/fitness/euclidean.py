import numpy as np
from skimage import color
from src.fitness.normalize import normalize

def compute_euclidean(img1, img2):

    # Convert to RGB if necessary
    if img1.mode != 'RGB':
        img1 = img1.convert('RGB')
    if img2.mode != 'RGB':
        img2 = img2.convert('RGB')

    # Convert to numpy arrays
    arr1 = np.array(img1)
    arr2 = np.array(img2)


    # Compute Delta E for each pixel (Euclidean distance in Lab)
    diff = arr1 - arr2
    delta_e_values = np.sqrt(np.sum(diff ** 2, axis=2))
    normalized_value = normalize(np.mean(delta_e_values))
    # Return mean Delta E
    return normalized_value