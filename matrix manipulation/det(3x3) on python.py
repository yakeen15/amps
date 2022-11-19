#Determinant_of_3x3_Matrix_using_python



import numpy as np

#importing_entries 

a= int(input())
b= int(input())
c= int(input())
d= int(input())
e= int(input())
f= int(input())
g= int(input())
h= int(input())
i= int(input())


#defining_function

def det(mat):
     
    det = np.linalg.det(mat)
    return round(det)
 
#matrix_declaration 
  
mat = [[a, b, c],
       [d, e, f],
       [g, h, i]]
 
#calling_det_function

print('det of the matrix =', det(mat))
