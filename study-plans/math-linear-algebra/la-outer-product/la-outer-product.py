import numpy as np

def outer_product(u: list, v: list) -> np.ndarray:
    """
    Returns the float64 outer-product matrix.
    """

    return np.outer(np.array(u).astype(float), np.array(v))
    