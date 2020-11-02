import matplotlib.pyplot as plt 
import random as rnd

for i in range(1, 1000):
    X = rnd.uniform(-1, 1)
    Y = rnd.uniform(-1, 1)
    plt.plot(X, Y, '*b')


plt.show()