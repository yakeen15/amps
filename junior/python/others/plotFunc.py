import matplotlib.pyplot as plt
import numpy as np


#Shajiratul Yakeen
#AMTH batch 6
#Purpose : prints a plot of a given function over a certain interval
#Inputs : function, interval
#Outputs : graph of the function

#Caution 1 : implicit multiplication not supported ie write '3*x' instead of '3x'
#Caution 2 : use '**' instead of '^' for exponentiation

func = input("Enter some function\n")
with open("somePyfile.py", 'w') as file:
    file.write("from math import *\n\ndef f(x):\n\treturn " + str(func))
from somePyfile import f

endp = []
print("Enter lower and upper bound: ")

endp.append(float(input('')))
endp.append(float(input('')))

x = []

ix = endp[0]

while ix <= endp[1]:
    x.append(ix)
    ix=ix+0.01

xpoints = np.array(x)
y = []
for i in x:
    y.append(f(i))
ypoints = np.array(y)

plt.plot(xpoints, ypoints)
plt.show()
