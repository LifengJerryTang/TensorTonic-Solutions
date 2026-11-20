import numpy as np

def sample_var_std(x: list) -> dict:
    """
    Returns a dictionary with variance and standard_deviation.
    """
    # Write code here
    data = np.array(x)
    sample_var = np.var(data, ddof=1) 
    sample_std = np.std(data, ddof=1) 

    return {"variance": float(sample_var), "standard_deviation": float(sample_std)}