def gran_de_tres():
    a = input("Introdueix el primer nombre: ")
    b = input("Introdueix el segon nombre: ")
    c = input("Introdueix el tercer nombre: ")
    return max(a, b, c)

resultat = gran_de_tres()
print("El nombre més gran és {}".format(resultat))  