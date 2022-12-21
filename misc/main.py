#PENDULUM_MOTION


import math as m
from prettytable import PrettyTable as pt


L=float(input("Length of the Pendulum (m) ="))
M=float(input("Mass of the pendulum (kg) ="))
A=float(input("Amplitude (m) ="))
x=float(input("Displacement from equilibrium (m) ="))
g=9.8


T=2*m.pi*(m.sqrt(L/g))
w=2*m.pi/T
v=w*(m.sqrt(A**2-x**2))
vmax=w*A
a=-(w**2)*x
amax=-(w**2)*A
Ek=0.5*M*(w**2)*(A**2-x**2)
Ep=0.5*M*(w**2)*(x**2)
E=Ek+Ep


tbl=pt(["Property","Numerical Value", "Unit"])

tbl.add_row(["Period",T,"sec"])
tbl.add_row(["Angular Frequency",w,"rad/sec"])
tbl.add_row(["Velocity at x",v,"m/s"])
tbl.add_row(["Max Velocity at Equilibrium",vmax,"m/s"])
tbl.add_row(["Acceleration at x",a,"m/s^2"])
tbl.add_row(["Max Acceleration at A",amax,"m/s^2"])
tbl.add_row(["Kinetic Energy at x",Ek,"J"])
tbl.add_row(["Potential Energy at x",Ep,"J"])
tbl.add_row(["Mechanical Energy at x",E,"J"])


print(tbl)



#/NayeemulHasan.0