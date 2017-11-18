
"""
	Resolução de exercicios base!
	return Matriz 	
"""

class CalcMat:

	# Matrizes

	matrizes = []

	def __init__(self, *args):

		# Pegando as matrizes
		
		if args:
			for mat in args:
				self.matrizes += [mat]

	# Retorna a determinante, Matriz 2x2 
	# >>> getDet2x2(A)

	def getDet2x2(self, mat):

		p1 = mat[0][0] * mat[1][1]
		p2 = mat[0][1] * mat[1][0]

		return p1 - p2

	# Soma de n Matrizes, Mesma ordem necessarias
	# >>> getSoma(A,B,C,..,N)
	# >>> getSoma() para somar todas as mat na instacia se de mesma ordem

	def getSoma(self, *args , islist = False):

		# Pegando a quantidade de matrizes 

		if islist:
			args = args[1]
			numMats = len(args)
		else:
			numMats = len(args)

		if numMats > 0 and self.mesmaOrdem(self, args, islist=True):

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

			if self.mesmaOrdem(self, self.matrizes, islist=True):
				return self.soma(self, self.matrizes, islist=True)
			return False

	# Verifica se as matrizes são de mesma ordem
	# >>> isSameOrder(A,B,..,N)
	# >>> isSmabeOrder( [ [],[],..,[], ] islist=True)

	def isSameOrder(self, *args, islist=False):

		# Verificnado se foram passados varios parametros ou um lista

		if islist:
			args = args[1]

		# Pegando a orderm da primeira matriz

		m = len(args[0]) 	# Linhas
		n = len(args[0][0]) # Colunas

		for k in range(len(args)):
			for i in range(len(args[k])):
				# Verificando a quantidade linhas e colunas em cada matriz
				if( len(args[k]) != n or len(args[k][i]) != m ):
					return False
		return True

	# Verifica se a matriz e da ordem passada pelo parametro order = ( linha, coluna)
	# >>> isOrder( A , ( m , n ) )

	def isOrder(self, mat, order):

		if not isinstance(mat , list) or not isinstance( order, tuple ): # Verificando se e lista e tupla
			return False

		m = order[0] # Linha
		n = order[1] # Coluna

		if len(mat) == m:
			for i in range(len(mat)): # N de linhas
				if len(mat[i]) != n: # Verificando o n de colunas em cada linha
					return False
			return True
		else: 
			return False

	# Retorna a ordem da matriz
	# >>> getOrder(A)

	def getOrder(self, mat):

		if not isinstance( mat, list ): # Verificando se e uma list
			return False

		n = len(mat[0]) # Pegando o numero de colunas na primeira linha

		for i in range(len(mat)):
			if n != len(mat[i]):
				return False

		return ( len(mat) , n ) # Retornando uma tupla m, n

	# -------------------------------------------------------------------------------

	# Eliminar matriz
	# >>> delMatriz(A)

	def delMatriz(self, mat):
		if mat in self.matrizes:
			self.matrizes.remove(mat)

	# Addcionar matrizes
	# >>> addMatriz(A)

	def addMatriz(self, mat):
		self.matrizes.append(mat)

	# Pegar todas matrizes
	# >>> getMatrizes()

	def getMatrizes(self):
		return self.matrizes





