import numpy as np
import matplotlib.pyplot as plt

def DrawGeometry(NODES, ELEMS, WB):
  
    fh = plt.figure()
    
    plt.plot(NODES[:,1], np.zeros( (np.shape(NODES)[0], 1) ), '-b|' )

    number_of_node = np.shape(NODES)[0]
        
    for ii in np.arange(0,number_of_node):
        
        ind = NODES[ii,0]
        x = NODES[ii,1]
        plt.text(x, 0.01, str( int(ind) ), c="b")
        plt.text(x, -0.01, str(x))
     
    number_of_element = np.shape(ELEMS)[0]
    for ii in np.arange(0,number_of_element):

        wp = ELEMS[ii,1]
        wk = ELEMS[ii,2]

        x = (NODES[wp-1,1] + NODES[wk-1,1] ) / 2  

        plt.text(x, 0.01, str(ii+1), c="r")

    plt.show()
    return fh