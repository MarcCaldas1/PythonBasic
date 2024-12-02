"""p = ""
l = []
while (p !="."):
    p = input("Introdueixi una paraula: ")
    if p !="." and len(p) == 4:
        l.append(p)
    if len(l) == 4:
        print("Les paraules són: {}".format(l))
        p = "."
print("Ja hem acabat.")"""




"""p = ""
l = []
while (p !=":"):
    p = input("Introdueixi una paraula: ")
    if p != ":" and p[0] == "A":
        l.append(p)
print("Les paraules que comencen per A són {}".format(l))"""


"""
#Exercici 3
p = ""
l = []
while (p != "?"):
    p = input("Introdueixi una paraula: ")
    if p!= "?":
        l.append(p.lower())
print("Les paraules introduïdes són: {}".format(l))



#Exercici 4
p = ""
l = []
while (p != "?"):
    p = input("Introdueixi una paraula: ")
    if p != "?":
        l.append(p.upper())
print("Les paraules introduïdes són: {}".format(l))"""


"""#Exercici 5
p = ""
l = []
while (p != "%"):
    p = input("Introdueixi una paraula: ")
    if p != "%":
        s = p.lower()
        p = s[0].upper() + s[1:]
        l.append(s)
print("Les paraules introduïdes són: {}".format(l))"""


"""#Exercici 6
p = ""
l = []
while (p != "."):
    p = input("Introdueixi una frase : ")
    if p != ".":
        l.append(p.upper())
print("Les frases introduïdes són: {}".format(l))
print("Ja hem acabat.")"""


"""def llegir_llista():
    l = []
    p = ""
    while p != ".":
        p = input("Introdueix un element de la llista: ")
        if p != ".":
            l.append(int(p))
    return l

#Programa principal
llista = llegir_llista()
r = []
for i,e in enumerate(llista):
    if i== e:
        r.append(e)
print("La llista d'elements que coincideix element i posició és {}".format(r))"""



"""#Ex8
def llista_descendent():
    l = []
    a = True
    u = input("Intodueixi el primer nombre: ")
    l.append(u)
    while a:
        c = input("Introdueixi un nombre: ")
        if c > u:
            a = False
        else:
            l.append(c)
    return l"""


"""def modifica_string(s):
    s = "Això és un canvi, anem a veure si fora de la funció queda el canvi o no"

s = "Bon dia, això és una prova"
print(s)
modifica_string(s)
print(s)




















def operacio(a,b,c):
    c = a + b 
a = 3 
b = 4
c = 0
print(c)
operacio(a,b,c,)
print(c)



def axllista(l):
    for i in range(len(l)):
        l[i]*=3



l = [3,4,5]
print(l)
axllista(l)
print(l)"""





"""def sumal(llista):
    ls = []
    for e in llista:
        ls.append(e)
    return ls

#Programa principal
l =  [2, 3, 4]
print(l)
s = sumal(l)
print("La llista original és {} i la modificada és {}".format(l,s))"""


"""l = [3, 25, 8, 9]
a = list(map((lambda x:x+10,l)))

print(a)"""

"""#Lambda i map
l = [3, 4, 5, 7, 10]
a = list(map(lambda x:x**5,l))
print(a)


#Bucle
r = []
for e in l:
    r.append(e**5)
print(r)

#Map i funció normal
def elevatcinc(x):
    return x**5
r=list(map(elevatcinc,l))
print(r)"""






#Donada una llista que ens retorni que siguin parells
l = [3,5,6,8,9,11,12]

#Versió iterativa
r = []
for e in l:
    if e%2==0:
        r.append(e)
print(r)


#Versió amb filter (programació funcional)
def parell(x):
    if x%2==0:
        return True
    return False
r = list(filter(parell,l))
print(r)


#Versió amb funció anònima
r = list(filter(lambda x:x%2==1,l))
print(r)


#Fer el factorial de forma iterativa
n = int(input("Introdueixi el número a fer el factorial: "))
r = 1
while (n>0):
    r = r*n
    n = n -1
print(r)


#Fer el factorial en recursivitat
def fact(n):
    if n<=0:
        return 1
    else:
        return n * fact(n-1)
print(fact(3))
