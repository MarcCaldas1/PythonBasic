"""
Definir una funció esta_ordenada() que donada una llista de números, 
ens indiqui si està ordenada en ordre ascendent, descendent o no està ordenada. 
Prova-la. Ex. esta_ordenada([3,2,1]) retorni està ordenada de forma descendent. 
esta_ordenada([4,5,6]) retorni està ordenada de forma ascendent i 
qualsevol altres cas retorni no està ordenada.
"""
def llegir_llista():
    # Prec: llista buida i llegeix del teclat paraules
    # Post: Retorna la llista llegida de paraules, la llista acaba en trobar un punt
    l=[]
    a="a"
    while a!=".":
        a=input("Introdueix una paraula: ")
        if a!=".":
            l.append(str(a))
    return l

def esta_ordenada(l):
    ld=l.sort(reverse=True)
    la=l.sort(reverse=False)
    if l.sort(reverse=True)==ld:
        print("La llista està ordenada de forma descendent")
    elif l.sort(reverse=False)==la:
        print("La llista està ordenada de forma ascendent")
    else:
        print("La llista no està ordenada")


#Programa principal
l=llegir_llista()
esta_ordenada(l)