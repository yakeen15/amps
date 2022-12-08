import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as stats
import math
sum=0
sum2 = 0
data = []
n = int(input("Please enter the number of data in the data set: "))
print("Please enter the data one by one as follows: \n")
for i in range(0,n):
    x=int(input())
    data.append(x)
for i in range(0,n):
    sum = sum + data[i]
mean = sum/n
for i in range (0,n):
    sum2 = sum2 + (data[i]-mean)**2
variance = sum2/(n-1)
sd = math.sqrt(variance)
x = np.linspace(mean - 3 * sd, mean + 3 * sd, 100)
plt.plot(x, stats.norm.pdf(x, mean, sd))
plt.show()
