print("aire d'un carré")

def aircarre():
    number = input("entrer une valeur : ")
    # print(f"voici le nombre choisi : {int(number)}")
    num = int(number)
    print(f"voici le nombre : {num}")
    print(num ** 2)
    return 1 

aircarre()
print("aire d'un rectangle : ")
def aireRectangle():
    longeur = input("entrer une longueur : " )
    largeur = input("entrer iune largeur : ")
    result = int(longeur) * int(largeur)
    print(result)
    return 1 

aireRectangle()

print("aire d'un triangle : ")
def aireRriangle():
    base = input("entrer une base : ")
    hauteur = input("entrer une hauteur : ")
    result = int(base) * int(hauteur) / 2
    print(f"aire du triangle {result}")
    return 1 

aireRriangle()

print("aire d'une losange : ")
def aireLosange():
    grandeDiagonale = input("entrez la diagonale : ")
    petiteDiagonale = input("petite diagonale : ")
    result = int(grandeDiagonale) * int(petiteDiagonale) / 2 
    print(result)
    return 1 

aireLosange()

print("aire d'un trapèze : ")
def airTrapeze():
    grandeBase = input("entrez la grande base : ")
    petiteBase = input("petite base : ")
    hauteur = input("hauteur : ")
    result = (((int(grandeBase) + int(petiteBase)) / 2) * int(hauteur))
    print(f"resultat : {result}")
    return 1 

airTrapeze()
