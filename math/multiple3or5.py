
import numpy as np

def multiple3or5():
    array = []
    for i in range(1, 10):
        if i % 3 == 0 or i % 5 == 0:
            array.append(i)
    sum = np.sum(array)
    print(sum)

multiple3or5()
