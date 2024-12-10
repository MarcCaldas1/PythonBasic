"""
Any actual 2022
Nom			Data naixement	Anys que farà aquest any
Pere			2000			22
Maria			1999			23
Anna			2005			17
"""

a = "2024"
d = []
l = []
for i in range(4):
    d.append(input("Indica el teu nom: "))
    d.append(input("Indica l'any (aaaa) que vares néixer: "))
    l.append(d)
    d.clear()
print("{:<20}  {:20}  {:20}".format("Nom", "Data naixement", "Anys que farà aquest any"))

for e in l:
    print(" {:<20}  {:20}  {:20}".format(i[0],i[1],int(a)-int(i[1])))