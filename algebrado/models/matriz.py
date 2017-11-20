# -*- coding: utf8 -*-

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

		# Verificando a ordem

		if not self.isOrder( mat, (2,2) ):
			return False

		p1 = mat[0][0] * mat[1][1]
		p2 = mat[0][1] * mat[1][0]

		return p1 - p2

	# Retorna determinante, Matriz 3x3
	# >>> getDet3x3(A)

	def getDet3x3(self, mat):

		# Verificando a ordem

		if not self.isOrder(mat, (3,3)):
			return False

		p1 = ( ( mat[0][0] * mat[1][1] * mat[2][2] ) + 
			   ( mat[2][0] * mat[0][1] * mat[1][2] ) + 
			   ( mat[1][0] * mat[2][1] * mat[0][2] )
			)
		p2 = ( ( mat[2][0] * mat[1][1] * mat[0][2] ) + 
			   ( mat[1][0] * mat[0][1] * mat[2][2] ) +
			   ( mat[0][0] * mat[2][1] * mat[1][2] )
			)

		return p1 - p2

	# Multiplicar matriz por um escalar, retorna mtriz
	# >>> getMatEscalar(A,escalar)

	def getMatEscalar(self, mat, esc = 1 ):

		if not isinstance( mat, list ):
			return False

		m, n = self.getOrder(mat)

		for i in range(m):
			for j in range(n):
				mat[i][j] = esc * mat[i][j]

		return mat

	# Multiplicar duas matrizes
	# >> grtMatxMat(A,B)

	def getMatxMat(self, matA, matB):

		# Pegando a ordem das matrizes
		m, n = self.getOrder(matA)
		p, q = self.getOrder(matB)

		# Verificando se possivel fazer a operacao, Propriedade de Multiplicacao de Matrizes - Algebra Linear 
		if not( n == p ):
			return False

		# Criando a Matriz nula que sera retornada
		matC = self.getNovaMatriz( (m, q) )

		for i in range(m): # Controle da Linha na mat A e C
			for j in range(q): # Controle da coluna na mat C e B
				for k in range(p): # Controle da coluna da mat A e da linha da mat B
					# Dica Ageu Matheus >>> Levei o dia todo para bolar isso daqui! Melhor Depurar para perceber.
					if k > 0:
						matC[i][j] = matC[i][j] + ( matA[i][k] * matB[k][j] )
					else:
						matC[i][j] = matA[i][k] * matB[k][j]

		return matC

		


	# Retorna a tronsposta da matriz
	# >>> getTransposta(A)

	def getTransposta(self, mat):

		if not isinstance( mat, list ): # Verificando se e uma list
			return False

		m , n = self.getOrder(mat)

		matT = self.getNovaMatriz( (m,n) )

		for i in range(m):
			for j in range(n):
				matT[j][i] = mat[i][j]

		return matT


	# Soma de n Matrizes, Mesma ordem necessarias
	# >>> getSoma(A,B,C,..,N)
	# >>> getSoma() para somar todas as mat na instacia se de mesma ordem

	def getSoma(self, *args , islist=False):

		# Pegando a quantidade de matrizes 

		if islist:
			args = args[1]
			numMats = len(args)
		else:
			numMats = len(args)

		if numMats > 0 and self.isSameOrder(self, args, islist=True):

			# Fazendo a matriz que sera retornada

			m = len(args[0])    # Numero de linhas
			n = len(args[0][0]) # numero de colunas

			sMat = self.getNovaMatriz( (m,n) )

			# Somando as matrizes

			for k in range(numMats):
				for i in range(m):
					for j in range(n):
						sMat[i][j] += args[k][i][j]
			return sMat
		else:
			# Verifica se todas as matrizes sao de mesma ordem

			if self.isSameOrder(self, self.matrizes, islist=True):
				return self.getSoma(self, self.matrizes, islist=True)
			return False

	# Verifica se as matrizes são de mesma ordem
	# >>> isSameOrder(A,B,..,N)
	# >>> isSameOrder( [ [],[],..,[], ] islist=True)

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

	# Cria matriz e retorna uma matriz nula
	# >>> getNewMat((m, n))

	def getNovaMatriz(self, order):

		if not isinstance( order, tuple):
			return False

		newMat = [[0]*order[1]]

		for i in range( order[0] - 1 ):
			newMat += [[0]*order[1]]

		return newMat



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
