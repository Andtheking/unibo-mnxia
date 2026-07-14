import numpy as np

def plagr(xnodi: np.matrix, j):
    """
    Restituisce i coefficienti del j-esimo polinomio fondamentale
    di Lagrange associato ai nodi contenuti nel vettore xnodi.
    """
    
    xzeri = np.zeros_like(xnodi)

    # n rappresenta il numero di nodi di interpolazione.
    n = xnodi.size
    
    if j == 0:
        xzeri = xnodi[1:n] # TODO
    else:
        xzeri = np.append(xnodi[0:j], xnodi[j+1: n]) # TODO

    num = np.poly(xzeri) # TODO
    den = np.polyval(num, xnodi[j]) # TODO

    p = num / den # TODO

    # La funzione restituisce i coefficienti del polinomio L_j(x).
    return p