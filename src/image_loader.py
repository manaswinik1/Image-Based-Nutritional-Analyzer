"""Image loading utilities for the Image-Based Nutritional Analyzer."""

from typing import Tuple
import cv2
import numpy as np



def load_image(path: str, size: Tuple[int, int] = (640, 640)) -> np.ndarray:
    """Load an image from disk and prepare it for model input.

    Parameters
    ----------
    path : str
        File path to the image.
    size : Tuple[int, int], optional
        Desired output size (width, height), by default (640, 640).

    Returns
    -------
    np.ndarray
        The loaded and resized image in RGB format.
    """
    image = cv2.imread(path)
    if image is None:
        raise FileNotFoundError(f"Image not found at path: {path}")

    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    image = cv2.resize(image, size)
    return image

