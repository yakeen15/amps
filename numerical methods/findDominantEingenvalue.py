import numpy as np

#Shajiratul Yaqueen
#AMTH batch 6
#Purpose : Finds the dominant eigenvalue of a matrix if there exists one
#Inputs : Size of matrix n, each entry in the matrix, number of iterations
#Outputs : Approximate eigenvector and eigenvalue at each iteration

def rq(a,x):
    return a.dot(x).dot(x) / x.dot(x)

print("Dimension of square matrix?")
n = int(input(''))

mat = []
for k in range(0,n):
    rows = []
    for i in range(0,n):
        print("Enter ("+str(i)+','+str(k)+") value")
        rows.append(float(input('')))
    mat.append(rows)

a = np.array(mat)
print(a)

x = []
for i in range(0,n):
    x.append(1.0)
x = np.array(x)


print("How many iterations?")
itr = int(input(''))

for i in range(0,itr):
    print("Iteration "+str(itr))
    print("Eigenvector")
    x = a.dot(x)
    print(x/x.max())
    print("Eigenvalue")
    print(rq(a,x))

