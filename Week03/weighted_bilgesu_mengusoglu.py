import random

def weighted_srs(data, n, weights=0, with_replacement=False):
    if weights == 0 and not with_replacement:
        return random.sample(data, n)
    return random.choices(data, weights=weights, k=n)
