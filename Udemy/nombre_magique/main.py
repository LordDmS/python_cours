import random


def demander_nombre(nbmin, nbmax):
    n = 0
    while n == 0:
        nbre_str = input(f"quel est le nombre magique (entre {nbmin} et {nbmax}) : ")
        try:
            nbre_int = int(nbre_str)
        except:
            print("ERREUR DE TYPE: vous devez rentrer un nombre")
            print("**********************************************")
            print()
        else:
            if nbre_int < nbmin or nbre_int > nbmax:
                print(f"ERREUR DE PLAGE: Vous devez saisir un nombre entre {nbmin} et {nbmax}")
                print("**********************************************")
                print()
            else:
                n += 1
    return nbre_int


# programme principale
NBMIN = 1
NBMAX = 10
NBMAGIC = random.randint(NBMIN, NBMAX)
NBVIE = 3
nb = 0
vies = NBVIE
""""
while not nb == NBMAGIC and vies > 0:
    print("*******************************")
    print(f"*** vous avez {vies} vie(s) ***")
    print("*******************************")
    nb = demander_nombre(NBMIN, NBMAX)
    if nb == NBMAGIC:
        print("Bravo, vous avez gagne")
    elif nb > NBMAGIC:
        print("le nombre magique est plus petit")
        print()
        vies -= 1
    else:
        print("le nombre magique est plus grand")
        print()
        vies -= 1
if vies == 0:
    print(f"Vous avez perdu! le nombre magic etait: {NBMAGIC}")
"""
win = False
for i in range(0, NBVIE):
    vies = NBVIE - i
    print("*******************************")
    print(f"*** vous avez {vies} vie(s) ***")
    print("*******************************")
    nb = demander_nombre(NBMIN, NBMAX)
    if nb == NBMAGIC:
        print("Bravo, vous avez gagne")
        win = True
        break
    elif nb > NBMAGIC:
        print("le nombre magique est plus petit")
        print()
    else:
        print("le nombre magique est plus grand")
        print()
if not win:
    print(f"Vous avez perdu! le nombre magic etait: {NBMAGIC}")
