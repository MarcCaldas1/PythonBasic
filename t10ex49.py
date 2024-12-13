"""Definir una funció llista_20_elements() que retorni una llista de 20 elements creats aleatòriament entre 1 i 100. 
Provar amb la funció anterior si s'han generat elements duplicats o no."""

import random

def llista_20_elements():
    l=[]
    for i in range(20):
        a=l.append(random.randint(0,101))
    print("Els nombres de la llista aleatòria són: {}".format(l))

a= llista_20_elements()
    

