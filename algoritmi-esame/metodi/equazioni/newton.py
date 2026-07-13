import numpy as np

def newton(fname,fpname,x0,tolx,tolf,nmax):
    """
    Calcola la pendezza esatta della curva nel punto in cui si trova
    """


    # fpname è la lambda function contenente la derivata prima di fname
    v_xk=[]
    xk=x0
    
    it=0
    xk1=None
    errorex=1+tolx
    erroref=1+tolf
    
    while errorex >= tolx and erroref >= tolf and it < nmax: # TODO: Tolleranze errori e  
        
        fxk=fname(xk)
        fpxk=fpname(xk)
        if abs(fpxk) <= np.spacing(1): #to do 
            print("Newton: La derivata prima si annulla ")
            return None,None,None

        d = fxk / fpxk # TODO: Spostamento
                
        '''
        #xk1= ascissa del punto di intersezione tra  la retta che passa per il punto
        (xk,f(xk)) e ha pendenza uguale a quella della tangente nel punto  e l'asse x
        '''
        xk1 = xk - d # TODO: nuovo punto
        
        fxk1 = fname(xk1)
        
        if xk1 != 0:
            errorex = abs(d) / abs(xk1) # TODO: Errore relativo
        else:
            errorex = abs(d) #to do 
        
        erroref = np.abs(fxk1)

        v_xk.append(xk1)

        xk=xk1
        it=it+1
        
        if it==nmax:
            print('Newton : raggiunto massimo numero di iterazioni \n')

    return xk1,it,np.array(v_xk)