def ertekel():
    print("I/A, B: ")
    etel = input("\tÉtel neve: ")
    nev = input("\tÉtel rendelőjének neve: ")
    ertekeles = int(input("\tÉrtékelés (1-5): "))
    while ertekeles > 5 or ertekeles < 1:
        if ertekeles < 0:
            ertekeles = int(input("\tAz értékelés nem lehet negatív!"))
        elif ertekeles > 5:
            ertekeles = int(input("\t5 pont feletti értékelés nem elfogadható!"))
        elif ertekeles == 0:
            ertekeles = int(input("\tAz értékelés nem lehet nulla! "))

    print("I/C:\n\tKöszönjük az értékelést!")
