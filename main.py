import numpy as np
import matplotlib.pyplot as plt
import scipy.integrate as spint

from GeometryDefinition import *
from GeometryGenerator import *
from DrawGeometry import *
from Marrays import *
from BaseFunctions import *
from Marrays import *
from DrawSolution import *
from Allocation import *

if __name__ == '__main__':
    
    #WEZLY, ELEMENTY, WB = GeometryDefinition()
    #n = np.shape(WEZLY)[0]
    c = 0 
    f = lambda x: 0*x 
    

    x_a =  0 
    x_b =  1
    
    n = 10
    
    WEZLY, ELEMENTY = GeometryGenerator(x_a,x_b,n)
  
    WB    = [{"ind": 1, "typ":'D', "wartosc":1}, 
              {"ind": n, "typ":'D', "wartosc":2}]
    
    
    
    DrawGeometry(WEZLY, ELEMENTY, WB)
    A,b = Allocation(n)
    
    stopien_fun_bazowych = 1
    phi, dphi = BaseFunctions(stopien_fun_bazowych)
    
    liczbaElementow = np.shape(ELEMENTY)[0]
    
    for ee in np.arange(0, liczbaElementow ):
        
        elemRowInd = ee
        elemGlobalInd = ELEMENTY[ee,0]        
        elemWezel1 = ELEMENTY[ee,1]     
        elemWezel2 = ELEMENTY[ee,2]   
        indGlobalneWezlow = np.array([elemWezel1, elemWezel2 ])
    
        x_a = WEZLY[ elemWezel1-1 ,1]
        x_b = WEZLY[ elemWezel2-1 ,1]
    
    
        Ml = np.zeros( [stopien_fun_bazowych+1, stopien_fun_bazowych+1] )
        
        J = (x_b-x_a)/2
        
        m = 0; n = 0 ;
        Ml[m,n] = J * spint.quad( Marrays(dphi[m], dphi[n], c, phi[m],phi[n]), -1, 1)[0]
        
        m = 0; n = 1 ;
        Ml[m,n] = J * spint.quad( Marrays(dphi[m], dphi[n], c, phi[m],phi[n]), -1, 1)[0]
        
        m = 1; n = 0 ;
        Ml[m,n] = J * spint.quad( Marrays(dphi[m], dphi[n], c, phi[m],phi[n]), -1, 1)[0]
        
        m = 1; n = 1 ;
        Ml[m,n] = J * spint.quad( Marrays(dphi[m], dphi[n], c, phi[m],phi[n]), -1, 1)[0]
                
        
        
        A[np.ix_(indGlobalneWezlow-1, indGlobalneWezlow-1  ) ] =  \
            A[np.ix_(indGlobalneWezlow-1, indGlobalneWezlow-1  ) ] + Ml
    
    
        

        
    if WB[0]['typ'] == 'D':
        ind_wezla = WB[0]['ind']
        wart_war_brzeg = WB[0]['wartosc']
        
        iwp = ind_wezla - 1
        
        WZMACNIACZ = 10**14
        
        b[iwp] = A[iwp,iwp]*WZMACNIACZ*wart_war_brzeg
        A[iwp, iwp] = A[iwp,iwp]*WZMACNIACZ
        
        
    if WB[1]['typ'] == 'D':
        ind_wezla = WB[1]['ind']
        wart_war_brzeg = WB[1]['wartosc']
        
        iwp = ind_wezla - 1
        
        WZMACNIACZ = 10**14
        
        b[iwp] = A[iwp,iwp]*WZMACNIACZ*wart_war_brzeg
        A[iwp, iwp] = A[iwp,iwp]*WZMACNIACZ        
       
    
   
    u = np.linalg.solve(A,b)
    
    DrawSolution(WEZLY, u)