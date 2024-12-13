def llegir_llista():
    l=[]
    a="a"
    while a!=".":
        a=input("Introdueix una paraula: ")
        if a!=".":
            l.append(a)
    return l

def elements_parells(l):
    print(l[::2])

#Programa principal

l= llegir_llista()
elements_parells(l)