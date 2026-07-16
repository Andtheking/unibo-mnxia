import numpy as np
import SolveTriangular as st
import scipy.linalg as spl

def LUsolve(P, L, U, b):
    Pb = P @ b
    y, flag = st.Lsolve(L, Pb)
    if flag != 0:
        return [], flag
    x, flag = st.Usolve(U, y)
    return x, flag

# Chiamare la fatt. di gauss dati A e b
if __name__ == "__main__":
    A = None # per non dare errore 
    b = None # per non dare errore
    Pt, L, U = spl.lu(A)
    P = Pt.T.copy()
    x, flag = LUsolve(P, L, U, b)