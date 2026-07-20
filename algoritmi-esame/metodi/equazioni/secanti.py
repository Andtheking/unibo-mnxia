import numpy as np

def secanti(fname,xm1,x0,tolx,tolf,nmax):
    #Metodo delle secanti per il calcolo degli zeri di un'equazione non lineare.
    #xm1, x0 due iterati iniziali
    
    v_xk=[]
    
    it=0
    errorex=1+tolx
    erroref=1+tolf
    xkm1=xm1
    xk=x0
    xk1=None #Inizializzare xk1 fa sì che se non si entra nel while la funzionenon dà errore, dovendo restituire xk1
    
    while errorex >= tolx and erroref >= tolf and it < nmax: # TODO: Errorex Errorey Iterazioni
        fxkm1=fname(xkm1)
        fxk=fname(xk)
        c_ang_k= (fxk - fxkm1) / (xk - xkm1) # TODO: coeff. angolare
        if np.abs(c_ang_k) <= np.spacing(1): # TODO: coeff. troppo piccolo 
            print("Coefficiente angolare secanti troppo piccolo")
            return None, None, None
            
        d = fxk / c_ang_k # TODO: spostamento
        
        #xk1 è l'ascissa del punto di intersezione tra la retta che passa due iterati precedenti e l'asse x
        xk1 = xk - d # TODO: Nuova x spostata
        
        fxk1=fname(xk1)
        v_xk.append(xk1)
        #Criteri di arresto
        if xk1!=0:
            errorex=abs(d)/abs(xk1)
        else:
            errorex=abs(d)
            
        erroref=np.abs(fxk1)
        #Aggiornamento di xkm1 ed xk
        xkm1 = xk
        xk = xk1
        
        it=it+1
        
    
    if it==nmax:
        print('Secanti: raggiunto massimo numero di iterazioni \n')
    
    return xk1,it,np.array(v_xk)