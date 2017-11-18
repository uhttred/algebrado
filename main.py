
# Algebrado Models
from algebrado.models.matriz import CalcMat 


A = [ [3,4,2], [3,2,4], [3,2,4] ]
B = [ [4,4,2], [7,2,4], [3,4,5] ]
C = [ [6,2,2], [6,0,4], [-32,2,4] ]
D = [ [2,6,2], [3,2,-4], [5,2,4] ]
E = [ [3,4] , [5,6] ]
F = [ [2,3,-2], [1,0,-3], [4,5,2] ]
G = [ [1,-2,3], [-2,4,-6], [1,1,1] ]

# instacea 

my = CalcMat(C)

# adciona matriz 

my.addMatriz(A)

print(my.getDet2x2(A))
print(my.getDet3x3(G))