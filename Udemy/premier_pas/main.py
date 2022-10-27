# fonction demander un language
def demanderlanguage():
    var = ""
    while var == "":
        var = input("Quel est ton language: ")
    return var


# fonction demander le temps
def demandercour(nom_cour):
    n = 0
    while n == 0:
        temps = input("Pour le language '" + nom_cour + "' vous travaillez depuis combien de temps: ")
        try:
            reste = 2100 - int(temps)
            n = n + 1
        except:
            print("ERREUR: vous devez entrez un nombre")
    return reste, temps


# fonction d'affichage
def afficher(language, temps, reste):
    print("*********************************************************************************************")
    print()
    print(" * Merci de suivre les cours de '" + language + "' depuis '" + temps + "' jours *")
    if int(temps) <= 700:
        print(" * Il vous reste  '" + str(reste) + "' jours pour finir le cour et vous etes au niveau << Debutant >>*")
    elif 701 <= int(temps) >= 1400:
        print(" * Il vous reste  '" + str(reste) + "' jours pour finir le cour et vous etes au niveau << Avancee >>*")
    else:
        print(" * Il vous reste  '" + str(reste) + "' jours pour finir le cour et vous etes au niveau << intermediaire >>*")

    print()
    print("*********************************************************************************************")


""" appelle de la fonction demander le nom du language
nom = demanderlanguage()
nom1 = demanderlanguage()
nom2 = demanderlanguage()

# appelle de la fonction demander le temps
rest, tmp = demandercour(nom)
rest1, tmp1 = demandercour(nom1)
rest2, tmp2 = demandercour(nom2)

# appelle de la fonction d'affichage
afficher(nom, tmp, rest)
afficher(nom1, tmp1, rest1)
afficher(nom2, tmp2, rest2)
"""
N = 3
for i in range(0, N):
    nom = demanderlanguage()
    rest, tmp = demandercour(nom)
    afficher(nom, tmp, rest)
