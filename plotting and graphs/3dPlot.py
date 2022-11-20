import matplotlib.pyplot as plt
ax = plt.axes(projection = '3d')

func = input("Enter x as a function of t\n")
with open("somePyfile1.py", 'w') as file:
    file.write("from math import *\ne=2.718281828459045\npi=3.14159265358979\n\ndef x(t):\n\treturn " + str(func))
func = input("Enter y as a function of t\n")
with open("somePyfile2.py", 'w') as file:
    file.write("from math import *\ne=2.718281828459045\npi=3.14159265358979\n\ndef y(t):\n\treturn " + str(func))
func = input("Enter z as a function of t\n")
with open("somePyfile3.py", 'w') as file:
    file.write("from math import *\ne=2.718281828459045\npi=3.14159265358979\n\ndef z(t):\n\treturn " + str(func))
from somePyfile1 import x
from somePyfile2 import y
from somePyfile3 import z
print("Enter range for t ")
tr = []
tr.append(float(input()))
tr.append(float(input()))

xp = []
yp = []
zp = []
t = tr[0]

while t < tr[1]:
    zp.append(z(t))
    xp.append(x(t))
    yp.append(y(t))
    t = t+0.01

ax.scatter(xp,yp,zp)
plt.show()
