# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Names:         Patrick Murphy
#                Steven Sooudi
#                Hayden Futch
# Section:      ENGR 102 569
# Assignment:   12 Team LAB
# Date:         11/12/24
import matplotlib.pyplot as plt
import matplotlib.lines as ln
from math import*
import numpy as np

x = np.linspace(-2.0, 2.0, 100)
plt.plot(x,(1/24)*x**2 ,label='f=6', lw = 6.0)
plt.plot(x,(1/8)*x**2, "r-", label='f=2', lw = 2.0)
plt.axis([-2.1,2.1,0,0.51])
plt.xlabel('x')
plt.ylabel('y')
plt.title('Parabola plots with varying focal length')
plt.legend()
plt.show()

x = np.linspace(-4, 4, 25)
plt.plot(x,2*x**3+3*x**2-11*x-6, 'y*', label='Cubic Polynomial')
plt.axis([-4,4,-50,125])
plt.title('Plot of cubic polynomial')
plt.show()

#x = np.linspace(-2*pi,2*pi,100)
#plt.title('plot of cos(x) and sin(x)')
#ax1 = plt.subplot(211)
#plt.plot(x,np.cos(x),label='cosx')
#plt.tick_params('x', labelbottom=False)
#plt.xlabel('x')
#plt.ylabel('y=cos(x)')
#plt.legend()

#


#ax2 = plt.subplot(212, sharex=ax1, sharey = ax1)
#plt.plot(x,np.sin(x),label='sinx')
#plt.tick_params('y', labelbottom=False)
#plt.ylabel('y=sin(x)')
#plt.legend()
#plt.subplots_adjust(top=0.92, bottom=0.08, left=0.10, right=0.95, hspace=0.25,wspace=0.35)
#plt.show()

t = np.arange(-2*pi, 2*pi, 0.01)
s1 = np.cos(t)
s3 = np.sin(t)

x1 = plt.subplot(211)
plt.title("Plot of cos(x) and sin(x)")
plt.plot(t, s1,"r", label = 'cosx')
plt.tick_params('x', labelsize=0)
plt.ylabel('y=cos(x)')
plt.grid(True)
plt.legend()

# share x only
#x2 = plt.subplot(312, sharex=x1)
#plt.plot(t, s2)
# make these tick labels invisible
#plt.tick_params('x', labelbottom=False)

# share x and y
x3 = plt.subplot(212, sharex=x1, sharey=x1)
plt.plot(t, s3, label="sinx")
plt.xlim(-2*pi, 2*pi)
plt.ylabel('y=sin(x)')
plt.legend()
plt.grid(True)
plt.xlabel("x")
plt.show()