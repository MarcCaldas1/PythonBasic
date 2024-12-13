"""Definir una funció hi_ha_duplicats() que ens indiqui si una llista donada té qualque element duplicat o no, 
no s'ha de modificar la llista donada. Prova-la.
"""

def llegir_llista():
    l=[]
    a="a"
    while a!=".":
        a=input("Introdueix elements per la llista: ")
        if a!=".":
            l.append(int(a))
    return l

def hi_ha_duplicats(l):
    s=set(l)
    if len(l)==len(s):
        print("No hi ha duplicats")
    else:
        print("Hi ha duplicats")

#Programa principal
l=llegir_llista()
hi_ha_duplicats(l)
