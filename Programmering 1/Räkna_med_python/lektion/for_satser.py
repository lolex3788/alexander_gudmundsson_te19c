
import matplotlib.pyplot as plt 

a_vals = []


for x in range(1,1000):
    a = round(5*(2+4/x),2)

    a_vals.append(a) # vi spapar värden på a i listan



print(a_vals)


plt.plot(a_vals)
plt.show()