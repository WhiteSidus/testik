print ("Vítam Vas v programu pro vypočet Ohmůva zákoná nebolí Odporu\b")

historie = []

U = ()
I = ()
R = ()

while True:
    vyber =  input("Co chcete vypočitat - Odpor(R), Napětí(U), Proud(I): ")
    if vyber == "R" or vyber == "Odpor"  or vyber == "r":
        
        U = float(input("Zadejte napetí (U): "))
        if U <= 0:
            print("Neplatna čislo. Zadejte znovu.")

        I = float(input("Zadejte proud (I): "))
        if I <= 0:
            print("Neplatna čislo. Zadejte znovu.")

        R = U/I
        print(f"Vzorec R=U/I (R = {U} V / {I} A)")
        print(f"Vysledek je: {R} Ω")

        

    elif vyber == "U" or vyber == "Napětí"  or vyber == "u":

        I = float(input("Zadejte proud (I): "))
        if I <= 0:
            print("Neplatna čislo. Zadejte znovu.")

        R = float(input("Zadejte odpor (R): "))
        if R <= 0:
            print("Neplatna čislo. Zadejte znovu.")

        U = R*I
        print (f"Vzorec U=R*I (U = {R} Ω * {I} A)")
        print(f"Vysledek je: {U} V")

    elif vyber == "I" or vyber == "Odpor" or vyber == "i":

        U = float(input("Zadejte napetí (U): "))

        R = float(input("Zadejte odpor (R): "))

        if R or U <= 0:
            print("Neplatna čislo. Zadejte znovu.")
            break

        else:
            I = U/R
            print(f"Vzorec I=U/R ( I = {U} V / {R} Ω)")
            print(f"Vysledek je: {I} A")

    else:
        print("Jste ne zadali co chcete vypočitat.")
    
    opakovani = input("Chcete pokračovat? (yes/no) ")
    if opakovani != "yes":
        break