import numpy as np

def hadamard_product(A: list, B: list) -> np.ndarray:
    """
    Returns the element-wise product as a float64 array.
    """

    return np.array(A).astype(float) * B