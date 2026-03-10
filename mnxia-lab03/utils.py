import numpy as np

def isView(arr: np.ndarray):
    return arr.base is not None
