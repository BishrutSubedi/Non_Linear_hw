import scipy.integrate as integrate
from scipy.integrate import odeint
#import matplotlib.pyplot as plt 
import numpy as np 
from pylab import * # for plotting commands

def voltera_fn(A,t):
    x_1,x_2 = A
    result = np.array( [ (-x_1 + x_1 * x_2 ), (x_2 - x_1 * x_2 )] )    
    return result

time = np.linspace(0,10,150)

X1 = np.linspace(-2,2,40)
X2 = X1

for i in X1:
    for j in X2:
        x_1,x_2 = integrate.odeint(voltera_fn,[i , j],time).T

#have to fix the iteration and plot to iteratively plot and hold all
plt.plot(x_1,x_2)
plt.show()
        
