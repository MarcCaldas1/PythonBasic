x= int(input("Introdueix la quantitat a sol·licitar: "))
i= float(input("Introdueix un interès: "))
a= int(input("Introdueix nombre d'anys: "))
c= x *(1+i/100)**a
print("Amb el capital {} amb un interès {} per {} anys, al final es convertirà en un valor de {}".format(x,i,a,c))
