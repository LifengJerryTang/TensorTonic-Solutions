import numpy as np

def majority_classifier(y_train: list, X_test: list) -> np.ndarray:
    """
    Returns a one-dimensional NumPy array.
    """
    # Write code here
    values, counts = np.unique(y_train, return_counts=True)
    most_frequent = values[counts == counts.max()].max()
    n = len(X_test)

    return np.full(n, most_frequent)