import matplotlib.pyplot as plt
import numpy as np
from polyplotter import polyplot

cords = open("C:\Coding\CPP\coordinates.txt")
coef = open("C:\Coding\CPP\coefficients.txt")

n = int(cords.readline())

xp = []
yp = []

for line in cords:
    xp.append(float(line.split(' ')[0]))
    yp.append(float(line.split(' ')[1]))

xp = np.array(xp)
yp = np.array(yp)

coefs = coef.readline().split(' ')
coefs.remove('')

a = min(xp)
b = max(xp)

p = a

xpol = []
ypol = []
while p <= b :
    xpol.append(p)
    ypol.append(polyplot(coefs,p))
    p = p+0.01

xpol = np.array(xpol)
ypol = np.array(ypol)

plt.scatter(xp, yp)
plt.plot(xpol, ypol)
plt.show()


