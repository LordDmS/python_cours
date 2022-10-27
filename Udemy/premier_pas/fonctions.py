def affichage_qcm():
    print("""
    *********************************************************
        -------------------------------------------------
         la Guinee est un pays de: 
        -------------------------------------------------
         1: Afrique de l'ouest       3: Afrique du nord
        -------------------------------------------------
         2: Afrique de l'est         4: Afrique du sud
        -------------------------------------------------
                     5: Afrique central
        -------------------------------------------------    
    *********************************************************""")
    veriftype()


def veriftype():
    n = 0
    while n == 0:
        entree = input("Entrez votre choix:")
        try:
            choix = int(entree)
            n = n + 1
        except:
            print("ERREUR DE TYPE: vous devez entrez un nombre")
    verifplage(choix)


def verifplage(ch):
    if 1 <= ch <= 5:
        verifresultat(ch)
    else:
        print("Erreur vous devez entrer un nombre entre '1' et '5'")
        veriftype()
    return ch


def verifresultat(resultat):
   if resultat == 1:
       print("""
       **********************************************************************
           ---------------------------------------------------------------
            **** la Guinee est  bien un pays de l'Afrique de l'ouest **** 
           ---------------------------------------------------------------
            **** FELICITATION VOUS AVEZ TROUVEZ LA BONNE REPONSE ****
           ---------------------------------------------------------------   
       **********************************************************************""")
   else:
       print("Desole mauvaise reponse s'il vous plait veillez ressectionnez un autre choix")
       affichage_qcm()


# programe principale
# appelle des fonctions
affichage_qcm()
