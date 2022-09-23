

texte = str(input("entrer une chaine de caractère : "))
'''       
mots = texte.split()

accro = ""
for i in mots:
    accro = accro+str(i[0]).upper()
print(accro)
'''
######################


def gener_accro(chaine):
    mots = chaine.split()
    accro = ""
    for i in mots:
        accro = accro+str(i[0]).upper()
    return accro


resultat = gener_accro(texte)
print(resultat)
