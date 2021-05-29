import numpy as np
import matplotlib.pyplot as plt
from DrawGeometry import *

def DrawSolution(NODES, u):
   
    x = NODES[:,1]
    
    plt.plot(x, u, 'm*')