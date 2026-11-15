import numpy as np

def vector_projection(u: list, v: list) -> np.ndarray:
    """
    Returns the float64 projection of u onto v.
    """

    return float(np.dot(u, v) / np.dot(v, v)) * np.array(v)