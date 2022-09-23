# ecrire un programme qui affiche les 100 premiers nombres#
print("### exo 1 ###")

for i in range(1,101):
    print(f"les 100 premiers nombres sont {i} : ")
# un programme qui demande à l'utilisateur de saisir son age
# et de lui afficher le message vous etes majeur !
print("### exo 2 ###")

age= int(input("entrer votre age svp "))

if (age>=18):
    print("vous etes majeur")
else:
    print("vous etes mineur")
#  un programme qui demande à l'utilisateur de saisir un entier n
# et de lui afficher la valeur de la somme
print("### exo 3 ###")
n= int(input("entrer un entier"))
s=0
for i in range(1,n+1):
    s=s+i
print("la somme est:",s)
##  un programme qui demande à l'utilisateur de saisir un entier n
# et de lui afficher n!
print("### exo 4 ###")
facto=1
n= int(input("entrer un nombre"))
for i in range(1,n+1):
    facto=facto*i
print(f"factorielle de {n} est : ",facto)
##  un programme qui demande à l'utilisateur de saisir un entier n
# et de lui afficher tous les diviseurs de ce nombre
print("### exo 5 ###")
n=int(input("taper la valeur de n : "))
for i in range(1,n+1):
    if(i%n==0):
        print(f"{i} est un diviseur de {n} !!!")
##  un programme qui demande à l'utilisateur de saisir un entier n
# et de lui afficher la table de multiplication de ce nombre
# afficher tous les tables de multiplications de tous les nomres compris entre
# 1 et 9
print("### exo 5 ###")
for n in range(1,10):
    print("-----------------------")
    for i in range(1,10):
        print(f'{i}x{n} = {i*n}')