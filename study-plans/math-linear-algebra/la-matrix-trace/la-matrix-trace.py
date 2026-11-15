import numpy as np

def matrix_trace(A: list) -> float:
    """
    Returns the trace as a Python float.
    """
    n = len(A)

    trace = sum(A[i][i] for i in range(n))

    return float(trace)