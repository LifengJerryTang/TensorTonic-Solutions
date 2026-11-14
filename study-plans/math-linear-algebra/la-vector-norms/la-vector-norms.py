import numpy as np
import math as m

def vector_norms(v: list) -> np.ndarray:
    """
    Returns a float64 array containing the L1, L2, and infinity norms.
    """
    l1_norm = float(sum(abs(num) for num in v))
    l2_norm = float(m.sqrt(sum(num ** 2 for num in v)))
    max_norm = float(max(abs(num) for num in v))

    return np.array([l1_norm, l2_norm, max_norm])