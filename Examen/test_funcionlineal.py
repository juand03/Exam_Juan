import math
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
A=np.array([[2,4,6],[3,8,5],[-1,1,2]])
b=np.array([22,27,2])
sol=np.linalg.solve(A,b)
#y=np.zeros(len(x))
#for i in range (len(x)):
    #y[i]=math.sin(x[i])
#plt.plot(x,"b--")
print(sol)
x,y=np.linspace(0,10,10),np.linspace(0,10,10),
X,Y=np.meshgrid(x,y)
Z1=(22-2*X-4*Y)/6
Z2=(27-3*X-8*Y)/5
Z3=(2+X-Y)/2
fig=plt.figure()
ax=fig.add_subplot(111,projection="3d")
ax.plot_surface(X,Y,Z1,alpha=0.5, cmap=cm.Accent,rstride=100,cstride=100)

plt.show()