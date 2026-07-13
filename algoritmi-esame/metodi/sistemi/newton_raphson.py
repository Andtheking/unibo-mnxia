import numpy as np

def newton_raphson(initial_guess, F_numerical, J_numerical, tolX, tolF, max_iterations):
    # Converte la stima iniziale in un array NumPy di float
    X = np.array(initial_guess, dtype=float)

    # Contatore delle iterazioni
    it = 0

    # Inizializzo gli errori con valori maggiori delle tolleranze
    # così il ciclo while parte sicuramente
    erroreF = 1 + tolF
    erroreX = 1 + tolX

    # Lista che conterrà la storia dell'errore relativo sugli iterati
    errore = []

     
    while erroreF >= tolF and erroreX >= tolX: #to do 
        # Calcolo della matrice Jacobiana nel punto corrente X
        jx = np.array(J_numerical(X[0], X[1]), dtype=float) # TODO: Jacobiana  

        if np.linalg.matrix_rank(jx) < jx.shape[0]: #to do 
            print("La matrice Jacobiana calcolata nell'iterato corrente non è a rango massimo")
            return None, None, None

        # Calcolo del valore della funzione F nel punto corrente
        fx = np.array(F_numerical(X[0], X[1]), dtype=float).squeeze() # to do

        
        s = np.linalg.solve(jx, -fx) #to do 

        # Aggiorno l'iterato
        Xnew = X + s #to do 

        # Calcolo dell'errore relativo tra iterati successivi
        # usando la norma 1
        normaXnew = np.linalg.norm(Xnew, 1)
        if normaXnew != 0:
            erroreX = np.linalg.norm(s, 1) / normaXnew #TODO
        else:
            erroreX = np.linalg.norm(s, 1) #TODO

        # Salvo l'errore relativo per analisi successive
        errore.append(erroreX)

        # Calcolo di F nel nuovo punto
        fxnew = np.array(F_numerical(Xnew[0], Xnew[1]), dtype=float).squeeze() #TODO
        erroreF = np.linalg.norm(fxnew, 1)

        # Aggiorno l'iterato corrente
        X = Xnew
        it = it + 1

    # Restituisce:
    # - l'approssimazione della soluzione
    # - il numero di iterazioni eseguite
    # - la lista degli errori relativi sugli iterati
    return X, it, errore