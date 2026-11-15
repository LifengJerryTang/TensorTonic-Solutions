import numpy as np

def matrix_rank(A: list) -> int:
    """
    Returns the numerical rank as a Python integer.
    """

    return int(np.linalg.matrix_rank(A))