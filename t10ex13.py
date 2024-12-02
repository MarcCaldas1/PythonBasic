def menu():
    op = 0
    while op <1 or op>5:
        print("Menú de la calculadora: ")
        print("1: Suma")
        print("2: Resta")
        print("3: Multiplicació")
        print("4: Divisió")
        print("5: Binari")
        print("6: Octal")
        print("7: Decimal")
        print("8: Hexadecimal")
        print("9: Sortir")
        op = int(input("Introdueix una opció del menú: "))
        return op

def sumar():
    a = int(input("Introdueix el primer element: "))
    b = int(input("Introdueix el segon element: "))
    c = a + b
    print("El resultat de sumar {} més {} és {}".format(a, b, c))

def restar():
    a = int(input("Introdueix el primer element: "))
    b = int(input("Introdueix el segon element: "))
    c = a - b
    print("El resultat de restar {} menys {} és {}".format(a, b, c))

def multiplicar():
    a = int(input("Introdueix el primer element: "))
    b = int(input("Introdueix el segon element: "))
    c = a * b
    print("El resultat de mutliplicar {} més {} és {}".format(a, b, c))

def dividir():
    a = int(input("Introdueix el primer element: "))
    b = int(input("Introdueix el segon element: "))
    c = a / b
    print("El resultat de dividir {} entre {} és {}".format(a, b, c))

def binari():
    a = int(input("Introdueix el nombre: "))
    b = bin(a)
    print("El nombre {} és igual a {}.".format (a, b))

def octal():
    a = int(input("Introdueix el nombre: "))
    b = oct(a)
    print("El nombre {} és igual a {}".format (a, b))

def decimal():
    a = input("Introdueix el nombre: ")
    b = int(input("Introdueix la base del nombre (2 per binari, 8 per octal, 16 per hexadecimal): "))
    c = int(a, b)
    print("El nombre {} és igual a {}".format (a,c))

def hexadecimal():
    a = int(input("Introdueix el nombre: "))
    b = hex(a)
    print("El nombre {} és igual a {}".format(a, b))


a = True
while a:
    op = menu()
    match op:
        case 1:
            sumar()
        case 2:
            restar()
        case 3:
            multiplicar()
        case 4:
            dividir()
        case 5:
            binari()
        case 6:
            octal()
        case 7:
            decimal()
        case 8:
            hexadecimal()
        case 9:
            a = False
            print("Adéu, gràcies per haver utilitzat la calculadora! \n")
        case _:
            print("Opció no vàlida \n")