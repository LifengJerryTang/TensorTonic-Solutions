from collections import Counter
import numpy as np

def mean_median_mode(x: list) -> dict:
    """
    Returns a dictionary with mean, median, and mode.
    """
    # Write code here
    data = np.array(x)
    mean = np.mean(data)
    median = np.median(data)

    vals, counts = np.unique(data, return_counts=True)
    mode = vals[np.argmax(counts)]

    return {"mean": float(mean), "median": float(median), "mode": float(mode)}