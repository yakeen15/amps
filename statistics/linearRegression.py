import matplotlib.pyplot as plt
from math import sqrt

def abs(x):
    if x > 0:
        return x
    else:
        return -x

#Shajiratul Yakeen
#AMTH batch 6
#Purpose : to find the best linear expression that fits the data
#Inputs : data set
#Outputs : pearson correlation coefficient, the straight line that best fits the data

print('How many data?\n')
n = int(input(''))

xp = []
yp = []

sumx = 0
sumy = 0
sumx2 = 0
sumy2 = 0
sumxy = 0

for i in range(0,n):
    print('Enter x('+str(i)+')')
    xp.append(float(input()))

for i in range(0,n):
    print('Enter y(' + str(i) + ')')
    yp.append(float(input()))

for i in range(0,n):
    sumx = xp[i] + sumx
    sumx2 = xp[i]**2 + sumx2
    sumy = yp[i] + sumy
    sumy2 = yp[i] ** 2 + sumy2
    sumxy = xp[i]*yp[i] + sumxy

r = (n*sumxy-sumx*sumy)/(sqrt(n*sumx2-sumx**2)*sqrt(n*sumy2-sumy**2))
print(r)
if abs(r) >= 0.7:
    print("Very high correlation")
elif abs(r) >= 0.5:
    print("High correlation")
elif abs(r) < 0.5 and abs(r) >= 0.3:
    print("Moderate correlation")
else:
    print("Low correlation")

a = (sumy*sumx2-sumx*sumxy)/(n*sumx2-sumx**2)
b = (n*sumxy-sumx*sumy)/(n*sumx2-sumx**2)
#print(a,b)
xc = []
yc = []

ix = min(xp)

while ix <= max(xp)+0.1:
    xc.append(ix)
    yc.append(b*ix+a)
    ix = ix + 0.1

plt.scatter(xp,yp,c='blue')
plt.plot(xc,yc,c='green')
plt.show()
