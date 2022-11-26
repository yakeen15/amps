import numpy as np
import matplotlib.pyplot as plt
from math import *
from scipy import integrate
import imageio
import os

#plt.style.use('fivethirtyeight')


L = 0
print("Lower limit is set to be 0.")

U = float(input("Input the upper limit: "))

n = int(input("Enter the value of n: "))

fun = input("Enter a function: ")
l = ["import numpy as np\nfrom math import *\n\ndef f(x):\n\treturn ", fun]
with open("function.py", "w") as file:
    file.writelines(l)
from function import f

d = U

x = np.arange(-10, 10, 0.05)


def periodicf(li, lf, f, x):
    if x >= li and x <= lf:
        return f(x)
    elif x > lf:
        if int((x-li)/(lf-li))%2==0:
            return f(li+((x-li)%(lf-li)))
        else:
            return -f(lf-((x-li)%(lf-li)))
    elif x < (li):
        if int((lf-x)/(lf-li))%2==0:
            return f(lf-((lf-x)%(lf-li)))
        else:
            return -f(li+((lf-x)%(lf-li)))


def fp(li, lf, x):
    return periodicf(li, lf, f, x)


def fs(x): return (1/d)*f(x)*np.sin((i*np.pi*x)/d)


Bn = []
sum = 0.0

for i in range(n):
    bn = integrate.quad(fs, L, U)
    p, q = bn
    Bn.append(p)


for i in range(n):
    sum = sum+2*Bn[i]*np.sin((i*np.pi*x)/d)


if __name__ == "__main__":

    plt.style.use('dark_background')
    #plt.style.use('seaborn')
    plt.title(f'Half Range Fourier Sine Series\n{fun}')


    y1 = [fp(L, U, xi) for xi in x]
    
    lim = ((fp(L, U, xi) for xi in x))
    y_max = max(lim)
    lim = ((fp(L, U, xi) for xi in x))
    y_min = min(lim)

    x_plot = []
    y_plot1 = []
    y_plot2 = []
    filenames = []

    x_l_plot = -10 - 15
    x_u_plot = x_l_plot + 20
    plt.xlim(x_l_plot, x_u_plot)
    plt.ylim(y_min - 5, y_max + 5)

    for i in range(x.size):
        x_plot.append(x[i])
        y_plot1.append(y1[i])
        y_plot2.append(sum[i])
        plt.plot(x_plot, y_plot1, c='darkkhaki')
        plt.plot(x_plot, y_plot2, c='tomato')
        
        x_l_plot = x_l_plot + 0.05
        x_u_plot = x_u_plot + 0.05
        plt.xlim(x_l_plot, x_u_plot)
        plt.pause(0.001)
        
        filename = f'{i}.png'
        filenames.append(filename)
        plt.savefig(filename)
    with imageio.get_writer('sine.gif', fps=60) as writer:
        for filename in filenames:
            image = imageio.v2.imread(filename)
            writer.append_data(image)
    
    for filename in set(filenames):
        os.remove(filename)
    plt.show()
