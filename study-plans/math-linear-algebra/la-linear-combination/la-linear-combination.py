import numpy as np

def linear_combination(vectors: list, coefficients: list) -> np.ndarray:
    """
    Returns the weighted sum as a float64 vector.
    """

    # only one of the two needs to be an np array!
    return np.column_stack(vectors).astype(float) @ coefficients