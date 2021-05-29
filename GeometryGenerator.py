import numpy as np

def GeometryGenerator(a,b,n):

    
    no = np.arange(1,n+1)
    x = np.linspace(a,b,n) ;        
    nodes = (np.vstack( (no.T, x.T) )).T 
    
    no = np.arange(1,n)
    C1 = np.arange(1,n)
    C2 = np.arange(2,n+1)
    elements = (np.block( [[no], [C1], [C2] ] ) ).T
                    
    return nodes, elements