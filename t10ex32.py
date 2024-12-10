def llegir_llista():
    l=[]
    a="a"
    while a!=".":
        a=input("Introdueix un número: ")
        if a!=".":
            l.append(int(a))
    return l

def noms_que_començen_per(l,c):
    m=[]
    for e in l:
        if e[0]==c:
            m.append(e)



#Programa principal
l=llegir_llista()
c=input("Introdueix un caràcter: ")
