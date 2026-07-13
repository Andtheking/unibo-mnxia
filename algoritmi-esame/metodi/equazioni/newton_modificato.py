import numpy as np

def newton_modificato(fname,fpname,m,x0,tolx,tolf,nmax):
    # Il codice implementa il metodo di Newton modificato per radici multiple.
    # m è la molteplicità della radice
    # fpname è la lambda function contenente la derivata prima di fname
    
    v_xk = []
    xk = x0
    
    xk1 = None
    it = 0
    errorex=1+tolx
    erroref=1+tolf
    while errorex >= tolx and erroref >= tolf and it < nmax:
        
        fxk=fname(xk)
        fpxk=fpname(xk)
        if abs(fpxk) <= np.spacing(1): #todo   #Se la derivata prima e' pià piccola della precisione di macchina stop
            print("Newton Modificato: La derivata prima si annulla ")
            return None,None,None
    
        d = fxk / fpxk # to do
                
        '''
        #xk1= ascissa del punto di intersezione tra  la retta che passa per il punto
        (xk,f(xk)) e ha pendenza uguale a quella della tangente nel punto  e l'asse x
        ''' 
        xk1 = xk - m * d # TODO:  Rispetto al Newton normale qui si aggiunge il parametro m
        fxk1=fname(xk1)
        if xk1!=0:
            errorex = abs(d) / abs(xk1) # to do 
        else:
            errorex = abs(d)
        
        erroref=np.abs(fxk1)
        v_xk.append(xk1)
        xk=xk1
        it=it+1
        
        
    if it==nmax:
        print('Newton Modificato : raggiunto massimo numero di iterazioni \n')
        
    return xk1,it,np.array(v_xk)