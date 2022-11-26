from function import f
import numpy as np
import matplotlib.pyplot as plt
from math import *
from scipy import integrate


L = float(input("Input the lower limit: "))

U = float(input("Input the upper limit: "))

n = int(input("Enter the value of n: "))

fun = input("Enter a function: ")
l = ["import numpy as np\nfrom math import *\n\ndef f(x):\n\treturn ", fun]
with open("function.py", "w") as file:
    file.writelines(l)


d = (U-L)/2

x = np.arange(-10, 10, 0.001)


def periodicf(li, lf, f, x):
    if x >= li and x <= lf:
        return f(x)
    elif x > lf:
        x_new = x-(lf-li)
        return periodicf(li, lf, f, x_new)
    elif x < (li):
        x_new = x+(lf-li)
        return periodicf(li, lf, f, x_new)


def fp(li, lf, x):
    return periodicf(li, lf, f, x)


y1 = [fp(L, U, xi) for xi in x]


def fc(x): return (1/d)*f(x)*np.cos((i*np.pi*x)/d)


def fs(x): return (1/d)*f(x)*np.sin((i*np.pi*x)/d)


An = []
Bn = []
sum = 0.0

for i in range(n):
    an = integrate.quad(fc, L, U)
    p, q = an
    An.append(p)

for i in range(n):
    bn = integrate.quad(fs, L, U)
    p, q = bn
    Bn.append(p)


for i in range(n):
    if i == 0:
        sum = sum+((An[i])/2)
    else:
        sum = sum+(An[i]*np.cos((i*np.pi*x)/d)+Bn[i]*np.sin((i*np.pi*x)/d))


plt.plot(x, sum, 'g')

plt.plot(x, y1, 'r--')

plt.axis([-10, 10, -10, 10])
plt.show()
