import matplotlib.pyplot as plt 

Sträcka = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
Tid = [1.83, 2.87, 3.78, 4.65, 5.5, 6.32, 7.14, 7.96, 8.79, 9.69]
V = []


for i in range(1, len(Sträcka)):
    V.append((Sträcka[i]-Sträcka[i-1])/(Tid[i]-Tid[i-1]))


print(len(V))
print(len(Tid))

plt.plot(V)
plt.show()