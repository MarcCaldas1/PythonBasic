def llegir_llista():
    l = []
    b = "1"
    while b != ".":
        b = input("Introdueix la llista amb nombres (per aturar prem el .) ") 
        if b !=  ".":
            l.append(int(b))
    c = len(l)
    return c

print("La longitud de la llista és {}".format(llegir_llista()))
