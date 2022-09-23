import random

longpass = int(input("donner la longueur du mot de passe : "))
alpha = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'
psw = "".join(random.sample(alpha, longpass))
print(psw)
