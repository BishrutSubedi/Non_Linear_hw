import scipy.integrate as integrate
from scipy.integrate import odeint
#import matplotlib.pyplot as plt 
from mpl_toolkits.mplot3d import Axes3D
import numpy as np 
from pylab import * # for plotting commands

def lorenz_fn(A,t):
    x,y,z = A
    s = 10 #10
    r = 20 #28
    b = 8/5 #8/3
    result = np.array([ (-s * ( x - y )), (r * x - y - x * z) , (- b * z + x * y) ])    
    #result = np.array([x(2) , (-a * ((x(1)**2 -1) * x(2)) - x(1) )])
    return result

time = np.linspace(0,10,1500)

x,y,z = integrate.odeint(lorenz_fn,[0.5, 0.5 ,0.5],time).T

'''
figure()
plot(time,x)
plot(time,y)
plot(time,z)
#plot(x(1),x(2))
xlabel('x_1')
ylabel('x_2')
show()
'''

#  PLOTTING IN 3D
mpl.rcParams['legend.fontsize'] = 10
fig = plt.figure()
ax = fig.gca(projection='3d')
ax.plot(x, y, z, label='parametric curve')
ax.legend()
plt.show()

'''
fig = plt.figure()
ax = fig.gca(projection='3d')
surf = ax.plot_trisurf(x, y, z, linewidth=0, antialiased=False)
plt.show()
'''
