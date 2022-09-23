'''''
print("### exo 1 ###")
# ecrire un programme python qui regroupe dans une liste tous les
# mots commencants par une majuscule dans une chaine donnée s.
s="""Python est un langage de programmation de haut niveau.
Développé à l'origine par Guido Van Rossum en 1989"""
# split permet de separer les mots en chaine
L=s.split()
word_maj=[]
for word in L:
    if word[0].isupper():
        word_maj.append(word)
print(f'les mots commencants par majuscule {word_maj} ')
'''
print("### exo 2 ###")
# ecrire un programme sous forme de fonction qui prend en parametre
# une chaine s et qui retourne la liste de tous les mots contenus
# dans s dont la longueur est superieur ou egale à 7.
s="python est un langage de programmation orienté objet"
M=s.split()
f=[]
for i in M:
    if len(i)>=7:
        f.append(i)
print(f)