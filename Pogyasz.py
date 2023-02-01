class Pogyasz:
    def __init__(self, szelesseg, magassag, melyseg, suly):
        self.szelesseg = int(szelesseg)
        self.magassag = int(magassag)
        self.melyseg = int(melyseg)
        self.suly = int(suly)

    def __str__(self):
        return f"{self.szelesseg}x{self.magassag}x{self.melyseg}, súlya:  {self.suly} kg."
