import numpy as np
import SolveTriangular as st

def qr_solve(Q, R, b):
    y = Q.T @ b
    x, flag = st.Usolve(R, y)
    if flag != 0:
        return [], flag
    return x, flag