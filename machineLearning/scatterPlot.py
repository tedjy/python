import numpy
import matplotlib.pyplot as plt

x = numpy.random.normal(5, 2.0, 100)
y = numpy.random.normal(10, 1.0, 100)

plt.scatter(x, y)
plt.show()