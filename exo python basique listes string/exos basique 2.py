'''
# ecrire un programme qui permet d'afficher et parcourir
# les caracteres d'une variable de type chaine 
print("### exo 1 ###")
c= "python"
for i in range(0,len(c)):
     print(c[i])
# ecrire un programme qui permet d'afficher une chaine de caractère donnée
# le nombre d'occurrence de chaque caractères dans la chaine
print("### exo 2 ###")
c= "python.org"
for i in range(0,len(c)):
     print(f"le caractere '{c[i]}' figure {c.count(c[i])} dans la chaine {c}")
# ecrire un programme qui demande à l'utilisateur de saisir une chaine de caractere
# et de lui envoyer un msg indiquant si la chaine contient la lettre a tout en
# indiquant sa position sur la chaine
print("### exo 2 ###")
x= str(input("entrer la chaine : "))
v= str(input("entrer la chaine à verifiée: "))
for i in range(0,len(x)):
     if(x[i] in v):
          print(f"Yes la lettre {v} se trouve à la position : {i}")
     else:
          print("Oups sorry !!!")
print("### exo 3 ###")
# ecrire un programme qui permet de compter le nbr de voyelle dans une chaine donnée
n= "anticonstitutionnellement"
voyelle=0
for i in range(0,len(n)):
     if(n[i] in["a","i","u","o","y","e"] ):
          voyelle=voyelle+1
print(f"la chaine {n} possede {voyelle} voyelles")
print("### exo 4 ###")
# ecrire un programme qui permet de renvoyer le 1er mot d'un texte donné


t="python est un merveilleux langage de programmation"
i=0
espace=" "
while(t[i] !=" "):
     espace=espace + t[i]
     i=i+1
print(f"le premier mot est {espace}")
print("### exo 5 ###")
# ecrire un programme qui demande à l'utilisateur de saisir un texte et de
# lui renvoyer tous les mots commencants par la lettre a
m= str(input("ecrivez une phrase : "))
n= m.split()
for i in n:
     if(i[0] =="a"):
          print('le mot ',i,"commence par la lettre 'a' ")

print("### exo 6 ###")
# ecrire un programme python qui permet de supprimer
# les elements dupliquées d'une liste
x= [10,2,5,6,2,0,8,10]
def supdup(x):
     u=[]
     for i in x:
          if i not in u:
               u.append(i)
     return u
print(f'la liste est : {supdup(x)}')
print("### exo 6 ###")
# ecrire un programme qui demande à l'utilisateur de saisir un mot 
# et de lui renvoyer inverse
mp= "hello"
def donne_moi_linverse(d):
     s=""
     for i in d:
          s=i+s 
     return s
print(f'l \' inverse est : {donne_moi_linverse(mp)} ')
print("### exo 6 ###")
# ecrire un programme qui demande à l'utilisateur de saisir un mot 
# et de lui renvoyer s'il sagit de palindrome ou pas
p= "laval"
inv= p[:: -1]
if p== inv:
     print("le mot ",p," est un palindrome")
else:
     print("le mot ",p," n'est pas un palindrome")
print("### exo 7 ###")
# ecrire un programme python qui remplace les caractères d'index
# impairs d'une chaine de caractères par #.
s="python"

def remp_index(c):
     for i in range(0,len(c)):
          w=""
          if(i% 2!=0):
               w=w+"#"
          else:
               w=w+c[i]
print(f"je remplace par # les mots de {s} par {remp_index(s)}")
print("### exo 8 ###")
# ecrire un programme en python  sous forme de
# de fonction qui determine la longueur d'une chaine
# sans utliser la methode len() ni autre methode 
# predefinie en python
x="python"
def longueur_dune_chaine(f):
     s=0
     for i in f:
          s=s+1
     return s
print(f'la longueur du chaine est : {longueur_dune_chaine(x)}')
'''


