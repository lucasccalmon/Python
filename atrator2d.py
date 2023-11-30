import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

r= 3.99
x= np.random.random()
X= [x]

for i in range(1000) :
    x = r*x*(1 - x)
    X.append(x)

#PLOTA GRAFICO
plt.figure(1)
plt.plot(X)
plt.show()

A = X[:len(X)-1]
B = X[1:len(X)]

#plota 2d
plt.figure(2)
plt.plot(A, B, '.', c='blue')
plt.show()



