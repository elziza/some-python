import random
print("1:lancer le dé - 0: quitter le programme ")
while True:
    x = int(input("cliquer sur un bouton : "))
    if x == 0:
        print('bye à la prochaine')
        break
    elif x == 1:
        print(random.randint(1, 6))
    else:
        print("je n'ai pas compris")
