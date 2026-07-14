import numpy as np
import scipy.linalg as spl

from SolveTriangular import Usolve

def qrLS(A, b):
    n = A.shape[1] # colonne
    Q, R = spl.qr(A) # TODO: A = Q R, con Q matrice ortogonale e R matrice triangolo superiore

    # Si calcola la fattorizzazione QR della matrice A.

    h = Q.T @ b 
    
    x, flag = Usolve(R[0:n, :], h[0:n]) # TODO
    
    residuo = np.linalg.norm(h[n:]) ** 2 # TODO

    # La funzione restituisce i coefficienti della soluzione x
    # e il valore del residuo quadratico.
    return x, residuo