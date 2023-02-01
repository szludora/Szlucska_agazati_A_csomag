from Pogyasz import Pogyasz

pogyaszok = []


def feladat():
    fajl = open("csomag.txt", "r", encoding="utf-8")
    fajl.readline()
    tartalom = fajl.readlines()
    fajl.close()
    letrehoz(tartalom)


def letrehoz(tartalom):
    i = 0
    while i < len(tartalom):
        sor = tartalom[i].strip().split("#")
        pogyasz = Pogyasz(sor[0], sor[1], sor[2], sor[3])
        pogyaszok.append(pogyasz)
        i += 1


def pogyaszok_szama():
    return len(pogyaszok)


def atlag():
    i = 0
    osszsuly = 0
    db = 0

    while i < len(pogyaszok):
        if pogyaszok[i].szelesseg == 51:
            osszsuly += pogyaszok[i].suly
            db += 1
        i += 1

    atlag = int(osszsuly / db * 1000)

    return atlag


def legmagasabb():
    i = 0
    magasabb = 0

    while i < len(pogyaszok):
        if pogyaszok[i].magassag > pogyaszok[magasabb].magassag:
            magasabb = i
        i += 1

    return pogyaszok[magasabb]
