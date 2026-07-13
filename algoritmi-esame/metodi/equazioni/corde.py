import numpy as np

def corde(fname,a,b,coeff_ang,x0,tolx,tolf,nmax):
    """
    Algoritmo veloce ma potrebbe non trovare mai lo zero.
    """
    # coeff_ang è il coefficiente angolare della retta che rimane fisso per tutte le iterazioni
    v_xk=[]
    xk=x0
    
    it=0
    errorex=1+tolx
    erroref=1+tolf
    xk1=None

    if abs(coeff_ang) <= np.spacing(1):
        print("Metodo delle corde: coefficiente angolare nullo")
        return None, None, None
                    
    while erroref >= tolf and errorex >= tolx and it < nmax: #to do
        
        fxk=fname(xk)

    
        d = fxk / coeff_ang
        '''
        #xk= ascissa del punto di intersezione tra  la retta che passa per il punto
        (xi,f(xi)) e ha pendenza uguale a coeff_ang  e l'asse x
        '''
        xk1= xk - d
        
        
        fxk1=fname(xk1)
        if xk1!=0:
            errorex = abs(d) / abs(xk1) # todo
        else:
            errorex = abs(d) # to do 
        
        erroref=np.abs(fxk1)
        
        xk=xk1
        it=it+1
        v_xk.append(xk1)
        
    if it==nmax:
        print('Corde : raggiunto massimo numero di iterazioni \n')
        
    
    return xk1,it,np.array(v_xk)