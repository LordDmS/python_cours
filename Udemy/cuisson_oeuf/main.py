import time
"""
a) Oeufs a la coque (3min)
b) Oeufs mollets (6 min)
c) Oeufs dur (9 min)
"""


def conversion_time(duree):
    minute = duree // 60
    seconde = duree - minute * 60
    return minute, seconde


def decrement_time(sec):
    while not sec == 0:
        minut, second = conversion_time(sec)
        print()
        print(f"Temps restant:{minut:02d} min {second:02d} s", end="")
        for i in range(0, 10):
            time.sleep(1)
            print(".", end="", flush=True)
        n = 10
        sec = sec - n
    print("\n", "***      Cuisson terminee        ***")


def menu():
    print()
    print("***********************************")
    print("*** Programme de cuisson d'oeuf ***")
    print("***                             ***")
    print("*** a) Oeufs a la coque (3min)  ***")
    print("*** b) Oeufs mollets (6 min)    ***")
    print("*** c) Oeufs dur (9 min)        ***")
    print("***                             ***")
    print("***********************************")
    print()

    chose = input("Faites votre choix de cuisson: ")
    print()
    return chose


choix = menu()
if choix.lower() == "a":
    temps = 180
    print("*** Vous avez choisi Oeufs a la coque duree: 3 min ***")
    decrement_time(temps)
elif choix.lower() == "b":
    temps = 360
    print("*** Vous avez choisi Oeufs mollets: 6 min ***")
    decrement_time(temps)
elif choix.lower() == "c":
    temps = 540
    print("*** Vous avez choisi Oeufs dur: 9 min ***")
    decrement_time(temps)
else:
    print("*** veillez choisir entre 'a', 'b' et 'c' ***")
    menu()

