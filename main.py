# -*- coding: utf8 -*-

###
## App Para Resolução de Alguns Exercicios de Algebra Linear
#  Algebrado © Smart Technology .AO - Ageu Matheus


# Algebrado Models
from algebrado.models.matriz import CalcMat 


E = [ [3,0,3,4,5] , 
	  [2,4,3,4,5] ,
	  [2,4,3,4,5] ,
]

S = [
	
	[5,3],
	[2,4]
]

K = [ [4,2] ,
	  [1,3]
]

F = [ [2,3,-2], [1,0,-3], [4,5,2] ]
G = [ [1,-2,3], [-2,4,-6], [1,1,1] ]



# instacea 

my = CalcMat(C)

# adciona matriz 

my.addMatriz(A)

print( my.getMatxMat(S,K) )