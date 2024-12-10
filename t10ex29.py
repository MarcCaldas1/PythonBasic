def bintodec(b):
    aux = b[::-1]
    d = 0
    for i,e in enumerate(b):
        d += int(e)*(2**i)
    return d 


#programa principal
a = input("Introdueix un número en binari (només pot tenir 0 i 1)")
print("El número {}-binari és {}-decimal".format(a,bintodec(a)))