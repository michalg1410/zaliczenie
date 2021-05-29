import numpy as np

def BaseFunctions(n):
  
    if n==0:
        f  = (lambda x: 1 + 0*x )
        df = (lambda x: 0*x )
        
    elif n == 1:
        
        f = (lambda x: -0.5*x + 0.5, lambda x: 0.5*x+0.5 )
        df= (lambda x: -0.5 + 0*x ,   lambda x: 0.5  + 0*x )
        

        
    else: 
        raise Exception("Error")

    return f,df