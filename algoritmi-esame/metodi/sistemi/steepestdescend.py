import numpy as np

def steepestdescent(A: np.matrix, b: np.typing.ArrayLike, x0, itmax, tol):
    # A = matrice del sistema
    # b = termine noto
    # x0 = punto iniziale
    # itmax = numero massimo di iterazioni
    # tol = tolleranza per il criterio di arresto

    n, m = A.shape  # dimensioni della matrice A
    if n != m:
        print("Matrice non quadrata")
        return [], []  # il metodo richiede una matrice quadrata

    # inizializzazione
    x = x0 # soluzione iniziale

    r: np.matrix = A @ x - b # TODO: Residio iniziale, la soluzione del sistema sarebbe A@x = b, portando b a sinistra abbiamo il residuo
    p = -r # TODO: Direzione del movimento, opposto al residuo
    it = 0 # contatore iterazioni

    nb = np.linalg.norm(b)
    errore = np.linalg.norm(r) / nb # TODO: Errore relativo iniziale

    vec_sol = []            # lista delle soluzioni iterate
    vec_sol.append(x.copy())

    vet_r = []              # lista degli errori
    vet_r.append(errore)

    # ciclo del metodo del gradiente
    while errore >= tol and it < itmax:
        it = it + 1  # incremento iterazioni

        Ap= A @ p # TODO: A per p, spostiamo la soluzione verso la direzione scelta prima
        # calcolo del passo ottimo (minimizza lungo la direzione p)
        alpha = -(r.T @ p) / (p.T @ Ap) #to do

        # aggiornamento soluzione
        x = x + alpha * p #to do  

        # salva iterata
        vec_sol.append(x.copy())

        # aggiornamento residuo (più efficiente che ricalcolare A@x - b)
        r = r + alpha * Ap # TODO: Ricalcolo residuo  

        # aggiornamento errore
        errore = np.linalg.norm(r) / nb # TODO: Errore nuovo
        vet_r.append(errore)

        # nuova direzione  
        p = -r #to do  

    # costruzione matrice delle iterate (ogni riga = una iterazione)
    iterates_array = np.array(vec_sol)

    # output
    return x, vet_r, iterates_array, it