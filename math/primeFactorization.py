import numpy as np

def primeFactorization(n):
    factor = []
    for i in range(2, n + 1):
        while n % i == 0:
            factor.append(i)
            n = n // i
            print("factor : FACTOR", factor)
    convertToString = ' x '.join(str(e) for e in factor)
    print("result = ", convertToString)
    return factor



n = int(input("Enter a number: "))
factors = primeFactorization(np.sum(n))