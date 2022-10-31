import random

NBMIN = 1
NBMAX = 10
QUESTION = 4


def poser_question():
    a = random.randint(NBMIN, NBMAX)
    b = random.randint(NBMIN, NBMAX)
    op = random.randint(0, 1)
    operateur = "+"
    if op == 1:
        operateur = "*"
    n = 0
    while n == 0:
        response_str = input(f"Calculez {a} {operateur} {b} = ")
        try:
            reponse_int = int(response_str)
            n += 1
        except:
            print(f"ERREUR DE TYPE: Veillez entrer un nombre entier entre {a} et {b}")
    if op == 1:
        calcul = a * b
    else:
        calcul = a + b
    if reponse_int == calcul:
        return True
    return False


points = 0
for i in range(0, QUESTION):
    print(f"***** Question {i+1} sur {QUESTION} *****")
    print()
    if poser_question():
        points += 1
        print()
        print("***** votre reponse est correcte *****")
    else:
        print()
        print("***** votre reponse est incorrecte *****")
print()
print(f"***** vous avez trouver {points}/{QUESTION} des questions posees *****")
moyenne = int(QUESTION/2)

if points == QUESTION:
    print("***** Excellent *****")
elif points == 0:
    print("***** Revisez vos maths *****")
elif points >= moyenne:
    print("***** Pas mal *****")
elif points < moyenne:
    print("***** Peut mieux faire *****")
