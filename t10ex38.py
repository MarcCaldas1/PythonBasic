x=input("Introdueix una paraula: ")
y=input("Introdueix una altre paraula: ")
if x[-3:]==y[-3:]:
    print("{} i {} rimen perquè les 3 últimes lletres són iguals".format(x,y))