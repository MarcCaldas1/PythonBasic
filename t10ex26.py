def llegir_llista():
    l = []
    a = "a"
    while a != ".":
        a = input("Introdeix una paraula: ")
        if a != ".":
            l.append(a)
    return l
def paraula_de_cada_longitud(l):
    a = []
    c = []
    for e in l:
        a.append(len(e))
    b= set(a)
    for e in b:
        y = len(list(filter(lambda x:len(x)==len(e),a)))
        c.append([e,y])
    return c

#programa principal
a = llegir_llista()
print("la paraula més llarga de la llista {} és {}".format(a,paraula_de_cada_longitud(a)))