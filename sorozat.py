import random

szamok = []


def general():

    while len(szamok) < 12:
        vel = int(random.random()*1011) - 10
        szamok.append(vel)


def kiir():
    eredmeny = ""

    i = 0
    while i < len(szamok) - 1:
        eredmeny += str(szamok[i]) + "$"
        i += 1
    print(eredmeny + str(szamok[i]))


def paratlanok_szama():
    paratlan = 0
    i = 0
    while i < len(szamok):
        if szamok[i] % 2 == 1:
            paratlan += 1
        i += 1
    return paratlan


def konzol_kiir():
    x = paratlanok_szama()
    eredmeny = f"A páratlanok száma: {x}."
    print(f"II/D, E:\n\t", eredmeny)
    fajlba_kiir(eredmeny)


def fajlba_kiir(x):
    fajl = open("eredmeny.txt", "w", encoding="utf-8")
    fajl.write(x)
    fajl.close()
    fajl = open("eredmeny.txt", "r", encoding="utf-8")
    tartalom = fajl.readlines()
    fajl.close()

    print("kimutatas.txt tartalma:\nII/F:")
    i = 0
    while i < len(tartalom):
        sor = tartalom[i].strip()
        print("\n", sor)
        i += 1
