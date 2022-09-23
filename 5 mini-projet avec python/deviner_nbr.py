import random

nbr_choisi = random.randint(1, 6)
resultat = 0

for i in range(3):
    nbr_propose = int(input("saisir un nombre: "))
    if nbr_choisi == nbr_propose:
        resultat = 1

        break
    elif nbr_propose > nbr_choisi:
        print("le nombre que vous avez choisi est superieur à celui que j'ai choisi")
    elif nbr_propose < nbr_choisi:
        print("le nombre que vous avez choisi est inferieur à celui que j'ai choisi ")

if resultat == 1:
    print("bravo, bien joué")
    print(f"le bon numero est {nbr_choisi}")
else:
    print(f"vous perdez le bon numero etait {nbr_choisi}")
