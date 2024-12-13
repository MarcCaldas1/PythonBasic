def es_de_traspas():
    a= int(input("Introdueix l'any actual: "))
    if a%4==0 and a%400==0:
        print("L'any {} és de traspas".format(a))
    else:
        print("L'any {} no és de traspas".format(a))


es_de_traspas()