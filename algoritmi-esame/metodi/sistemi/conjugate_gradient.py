import numpy as np

def conjugate_gradient(A: np.matrix, b: np.typing.ArrayLike, x0, itmax,tol):
    # Metodo del gradiente coniugato

    n, m = A.shape  # dimensioni della matrice A
    if n != m:
        print("Matrice non quadrata")
        return [], []  # necessario che A sia quadrata

    # inizializzazione
    x = x0  # punto iniziale
    r = A @ x - b 
    p = -r #to do 
    it = 0             # contatore iterazioni

    nb = np.linalg.norm(b)   # norma di b (non usata qui)
    errore = np.linalg.norm(r) / nb 
    
    vec_sol = []             # lista delle soluzioni
    vec_sol.append(x0.copy())

    vet_r = []               # lista degli errori
    vet_r.append(errore)

    # ciclo del gradiente coniugato
    while errore >= tol and it < itmax: #to do 
        it = it + 1  # incremento iterazioni

        Ap = A @ p # TODO

        # passo ottimo lungo la direzione coniugata p
        alpha = -(r.T @ p) / (p.T @ Ap) # TODO 

        # aggiornamento soluzione
        x = x + alpha * p # TODO 

        
        vec_sol.append(x.copy())  # salva iterata

        # salva (r^T r) vecchio per calcolare gamma
        rtr_old = r.T @ r #to do 

        # aggiornamento residuo
        r = r + alpha * Ap #to do 

        # coefficiente di coniugazione (Fletcher-Reeves)
        gamma = r.T @ r / rtr_old #to do

        # aggiornamento errore
        errore = np.linalg.norm(r)/nb
        vet_r.append(errore)

        # nuova direzione: 
        p = -r + gamma * p # TODO 

    # costruzione matrice delle iterate (ogni riga = una iterazione)
    iterates_array = np.array(vec_sol).squeeze()

    # output
    return x, vet_r, iterates_array, it