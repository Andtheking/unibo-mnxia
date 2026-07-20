import numpy as np

def falsi(fname, a, b, maxit, tolx,tolf):
 """
 Implementa il metodo di falsa posizione per il calcolo degli zeri di un'equazione non lineare.

 Parametri:
  f: La funzione da cui si vuole calcolare lo zero.
  a: L'estremo sinistro dell'intervallo di ricerca.
  b: L'estremo destro dell'intervallo di ricerca.
  tol: La tolleranza di errore.

 Restituisce:
  Lo zero approssimato della funzione, il numero di iterazioni e la lista di valori intermedi.
 """
 fa=fname(a)
 fb=fname(b)
 if np.sign(fa) * np.sign(fb) >= 0: # TODO: Teorema del Segno
     print("Non è possibile applicare il metodo di falsa posizione \n")
     return None, None,None

 it = 0
 v_xk = []
 
 fxk=tolf+1

 errore=tolx+1
 xk=None
 xprec=a
 
 while abs(fxk) > tolf and errore > tolx and it < maxit: # TODO: tolleranza y and tolleranza x and iterazione
        xk = a - fa * (b - a) / (fb - fa) # TODO: FORMULA RETTE SECANTI 
         
        fxk=fname(xk)
        if np.abs(fxk)<tolf:
          return xk, it, np.array(v_xk)
    
        if np.sign(fxk) * np.sign(fa) < 0: # TODO: la radice si trova nell'intervallo [a, xk].
          b = xk
          fb = fxk
        elif np.sign(fxk) * np.sign(fb) < 0: # TODO: la radice si trova nell'intervallo [xk, b].
          a = xk
          fa = fxk
    
        if xk!=0:
             errore = abs(xk - xprec) / abs(xk) # TODO: errore relativo
        else:
             errore = abs(xk - xprec) # TODO: errore assoluto 
        
        xprec=xk
        v_xk.append(xk)
        it += 1
 return xk, it, np.array(v_xk)