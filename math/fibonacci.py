import numpy as np

def fibonacci(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0,1]
    else:
        fibo_sequence = np.array([1,2])
        for i in range(2,n):
            next_fibo = fibo_sequence[i-1] + fibo_sequence[i-2]
            fibo_sequence = np.append(fibo_sequence,next_fibo)
            
        return fibo_sequence
        

n = 10
print(np.sum(fibonacci(n)))