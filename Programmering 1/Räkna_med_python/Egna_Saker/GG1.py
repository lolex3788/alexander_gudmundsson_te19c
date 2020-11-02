
från = 0
till = 100

for i in range(från, till + 1):
   if i>1:
       for g in range(2, i):
           if (i%g)==0:
               break
       else:
           print(i)