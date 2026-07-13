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
 if np.sign(fa) * np.sign(fb) >= 0: #to do
     print("Non è possibile applicare il metodo di falsa posizione \n")
     return None, None,None

 it = 0
 v_xk = []
 
 fxk=tolf+1

 errore=tolx+1
 xk=None
 xprec=a
 
 while abs(fxk) > tolf and errore > tolx and it < maxit: #to do 
        xk = a - fa * (b - a) / (fb - fa) # FORMULA RETTE SECANTI #to do 
         
        fxk=fname(xk)
        if np.abs(fxk)<tolf:
          return xk, it, np.array(v_xk)
    
        if np.sign(fxk) * np.sign(fa) < 0: #  #la radice si trova nell'intervallo [a, xk].
          b = xk
          fb=fxk
        elif np.sign(fxk) * np.sign(fb) < 0: #to do   #la radice si trova nell'intervallo [xk, b].
          a = xk
          fa=fxk
    
        if xk!=0:
             errore = abs(xk - xprec) / abs(xk) # errore relativo $todo
        else:
             errore = abs(xk - xprec) # errore assoluto #to do
        
        xprec=xk
        v_xk.append(xk)
        it += 1
 return xk, it, np.array(v_xk)