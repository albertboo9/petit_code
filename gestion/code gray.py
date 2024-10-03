"coding: utf-8"
#</BAE>

#fonction qui permet d'obtenir le code gray d'un entier
def dectogray(num):
    """retourne le code gray correspondant à l'entier num"""
    n=(num>>1)^num
    dec2bin = lambda x, n=8:bin(x)[2:].zfill(n)
    return dec2bin(n)

#fonction qui permet de passe du code gray à l'entier
def graytodec(num):
    """retourne le nombre entier correspondant au code gray num"""
    shift = 1
    while True:
        idiv = num >> shift
        num ^= idiv
        if idiv <= 1 or shift == 32:
            return num
        shift <<= 1

a=int(input("veuillez entrer un nombre entier"))
b=dectogray(a)
print(f'le code gray de {a} est {b}')