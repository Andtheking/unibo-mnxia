import numpy as np
import SolveTriangular as st

def cholesky_solve(L, b):
    y, flag = st.Lsolve(L, b)
    if flag != 0:
        return [], flag
    x, flag = st.Usolve(L.T, y)
    return x, flag