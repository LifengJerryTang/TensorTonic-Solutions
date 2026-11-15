import numpy as np

def matrix_vector_multiply(A: list, x: list) -> np.ndarray:
    """
    Returns the matrix-vector product as a float64 array.
    """

    return np.array(A).astype(float) @ x