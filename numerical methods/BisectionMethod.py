#BisectionMethod


#e**x − x**2 + 3x − 2 = 0    ; for 0 ≤ x ≤ 1
#2x cos(2x) − (x + 1)**2 = 0 ; for −3 ≤ x ≤ −2
#x cos x − 2x**2 + 3x − 1 = 0; for 0.2 ≤ x ≤ 0.3

import math as m


l=float(input("Lower Boundary:"))
u=float(input("Upper Boundary:"))


#FUNC. DEFINING

def f(x):
    f = m.e**x -x**2 +3*x - 2                                                 ####### define other f(x)s
    #f=2*x*m.cos(2*x) - (x+1)**2                                              #They'r here just for TestRide
    #f= x * m.cos(x) - 2*x**2 + 3*x -1
    return f


#DHONG

if f(l)*f(u)<0:
    print("There exists at least one root in the closed interval","[",l,",",u,"]")
else:
    print("Ja, Vaag!")


#n(ITTERATION)

d=int(input("result need to be accurate within ? decimal place:"))
t=10**(-d)

n=m.ceil((m.log10(u-l)-m.log10(t))/m.log10(2))
print(" ")
print("We'll need",n,"iterations;")


#MechaParts

for i in range(n):

    p=(u+l)/2

    if f(l)<0:

        if f(p)*f(l)<0:
            u=p
        elif f(p)*f(l)>0:
            l=p

    elif f(l)>0:

        if f(p)*f(l)<0:
            u=p
        elif f(p)*f(l)>0:
            l=p

    elif f(u)<0:

        if f(p)*f(u)<0:
            l=p
        elif f(p)*f(u)>0:
            u=p

    elif f(u)>0:

        if f(p)*f(u)<0:
            l=p
        elif f(p)*f(u)>0:
            u=p




print("And our desired root is:",p)



#/NayeemulHasan.0
