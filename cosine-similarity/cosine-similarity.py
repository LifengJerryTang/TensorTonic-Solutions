import math as math

def cosine_similarity(a: list, b: list) -> float:
    """
    Returns the cosine similarity as a Python float.
    """

    dot = dot_product(a, b)
    a_norm = l2_norm(a)
    b_norm = l2_norm(b)

    denominator = (a_norm * b_norm)

    if denominator == 0:
        return 0.0

    return dot / (a_norm * b_norm)

def dot_product(a: list, b: list) -> float:
    return float(sum(x * y for x, y in zip(a, b)))


def l2_norm(vec: list) -> float:
    return math.sqrt(sum(val ** 2 for val in vec))
    