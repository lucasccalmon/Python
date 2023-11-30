import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

def atrator(X):
    A = X[:len(X)-2]
    B = X[1:len(X)-1]
    C = X[2:]
    #Plota atrator em 3D
    fig = plt.figure(2)
    ax = fig.add_subplot(111, projection='3d')
    ax.plot(A, B, C , '.', c='red')
    plt.show()

#inicio script
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
atrator(X)

