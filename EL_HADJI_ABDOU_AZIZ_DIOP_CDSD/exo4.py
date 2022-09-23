
print("chaine inversée")
X= "citoyen"
n=""
for i in X:
    n=i+n   
print(n)
print("dire si un mot est oui ou non un palyndrome")
p= "RADAR"
inv= p[:: -1]
if p== inv:
     print("oui le mot ",p," est un palindrome")
else:
     print("non le mot ",p," n'est pas un palindrome")
