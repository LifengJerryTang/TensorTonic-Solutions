import numpy as np

def gram_schmidt(vectors: list) -> np.ndarray:
    """
    Returns a float64 array whose rows form the ordered orthonormal basis.
    """
    #1 Start with an initial vector
    results = []
    n = len(vectors)

    for i in range(n):
        curr_vec = np.array(vectors[i])
        curr_res = curr_vec - projection(curr_vec, results)
        curr_res = curr_res / np.linalg.norm(curr_res)
        results.append(curr_res)

    return np.array(results)


def projection(target_vec: np.ndarray, space_vec: list[np.ndarray]) -> np.ndarray:
        
    result = np.zeros(target_vec.shape[0])
    
    if len(space_vec) == 0:
        return result
        
    for vec in space_vec:
        result += (np.dot(target_vec, vec) / (np.linalg.norm(vec) ** 2)) * vec

    return result



    

    