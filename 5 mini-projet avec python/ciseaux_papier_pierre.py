import random

choix = ["c", "p", "pi"]
cpu = random.choice(choix)


while True:
    joueur = str(input(
        "c: ciseaux, p: papier, pi: pierre ? pour terminer taper fin")).capitalize()
    if joueur == cpu:
        print("égalité")
    elif joueur == "pi":
        if cpu == "p":
            print("vous perdez, le papier couvre la pierre")
        elif cpu == "c":
            print("vous gagnez, la pierre casse les ciseaux")
    elif joueur == "p":
        if cpu == "pi":
            print("vous gagnez, le papier couvre la pierre")
        elif cpu == "c":
            print("vous perdez, les ciseaux coupent le papier")
    elif joueur == "c":
        if cpu == "pi":
            print("vous perdez, la pierre casse les ciseaux")
        elif cpu == "p":
            print("vous gagnez, les ciseaux coupent le papier")
    else:
        print("je n'ai pas compris l'orthographe")
