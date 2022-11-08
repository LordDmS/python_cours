"""
def menu_choix():
    print()
    print("*** 1 - Convertir de centimetre vers pouces ***")
    print("*** 2 - Convertir de pouces vers centimetre ***")
    print()
    n = 0
    while n == 0:
        choix = input("Faites votre choix? ")
        try:
            choix_int = int(choix)
            n += 1
        except:
            print("ERREUR DE TYPE: Veillez entrer un nombre entre 1 et 2")
        else:
            if 1 == choix_int or 2 == choix_int:
                return choix_int
            else:
                print("ERREUR entrer un nombre entre 1 et 2")
                n = 0


def verifvaleur():
    n = 0
    while n == 0:
        valeur = input("Entrez une valeur a convertir ou ' q ' pour quitter le programme: ")
        if valeur == "q":
            return True
            print("hello")
        else:
            try:
                verif = float(valeur)
                n += 1
            except:
                print("ERREUR DE TYPE: Veillez entrer un nombre")
    return verif


def convertisseur(unite1, unite2, facteur):
    print()
    print(f"Vous avez selectionnez '{unite1}' vers '{unite2}'")
    if verifvaleur():
        return True
        print("hello")
    else:
        v = verifvaleur()
        resultat = round(v * facteur, 2)
        print()
        print(f"Le resultat de la convertion de {v} {unite1} est : {resultat} {unite2}")
        return False


# programme principale
chx = menu_choix()
while True:
    if chx == 1:
        unit1 = "cm"
        unit2 = "inch"
        fact = 0.394
        if convertisseur(unit1, unit2, fact):
            break
    else:
        unit1 = "inch"
        unit2 = "cm"
        fact = 2.54
        if convertisseur(unit1, unit2, fact):
            break

print("*** Vous avez arreter le programme de conversion ***")
"""
while True:
    print()
    print("***********************************************")
    print("*** SELECTIONNEZ UN MENU POUR LA CONVERTION ***")
    print("***********************************************")
    print("*** 1 - Convertir de centimetre vers pouces ***")
    print("*** --------------------------------------- ***")
    print("*** 2 - Convertir de pouces vers centimetre ***")
    print("***********************************************")
    print()

    choix = input("votre choix (1 ou 2): ")
    if choix == "1" or choix == "2":
        break
    print("ERREUR: Vous devez choisir entre 1 ou 2")


def eff_conversion(unit1, unit2, facteur):
    valeur_str = input(f"Conversion de {unit1} -> {unit2}. Entrer la valeur en {unit1} ou 'q' pour Quitter: ")
    if valeur_str == "q":
        return True
    try:
        valeur_float = float(valeur_str)
    except ValueError:
        print("ERREUR DE TYPE: Vous devez renter un nombre numerique")
        print("(pour les chiffres a virgule utilise un point)")
        return eff_conversion(unit1, unit2, facteur)
    val_convertie = round(facteur * valeur_float, 2)
    print()
    print(f"*** La valeur convertie de {valeur_float} {unit1} est: {val_convertie} {unit2}")
    print()
    return False


while True:
    if choix == "1":
        unite1 = "CM"
        unite2 = "INCH"
        facteur_conv = 0.394
        if eff_conversion(unite1, unite2, facteur_conv):
            break

    if choix == "2":
        unite1 = "INCH"
        unite2 = "CM"
        facteur_conv = 2.54
        if eff_conversion(unite1, unite2, facteur_conv):
            break
