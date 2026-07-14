import numpy as np

from metodi.lagr.plagr import plagr

def InterpL(x, y, xx):
    """
    Funzione che calcola i valori del polinomio interpolante
    di Lagrange in un insieme di punti.

    DATI INPUT:
    x  = vettore contenente i nodi di interpolazione
    y  = vettore contenente i valori della funzione nei nodi
    xx = vettore contenente i punti in cui valutare il polinomio interpolante

    DATI OUTPUT:
    vettore contenente i valori assunti dal polinomio interpolante
    nei punti xx
    """

    # n è il numero di nodi di interpolazione.
    n = x.size

    # m è il numero di punti in cui si vuole valutare il polinomio.
    m = xx.size

     
    L = np.zeros((m, n))

    # Per ogni nodo di interpolazione si costruisce il corrispondente
    # polinomio fondamentale di Lagrange.
    for j in range(n):
        p = plagr(x, j) # TODO
        L[:, j] = np.polyval(p, xx) # TODO: Salvi i valori dei punti xx nel polinomio p nella colonna j di L

    pol = L @ y # TODO
    return pol