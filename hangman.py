import random
from obrazek import obrazky

def choose_word():
    seznam_slov = ["snehulak", "pyladies", "podzim", "jednicka", "kopretina"]
    for word in seznam_slov:
        word = random.choice(seznam_slov)
        return word

slovo = choose_word()
pole = "-" * len(slovo)

neuspesny_pokus = 0

def tah_hrace(pole, neuspesny_pokus):
    pismeno = input("Hádej písmeno:")
    if pismeno in slovo:
        cislo_policka = slovo.index(pismeno)
        print("Super, trefil ses, písmeno ", pismeno, "je ve slově.")
        return pole[:cislo_policka] + pismeno + pole[cislo_policka + 1:], neuspesny_pokus
    elif pismeno not in slovo:
        print(obrazky[neuspesny_pokus])
        neuspesny_pokus = neuspesny_pokus + 1
        print("Tohle písmeno ve slově není.")

        return pole, neuspesny_pokus

while True:
    print(pole)
    pole, neuspesny_pokus = tah_hrace(pole,neuspesny_pokus)
    if "-" not in pole:
        print("Vyhrál jsi. Gratuluji")
        break
    elif neuspesny_pokus > 8:
        print("Smůla kámo, prohrál jsi.")
        break
