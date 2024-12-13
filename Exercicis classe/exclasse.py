a = "Hola"
b = input("Llegir paraula: ")

#Mostrar caràcter a caràcter la cadena llegida
for e in b:
    print(e)

#Longitut paraula llegida
print(len(b))

#COmparar si les dues paraules son iguals
if a == b:
    print("{} i {} són iguals ".format(a,b))
else:
    print("{} i {} són diferents ".format(a,b))

#Juntar a i b amb un guió
print(a + "-" + b)

#Repetir 3 vegades la paraula de b
print(b*3)

#Mirar si la vocal a és dins b
if "a" in b:
    print("a és dins l'string {}".format(b))
else:
    print("a no hi és")


lb = [1, "hola", "b", (1,3), [3,4]]
print(lb[4])

print(b[-1])

print(lb[0:5:2])

for e in lb:
    print(e)

lb.append(3)
print(lb)

lb.extend([1,4,6])
print(lb)

lc = [1, 3, 4, 5]
ld = lb + lc
print(ld)

lp = lc*3
print(lp)

lc.insert(1, 2)
print(lc)

lc. insert(4,[1, 2, 3, 4, 5])
print(lc)

if 6 in lc:
    print("6 és dins la llista {}".format(lc))
else:
    print("6 no és dins la llista {}".format(lc))

lc[5] = 6
lc[4] = 5
print(lc)

del lc[5]
print(lc)

del lc[0:2]
print(lc)

lc.remove(4)
print(lc)

lc.pop(0)
print(lc)

lc.clear()
print(lc)

print(len(lc))

print(lp.count(1))


lp.sort()
lp.pop(0)
lp.sort()

lp.reverse()
print(lp)

lpb = lp[::-1]
print(lpb)