# Predict the speed of a 10 years old car:
from scipy import stats
import matplotlib.pyplot as plt
x = [5,7,8,7,2,17,2,9,4,11,12,9,6]
y = [99,86,87,88,111,86,103,87,94,78,77,85,86]

slope, intercept, r, p, std_err = stats.linregress(x, y)

def myfunc(x):
  return slope * x + intercept

mymodel = list(map(myfunc, x))

speed = myfunc(10)
print(f"Predicted speed for a 10 years old car: {speed}")
plt.title(f"vitesse predite pour une voiture de 10 ans")
plt.scatter(x, y, label=f"data")
plt.plot(x, mymodel, color = "red", label=f"linear regression")
plt.scatter(10, speed, color="green", label=f"la prédiction ")
plt.axvline(x=10, color='green', linestyle='solid')
plt.axhline(y=speed, color='green', linestyle='solid')

plt.xlabel("age de la voiture (année)")
plt.ylabel("vitesse (km/h)")
plt.legend()
plt.show() 
