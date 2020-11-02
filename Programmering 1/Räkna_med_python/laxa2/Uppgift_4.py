vinkel = float(input("Skriv din vinkel här."))

if vinkel > -1 and vinkel < 90:
    print ("Det är en spetsig vinkel.")

elif vinkel == 90:
    print ("Det är en rät vinkel.")

elif vinkel > 90 and vinkel < 180:
    print ("Det är en trubbig vinkel.")

elif vinkel == 180:
    print ("Det är en rak vinkel.")

elif vinkel > 180 and vinkel < 360:
    print ("Det är en konvex vinkel.")

elif vinkel >= 360:
    print ("Det är en hel vinkel.")