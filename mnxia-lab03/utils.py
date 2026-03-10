import numpy as np

def isView(arr: np.ndarray):
    return arr.base is not None

def printIsView(arr: np.ndarray):
    print("View" if isView(arr) else "Copy")