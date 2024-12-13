"""Escriure un programa que ens permeti jugar a una versió simplificada del joc de MasterMind,
 el joc consisteix en crear un codi de 4 xifres i demanar a l’usuari que vagi introduint codis de 4 xifres fins que l’endevini.
 En cada jugada, li direm quants número ha encertat (estan en la posició correcte) i quants coincideixen (i són, però no estan en la posició correcte).
"""


import random

def generar_codi_secret():
    return [random.randint(0, 9) for _ in range(4)]

def jugar(codi_secret):
    while True:
        intent = []
        print("Introdueix un codi de 4 xifres (separades per espais):")
        while len(intent) != 4:
            try:
                intent = list(map(int, input().split()))
                if len(intent) != 4:
                    print("Has d'introduir exactament 4 xifres. Torna a provar.")
            except ValueError:
                print("Entrada invàlida. Assegura't d'introduir 4 nombres separats per espais.")

        encerts = sum(1 for i in range(4) if codi_secret[i] == intent[i])
        coincidencies = sum(min(codi_secret.count(x), intent.count(x)) for x in set(intent)) - encerts

        print("Encerts (posició correcta): {}".format(encerts))
        print("Coincidències (nombre correcte en posició incorrecta): {}".format(coincidencies))

        if encerts == 4:
            print("Felicitats! Has endevinat el codi!")
            break

# Programa principal
if __name__ == "__main__":
    codi = generar_codi_secret()
    print("El joc ha començat! Prova d'endevinar el codi secret.")
    jugar(codi)