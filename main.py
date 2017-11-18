
# Algebrado Models
from algebrado.models.matriz import Mat 


A = [ [3,4,2], [3,2,4], [3,2,4] ]
B = [ [4,4,2], [7,2,4], [3,4,5] ]
C = [ [6,4,2], [6,0,4], [-32,2,4] ]
D = [ [2,6,2], [3,2,-4], [5,2,4] ]


a = Mat(A,B)

# print(a.soma()) # Soma as matrizes instaciadas

print(a.soma(C,A)) #soma quantas matrizes forem passadas, mesma ordem necessaria

