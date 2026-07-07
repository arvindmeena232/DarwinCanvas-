import numpy as np
from skimage.metrics import structural_similarity


def compute_ssim(img1, img2):
    """
    Compute Structural Similarity Index (SSIM) between two images.

    Parameters
    ----------
    img1 : PIL.Image.Image
        First image (rendered)
    img2 : PIL.Image.Image
        Second image (target)

    Returns
    -------
    float
        SSIM value in [0, 1] (higher = more similar)
    """
    # Convert to RGB if necessary
    if img1.mode != 'RGB':
        img1 = img1.convert('RGB')
    if img2.mode != 'RGB':
        img2 = img2.convert('RGB')

    # Convert to numpy arrays
    arr1 = np.array(img1)
    arr2 = np.array(img2)

    # Compute SSIM (multichannel for RGB)
    ssim_value = structural_similarity(arr1, arr2, channel_axis=2, data_range=255)

    return ssim_value