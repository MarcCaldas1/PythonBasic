"""Definir una funció hi_ha_duplicats() que ens indiqui si una llista donada té qualque element duplicat o no, 
no s’ha de modificar la llista donada. Prova-la.
"""

def llegir_llista():
    l=[]
    a="a"
    while a!=".":
        a=input("Introdueix elements per la llista: ")
        if a!=".":
            l.append(a)
    return l

def hi_ha_duplicats(l):
    duplicats= [e for e in set(l) if l.count(e)>1]
    return duplicats

#Programa principal
if __name__ == "__main__":
    llista=llegir_llista()
    duplicats=hi_ha_duplicats(llista)
    if duplicats:
        print("Hi ha elements duplicats: {}".format(', '.join(duplicats)))
