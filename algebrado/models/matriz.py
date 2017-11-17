
"""
	Resolução de exercicios base!
	return Matriz 	
"""

class Mat:

	# Matrizes

	matrizes = []

	def __init__(self, *args):

		# Pegando as matrizes
		
		if args:
			for mat in args:
				self.matrizes += [mat]

	# Retorna a determinante, Matriz 2x2

	def det2x2(self, A):

		matA = A[0][0] * A[1][1]
		matB = A[0][1] * A[1][0]

		return matA - matB

	# Soma de n Matrizes, Mesma ordem necessarias

	def soma(self, *args , islist = False):

		# Pegando a quantidade de matrizes 

		if islist:
			args = args[1]
			numMats = len(args)
		else:
			numMats = len(args)

		if numMats > 0 and self.mesmaOrdem():

			# Fazendo a matriz que sera retornada

			m = len(args[0])    # Numero de linhas
			n = len(args[0][0]) # numero de colunas

			sMat = [[0]*n]
			for i in range(m-1):
				sMat += [[0]*n]

			# Somando as matrizes

			for k in range(numMats):
				for i in range(m):
					for j in range(n):
						sMat[i][j] += args[k][i][j]

			return sMat

		else:

			# Verifica se todas as matrizes sao de mesma ordem

			if self.mesmaOrdem():
				return self.soma(self, self.matrizes, islist=True)
			return False

	# Verifica se as matrizes são de mesma ordem

	def mesmaOrdem(self, *args):
		return True




