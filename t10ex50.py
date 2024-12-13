"""
Definir una funció elimina_duplicats() que donada una llista ens retorni una nova llista sense elements duplicats.
"""

def llegir_llista():
    l=[]
    a="a"
    while a!=".":
        a=input("Introdueix elements per la llista: ")
        if a!=".":
            l.append(int(a))
    return l

def elimina_duplicats(l):
    s=set(l)
    return list(s)

#Programa principal
l=llegir_llista()
r=elimina_duplicats(l)
print("La llista {} que així {}".format(l,r))