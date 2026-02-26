import numpy as np
import math 
import pylab as pl 

z=1+2j
# z=complex(1,2)
# X=pl.array([1,3])
# Y=pl.array([2,4])
# pl.plot(X,Y)
# pl.plot(X,Y,color="blue") # color est un argument optionnel...
# pl.show() # provoque l’affichage si vous ^etes chanceux
# pl.savefig("segment.pdf") # enregistre dans un pdf. : marche mieu

# pl.axis('equal')
# pl.clf()

# print(z)


# A=complex(1,2)
# B=complex(3,4)
# L=np.array([A,B])

# X=np.real(L)
# Y=np.imag(L)
# pl.clf() # clf pour clearfigure
# pl.plot(X,Y)
# # pl.savefig('segment2.pdf')
# pl.show()


import numpy as np
import matplotlib.pyplot as plt


def TSC(A: complex, B: complex):
    """
    Transformation Segment Complexe (Von Koch) sur le segment [A,B].

    Renvoie la liste [A, C, D, E] où C, D, E sont définis relativement à A et B :
      - C = A + (B-A)/3
      - E = A + 2(B-A)/3
      - D = C + (E-C) * exp(i*pi/3)   (rotation de +60° du vecteur (E-C))
    """
    A=complex(A)
    B=complex(B)
    L= B-A
    C= A + L /3
    E = A+ 2* L/3

    rotation = np.exp(1j*math.pi/3)
    D=C+(E-C) * rotation

    return [A,C,D,E]


# print(TSC(1,2))
def TGC(L):
    """
    Transformation Globale Complexe.
    Prend une liste L de complexes (polyline) et insère C,D,E entre chaque paire successive A,B.

    Retourne LT.
    """
    if len(L) < 2:
        return list(L)
    
    L= [complex(z) for z in L]
    LT = []


    for i in range(len(L) - 1):
        A,B = L[i], L[i+1]
        LT.extend(TSC(A, B))   # ajoute [A, C, D, E] pour le segment [A,B]

    LT.append(L[-1])           # on termine par le dernier point B
    print(LT)
    return LT

# print(TGC(TSC(1,2)))
    




def VonKochIC(n: int, L=None):
    """
    Von Koch par Itération en Coordonnées Complexes.
    - n : nombre d'itérations (>=0)
    - L : liste initiale de complexes (par défaut [0,1])

    Affiche la courbe après n itérations.
    """
    if L is None:
        L = [0, 1]

    L = [complex(z) for z in L]

    for _ in range(n):
        L = TGC(L)

    X = [z.real for z in L]
    Y = [z.imag for z in L]

    plt.figure()
    plt.plot(X, Y)
    plt.axis("equal")
    plt.grid(True)
    plt.title(f"Courbe de Von Koch (n={n})")
    plt.show()

    return L  


def FloconVonKoch(n: int):
    """
    Flocon (triangle équilatéral) en fermant la polyline.
    """




VonKochIC(5)       
# FloconVonKoch()   
