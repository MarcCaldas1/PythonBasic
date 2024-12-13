"""a = {1, 2, 3}

if 2 in a:
    print("El 2 és dins a")
else:
    print("El 2 no és dins a")"""

"""a = {"Nom":"Joan","Cognom":"Ramis","Telèfon":971360133}
for e in a:
    print("{} : {}".format(e,a[e]))"""

"""a = {"Nom":"Joan","Cognom":"Ramis","Telèfon":971360133}
for x,y in a.items():
    print(x,y)"""

"""a = {"E1":"V1","E2":"V2","E3":{"E31":"Pepe","E32":"Ramis"}}
print(a.get("E3"))"""

""" a = {"Contacte1":{"nom":"Joan","cognom":"Ramis","Telèfon":971360133},
     "Contacte2":{"nom":"Martí","cognom":"Pons","Telefòn":971360133}
     "Contacte3":{"nom":"Maria","cognom":"Carreras","Telèfon":971360133}}"""


"""a = int(input("Escriu un nombre: "))
b = int(input("Escriu un altre nombre: "))
c = a + b
print(c)"""


a = 3 + 4 * 5 / 7 ** 4 - 27
print(a)

a = (3 + 4) * 5 / (7 ** (4 - 27))
print(a)


a = int(input("Escriu un número: "))
b = int(input("Escriu un número: "))
c = int(input("Escriu un número: "))
if a > b:
    if b > c:
        print("{} és major que {} i aquest és major que {}".format(a, b, c))
    elif b < c:
        if a > c:
            print("{} és major que {} i aquest és major que {}".format(a, c, b))
        elif c>a:
            print("{} és major que {} i aquest és major que {}". format(c, a, b))
        else: print("{} i {} són iguals i majors que {}".format(a,c,b))
    else:
        print("{} i {} són iguals i menors que {}".format(b,c,a))
elif a < b:
    print("")