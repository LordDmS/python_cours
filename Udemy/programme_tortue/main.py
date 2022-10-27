import turtle


def veriftype():
    n = 0
    while n == 0:
        tail = input("Entrez la taille:")
        esc = input("Entrez le nombre d'escalier:")
        try:
            tai = int(tail)
            es = int(esc)
            n = n + 1
        except:
            print("ERREUR DE TYPE: vous devez entrez un nombre")
    return tai, es


def escalier(taille, nbesc):
    for i in range(0, nbesc):
        t.forward(taille)
        t.left(90)
        t.forward(taille)
        t.right(90)
    t.forward(taille)


def carre(taille):
    for i in range(0, 4):
        t.forward(taille)
        t.left(90)


def carees(taille, nbresc):
    for i in range(0, nbresc):
        taille = taille * (nbresc + 1)
        carre(taille)


t = turtle.Turtle()
# taill, esca = veriftype()
# escalier(taill, esca)
carees(3, 4)
turtle.done()
