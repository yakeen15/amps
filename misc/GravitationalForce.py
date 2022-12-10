#GravitationalForce

import math as mt


n=int(input("Total Number of Particles= ")) - 1

M=float(input("Mass of the Suspect object:"))
X=float(input("X-Coord. of the Suspect object:"))
Y=float(input("Y-Coord. of the Suspect object:"))


mass=[]
x_coord=[]
y_coord=[]
theta=[]

for i in range (n):

  print("mass of the",i+1,"st/nd/rd/th particle=")
  m=float(input())
  print("X Coord.s of the",i+1,"st/nd/rd/th particle:")
  x=float(input())
  print("Y Coord.s of the",i+1,"st/nd/rd/th particle:")
  y=float(input())

  
  mass.append(m)
  x_coord.append(x)
  y_coord.append(y)


for i in range (n):

  
  if x_coord[i]>X:

      if y_coord[i]>Y:
        t= mt.atan(abs((y_coord[i]-Y)/(x_coord[i]-X)))
        theta.append(t)

      elif y_coord[i]<Y:
        t= - mt.atan(abs((y_coord[i]-Y)/(x_coord[i]-X)))
        theta.append(t)
  
      elif y_coord[i]==Y:
        t=0
        theta.append(t)

  
  elif x_coord[i]<X:
    
      if y_coord[i]>Y:
        t= mt.pi - mt.atan(abs((y_coord[i]-Y)/(x_coord[i]-X)))
        theta.append(t)

      elif y_coord[i]<Y:
        t= mt.pi + mt.atan(abs((y_coord[i]-Y)/(x_coord[i]-X)))
        theta.append(t)

      elif y_coord[i]==Y:
        t= mt.pi
        theta.append(t)


  elif x_coord[i]==X:
      
      if y_coord[i]>Y:
        t= mt.pi/2 
        theta.append(t)
      
      elif y_coord[i]<Y:
        t= mt.pi/2 + mt.pi
        theta.append(t)

      elif y_coord[i]==Y:
        print("BEKUB KOTHAKAR!")



G=6.6743*10**(-11)

Fx=[]
Fy=[]

for i in range (n):

  fx= ((G*M*mass[i]) / ((X-x_coord[i])**2 + (Y-y_coord[i])**2)) * mt.cos(theta[i])
  fy= ((G*M*mass[i]) / ((X-x_coord[i])**2 + (Y-y_coord[i])**2)) * mt.sin(theta[i])

  Fx.append(fx)
  Fy.append(fy)


NetFx=sum(Fx)
NetFy=sum(Fy)


if (NetFx<10**(-23) and NetFy<10**(-23)):
  NetFx=0
  NetFy=0


F= mt.sqrt(NetFx**2+NetFy**2)


print("Net Force=", F) 
