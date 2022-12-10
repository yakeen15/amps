#PROJECTILE_Normal


import math as m
import numpy as np
import matplotlib.pyplot as mpl



#Prompt

u=float(input("Initial Valovity (m/sec)="))
ad=float(input("Angle with ground (deg)="))
ar=ad*(m.pi/180)
g=9.8
t1=float(input("t(sec)= "))


#Infos

x=u*m.cos(ar)*t1
y=u*m.sin(ar)*t1-0.5*g*(t1**2)
T=2*u*m.sin(ar)/g
H=((u**2)*((m.sin(ar))**2))/(2*g)
R=((u**2)*m.sin(2*ar))/g

print("All About Your Projectile:")
print("Horizontal displacement after t sec, X=",x,"m")
print("Vartical displacement after t sec, Y=",y,"m")
print("Total Flight Time, T=",T,"sec")
print("Max Height, H=",H,"m")
print("horizontal Range",R,"m")


#Plotting

t=np.linspace(0,T,100)
X=u*np.cos(ar)*t
Y=u*np.sin(ar)*t-0.5*g*(t**2)

mpl.title("Trajectory of The Projectile")
mpl.xlabel("Horizontal Dist")
mpl.ylabel("Vartical Dist")
mpl.grid()

mpl.plot(X,Y,linestyle="dashed",color="red")
mpl.show()
