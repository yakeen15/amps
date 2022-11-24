import numpy as np
import matplotlib.pyplot as plt
from math import *
from scipy import integrate
from matplotlib.animation import FuncAnimation

plt.style.use('fivethirtyeight')


L = float(input("Input the lower limit: "))

U = float(input("Input the upper limit: "))

n = int(input("Enter the value of n: "))

fun = input("Enter a function: ")
l = ["import numpy as np\nfrom math import *\n\ndef f(x):\n\treturn ", fun]
with open("function.py", "w") as file:
    file.writelines(l)
from function import f

d = (U-L)/2

x = np.arange(-5, 5, 0.05)


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



#plt.plot(x, sum, 'g')

#plt.plot(x, y1, 'r--')

#plt.axis([-10, 10, -10, 10])
#plt.tight_layout()
#plt.show()

for i in range(x.size):
    print(sum[i])

x_vals = []
y_vals = []
sum_vals = []

for i in range(x.size):
    plt.xlim(-5, 5)
    plt.ylim(-10, 10)
    def animate(i):
        x_vals.append(i)
        y_vals.append(fp(L, U, x[i]))
        sum_vals.append(sum[i])
        
        plt.cla()
        plt.plot(x_vals, y_vals, c='tomato')
        plt.plot(x_vals, sum_vals, c='orange')
    
ani = FuncAnimation(plt.gcf(), animate, interval = 50)

plt.show()