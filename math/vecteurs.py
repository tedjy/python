import math

def composantesVecteur():
    print("AB-> ex : A(4, 5) et B(2, 5)")
    a1 = input("A(a1, ?) : ")
    a2 = input("A(a1, a2) : ")
    b1 = input("B(b1, ?) : ")
    b2 = input("B(b1, b2) : ")
    # a = [a1, a2]
    # b = [b1, b2]
    result1 = (int(b1) - int(a1))
    result2 = (int(b2) - int(a2))
    print(f"compôsante vecteur AB-> = ({result1}, {result2})")
    return 1

composantesVecteur()



class normes():
    print("||u|| = sqrt(3²+2²) = sqrt(13)")
    a = input("entrez la valeur a de la norme : ")
    b = input("entrez la valeur b de la norme : ")
    # print(a, b)
    a = int(a)
    b = int(b) 
    p1 = int(a**2)
    p2 = int(b**2)
    u = p1 + p2
    print("valeur de la norme = ||u|| = racine carré de " , {u})
normes()


def carreScalaire(): 
    print("(u)² = ||u||²")
    a = input("entrez la valeur a de la norme : ")
    b = input("entrez la valeur b de la norme : ")
    # print(a, b)
    a = int(a)
    b = int(b) 
    p1 = int(a**2)
    p2 = int(b**2)
    u = p1 + p2
    print("carré scalaire (u)² = ||u||² = ", {math.sqrt(u**2)})
    return 1
carreScalaire()


def operationsArithmetiques():
    # + produit Scalaires
    return 1

operationsArithmetiques()

def angleDeuxDroites():
    return 1 

