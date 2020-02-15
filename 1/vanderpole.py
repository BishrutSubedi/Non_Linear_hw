import scipy.integrate as integrate
from scipy.integrate import odeint
#import matplotlib.pyplot as plt 
import numpy as np 
from pylab import * # for plotting commands

def vanderpole_fn(A,t):
    x_1,x_2 = A
    #x= A
    a=0.9
    result = np.array([x_2, (-a * ((x_1**2 -1) * x_2) - x_1 )])    
    #result = np.array([x(2) , (-a * ((x(1)**2 -1) * x(2)) - x(1) )])
    return result

time = np.linspace(0,30,150)

x_1,x_2 = integrate.odeint(vanderpole_fn,[0.1 ,0.1],time).T
#x = integrate.odeint(vanderpole_fn,[0.1 ,0.1],time).T

figure()
plot(x_1,x_2)
#plot(x(1),x(2))
xlabel('x_1')
ylabel('x_2')
show()