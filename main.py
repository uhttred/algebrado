
# Algebrado Models
from algebrado.models.matriz import CalcMat 


A = [ [3,4,2], [3,2,4], [3,2,4] ]
B = [ [4,4,2], [7,2,4], [3,4,5] ]
C = [ [6,2,2], [6,0,4], [-32,2,4] ]
D = [ [2,6,2], [3,2,-4], [5,2,4] ]

# instacea 

my = CalcMat(C)

# adciona matriz 

my.addMatriz(A)

# Pega todas as matrizes cadastradas na instancia

print(my.getMatrizes())

# Verifica se as matrizes sao de mesma ordem

print(my.isSameOrder(A,B))

# Verifica se uma matris e de ordem x

print(my.isOrder( A, (3,3) ))