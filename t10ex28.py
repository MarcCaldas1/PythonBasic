def num_majuscules(s):
    num = 0
    for e in s:
        if e in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
            num += 1
    return num

#Programa principal
a = input("Introdueixi una paraula amb Majúscules i minúscules: ")
print("El número de majúscules que té la paraula {} és de {}".format(a,num_majuscules(a)))