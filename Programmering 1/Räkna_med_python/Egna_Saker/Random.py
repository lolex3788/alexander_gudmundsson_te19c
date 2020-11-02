import random as rnd

#N = rnd.randint(1,10)

#print(N)


#for N in range (1001):
#    N = rnd.randint(1,1000)
#    print(N)
#    if N == 1000:
#        print("GG")
#        break


N = rnd.randint(1, 1000)
M = 0
X = 0
Xupp = 1000
Xner = 1

while M == 0:
    X = rnd.randint(Xner,Xupp)
    if X == N:
        print("Talet var", N)
        break
    elif X > N:
        Xupp = X
        print(X)
    elif X < N:
        Xner = X
        print(X)












