"""def llegir_llista():
    l=[]
    a="a"
    while a!=".":
        a=input("Introdueix un nom: ")
        if a!=".":
            l.append(a)
    return l

def noms_que_començen_per(l,c):
    m=[]
    for e in l:
        if e[-1]==c.upper() or e[-1]==c.lower():
            m.append(e)
    print("Els elements de la llista {} que acaben per {} són {}".format(l,c,m))



#Programa principal
l=llegir_llista()
c=input("Introdueix un caràcter: ")
noms_que_començen_per(l,c)"""





"""
def llegir_llista():
    l=[]
    a="a"
    while a!=".":
        a=input("Introdueix un nom: ")
        if a!=".":
            l.append(a)
    return l

def noms_que_comencen_per(l,c):
    m=[]
    for e in l:
        senar = len(e)%2==1
        if senar:
            aux= len(e)//2+1
            if e[aux] == c.upper() or e[aux]==c.lower():
                m.append(e)
        else:
            aux=len(e)//2 -1
            if e[aux] == c.upper() or e[aux]==c.lower() or e[aux+1]==c.upper() or e[aux+1]==c.lower():
                m.append(e)
    print("Els elements de la llista {} que comencen per {} són {}".format(l,c,m))

#Programa principal
l=llegir_llista()
c=input("Introdueix un caràcter: ")
noms_que_comencen_per(l,c)
"""


def llegir_llista():
    l=[]
    a="a"
    while a!=".":
        a=input("Introdueix un nom: ")
        if a!=".":
            l.append((a))
    return l

def retorna_conjunt(l):
    #Prec: Donada una llista de paraules
    #Post: Retorna un conjunt de caràcters del centre (si senar, centres si parell) de cada paraula
    m=[]
    for e in l:
        senar = len(e)%2==1
        if senar:
            m.append(e[len(2)//2])
        else:
            m.append(e[len(2)//2])
            m.append(e[len(2)//2+1])
    s=set(m)
    return s

def llistes_comparades(l,s):
    #Prec: DOnada una llista de paraules i un conjunt de lletres centrals
    #Post: Mostraré llistes de paraules que tenen els elements centrals iguals
     for e in s:
        laux=[]
        for x in l:
            senar=len(x)%2==1
            if senar:
                 if x[len(x)%2]==e:
                     laux.append(x)
            else:
                if x[len(x)//2]==e or x[len(x)//2+1] ==e:
                    laux.append(x)
        print("Totes les paraules de la llista {} que tenen el centre {} igual són: {}".format(l,e,laux))



def noms_que_les_lletres_enmig_son_iguals(l):
    #Mostra tots els que tenen les lletres d'enmig iguals
    


#Programa principal
l = llegir_llista()
s = retorna_conjunt(l)
llistes_comparades(l,s)





def llegir_llista():
    l=[]
    a="a"
    while a!=".":
        a=input("Introdueix un nom: ")
        if a!=".":
            l.append((a))
    return l

def retorna_conjunt(l):
    #Prec: Donada una llista de paraules
    #Post: Retorna un conjunt de caràcters del centre (si senar, centres si parell) de cada paraula
    m=[]
    for e in l:
        senar = len(e)%2==1
        if senar:
            m.append(e[len(2)//2])
        else:
            m.append(e[len(2)//2])
            m.append(e[len(2)//2+1])
    s=set(m)
    return s

def llistes_comparades(l,s):
    #Prec: DOnada una llista de paraules i un conjunt de lletres centrals
    #Post: Mostraré llistes de paraules que tenen els elements centrals iguals
     for e in s:
        laux=[]
        for x in l:
            senar=len(x)%2==1
            if senar:
                 x= list(filter(lambda x:len(x%2==0,laux)))
                laux.append(x)
            else:
            if x[len(x)//2]==e or x[len(x)//2+1] ==e:
                    laux.append(x)
        print("Totes les paraules de la llista {} que tenen el centre {} igual són: {}".format(l,e,laux))



def noms_que_les_lletres_enmig_son_iguals(l):
    #Mostra tots els que tenen les lletres d'enmig iguals
    


#Programa principal
l = llegir_llista()
s = retorna_conjunt(l)
llistes_comparades(l,s)