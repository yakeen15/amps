import numpy as np
import matplotlib.pyplot as plt
from math import *
from scipy import integrate
import imageio
import os

#plt.style.use('fivethirtyeight')


L = float(input("Input the lower limit: "))

U = float(input("Input the upper limit: "))

n = int(input("Enter the value of n: "))

fun = input("Enter a function: ")
l = ["import numpy as np\nfrom math import *\n\ndef f(x):\n\treturn ", fun]
with open("function.py", "w") as file:
    file.writelines(l)
from function import f

d = (U-L)/2

x = np.arange(-10, 10, 0.05)


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



if __name__ == "__main__":

    plt.style.use('dark_background')
    #plt.style.use('seaborn')
    plt.title('Periodic functions\nFourier Series')


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
    with imageio.get_writer('x cubed.mp4', fps=60) as writer:
        for filename in filenames:
            image = imageio.v2.imread(filename)
            writer.append_data(image)
    
    for filename in set(filenames):
        os.remove(filename)
    plt.show()
