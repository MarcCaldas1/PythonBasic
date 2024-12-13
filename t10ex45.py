"""
Escriure un programa que mostri els dígits parells d’un número donat.

"""

x = (input("Intro un número: "))
i=0
for e in x:
    if i%2==0:
        print(e)
    i+=1
