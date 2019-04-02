# coding: utf-8
import time, copy, random, math, sys, numpy as np

class Nodo:
	def __init__(self, tabuleiro, nivel):
		self.tab = tabuleiro
		self.cima = None
		self.baixo = None
		self.esq = None
		self.dir = None
		self.pai = None
		self.nivel = nivel
		self.h1 = pecasErradas(self.tab) #valor da heurística 1 (número de peças fora do lugar)
		self.h2 = distanciaManhattan(self.tab) #valor da heurística 2
		self.movimento = -1 #0 = cima 1 = baixo 2 = esquerda 3 = direita

	def visitaNodo(self, nivel): #abre o nodo (gera seus nodos filhos)
		
		x, y = np.where(self.tab == 0)

		x = x[0]
		y = y[0]

		if(x != 0 and self.movimento != 1):
			self.cima = Nodo(move(self.tab.copy(), self.tab[x-1][y]), self.nivel+1)
			self.cima.pai = self
			self.cima.movimento = 0
		if(x != (len(self.tab)-1) and self.movimento != 0):
			self.baixo = Nodo(move(self.tab.copy(), self.tab[x+1][y]), self.nivel+1)
			self.baixo.pai = self
			self.baixo.movimento = 1
		if(y != 0 and self.movimento != 3):
			self.esq = Nodo(move(self.tab.copy(), self.tab[x][y-1]), self.nivel+1)
			self.esq.pai = self
			self.esq.movimento = 2
		if(y != (len(self.tab)-1) and self.movimento != 2):
			self.dir = Nodo(move(self.tab.copy(), self.tab[x][y+1]), self.nivel+1)
			self.dir.pai = self
			self.dir.movimento = 3

def geraTabuleiro(n): #n é a proporção do tabuleiro (n = 3 irá gerar um tabuleiro 3x3, por exemplo).

	tabuleiro = np.zeros([n, n], int) #Inicia matriz de 0s
	cont = 1
	for i in range (0, n):
		for j in range (0, n):
			tabuleiro[i][j] = cont #Preenche com os valores
			cont += 1
	tabuleiro[n-1][n-1] = 0 #Define o último elemento como o espaço vazio (0)
	return tabuleiro

def embaralhaTabuleiro(t, n):

	for i in range(0, n):
		#random.seed(15)
		escolha = random.randint(1, 4)
		x, y = np.where(t == 0)
		x = x[0]
		y = y[0]
		if (escolha == 1):
			if(x != 0): #se não estiver na primeira linha, pode ir pra cima
				t = move(t, t[x-1][y])
		elif (escolha == 2):
			if(x != (len(t)-1)):
				t = move(t, t[x+1][y])
		elif (escolha == 3):
			if(y != 0):
				t = move(t, t[x][y-1])
		elif (escolha == 4):
			if(y != (len(t)-1)):
				t = move(t, t[x][y+1])
	return t

def move(t, v):

	p1, p2 = np.where(t == 0)
	p3, p4 = np.where(t == v)
	t[p1[0]][p2[0]] = v
	t[p3[0]][p4[0]] = 0
	return t

def printaCaminho(n):

	print('Caminho percorrido pelo espaço vazio (do estado final ao inicial): ')
	while(n.pai != None):
		#print(n.tab)
		if(n.movimento == 0):
			print('↑')
		if(n.movimento == 1):
			print('↓')
		if(n.movimento == 2):
			print('←')
		if(n.movimento == 3):
			print('→')
		n = n.pai
	if(n.movimento == 0):
		print('↑')
	if(n.movimento == 1):
		print('↓')
	if(n.movimento == 2):
		print('←')
	if(n.movimento == 3):
		print('→')

def pecasErradas(t):

	resultado = geraTabuleiro(int(math.sqrt(t.size)))
	return (t.size - (np.sum(t == resultado)))

def distanciaManhattan(t):

	distManhattan = 0
	resultado = geraTabuleiro(int(math.sqrt(t.size)))

	for i in range(0, int(math.sqrt(t.size))):
		for j in range(0, int(math.sqrt(t.size))):
			n = t[i][j]
			x, y = np.where(resultado == n)
			x = x[0]
			y = y[0]
			distManhattan += abs(i-x) + abs(j-y)

	return distManhattan

def largura(t):

	tempoInicio = time.time()

	arrayNodos = []
	contadorNodos = 0 #número de nodos visitados

	raiz = Nodo(t, 0) #inicializa a raíz
	arrayNodos.append(raiz)

	final = geraTabuleiro(int(math.sqrt(t.size))) #resultado final a ser achado

	while(arrayNodos): #percorre todo vetor
		raiz = arrayNodos.pop(0)
		contadorNodos += 1
		if(np.array_equal(raiz.tab, final)):
			tempoFinal = time.time()
			print ('A busca em largura demorou ', (tempoFinal - tempoInicio), ' segundos e visitou ', contadorNodos, ' nodos.')
			printaCaminho(raiz)
			return
		else:
			raiz.visitaNodo(raiz.nivel)
			if(raiz.cima != None):
				arrayNodos.append(raiz.cima)
			if(raiz.baixo != None):
				arrayNodos.append(raiz.baixo)
			if(raiz.esq != None):
				arrayNodos.append(raiz.esq)
			if(raiz.dir != None):
				arrayNodos.append(raiz.dir)
				
def profundidade(t):
	
	tempoInicio = time.time()

	arrayNodos = []
	contadorNodos = 0

	raiz = Nodo(t, 0)
	arrayNodos.append(raiz)

	final = geraTabuleiro(int(math.sqrt(t.size)))

	while(arrayNodos):
		raiz = arrayNodos.pop(0)
		contadorNodos += 1
		if(np.array_equal(raiz.tab, final)):
			tempoFinal = time.time()
			print('A busca em profundidade demorou ', (tempoFinal - tempoInicio), ' segundos e visitou ', contadorNodos, ' nodos.')
			printaCaminho(raiz)
			return
		else:
			raiz.visitaNodo(raiz.nivel)
			if(raiz.cima != None):
				arrayNodos.append(raiz.cima)
			if(raiz.baixo != None):
				arrayNodos.append(raiz.baixo)
			if(raiz.esq != None):
				arrayNodos.append(raiz.esq)
			if(raiz.dir != None):
				arrayNodos.append(raiz.dir)

def profundidadeIterativa(t):
	
	tempoInicio = time.time()

	arrayNodos = []
	contadorNodos = 0
	limite = 0

	raiz = Nodo(t, 0)
	raizdef = copy.copy(raiz)
	arrayNodos.append(raiz)

	final = geraTabuleiro(int(math.sqrt(t.size)))

	if(math.sqrt(t.size) == 3):
		limiteMax = 31 #limite maximo de profundidade pra 3x3
	else:
		limiteMax = 100 #?

	while(limite < limiteMax): #31 é o número máximo de níveis para encontrar uma solução ótima (no tabuleiro 3x3)
		while(arrayNodos):
			raiz = arrayNodos.pop(0)
			contadorNodos += 1
			if(np.array_equal(raiz.tab, final)):
				tempoFinal = time.time()
				print('A busca em profundidade iterativa demorou ', (tempoFinal - tempoInicio), ' segundos e visitou ', contadorNodos, ' nodos em ', limite+1, ' níveis.')
				printaCaminho(raiz)
				return
			else:
				if(raiz.nivel <= limite):
					raiz.visitaNodo(raiz.nivel)
					if(raiz.cima != None):
						arrayNodos.append(raiz.cima)
					if(raiz.baixo != None):
						arrayNodos.append(raiz.baixo)
					if(raiz.esq != None):
						arrayNodos.append(raiz.esq)
					if(raiz.dir != None):
						arrayNodos.append(raiz.dir)
		arrayNodos.append(raizdef) #array já vai ter esvaziado, bota de volta a primeira raíz
		limite += 1
		contadorNodos = 0

	return

def aEstrela(t, h): #h = heurística (1 - número de peças fora do lugar, 2 - distância de manhattan)
	
	tempoInicio = time.time()

	arrayNodos = []
	contadorNodos = 0

	raiz = Nodo(t, 0)
	arrayNodos.append(raiz)

	final = geraTabuleiro(int(math.sqrt(t.size)))

	while(arrayNodos):
		if(np.array_equal(raiz.tab, final)):
			tempoFinal = time.time()
			if(h == 1):
				print ('A busca A* com a heurística 1 demorou ', (tempoFinal - tempoInicio), ' segundos e visitou ', contadorNodos, ' nodos.')
			if(h == 2):
				print ('A busca A* com a heurística 2 demorou ', (tempoFinal - tempoInicio), ' segundos e visitou ', contadorNodos, ' nodos.')
			printaCaminho(raiz)
			return
		else:	
			if(h == 1):
				arrayNodos.sort(key=heuristicaMenor1)
			if(h == 2):
				arrayNodos.sort(key=heuristicaMenor2)
			raiz = arrayNodos.pop(0)
			raiz.visitaNodo(raiz.nivel)
			contadorNodos += 1
			if(raiz.cima != None):
				arrayNodos.append(raiz.cima)
			if(raiz.baixo != None):
				arrayNodos.append(raiz.baixo)
			if(raiz.esq != None):
				arrayNodos.append(raiz.esq)
			if(raiz.dir != None):
				arrayNodos.append(raiz.dir)

def heuristicaMenor1(t):

	return t.h1 + t.nivel

def heuristicaMenor2(t):

	return t.h2 + t.nivel

def main(busca, tamanho, embaralhamento):

	t = geraTabuleiro(int(tamanho))
	t = embaralhaTabuleiro(t.copy(), int(embaralhamento))
	if(busca == '0'):
		largura(t)
	elif(busca == '1'):
		profundidade(t)
	elif(busca == '2'):
		profundidadeIterativa(t)
	elif(busca == '3'):
		aEstrela(t, 1)
	elif(busca == '4'):
		aEstrela(t, 2)
	else:
		print("Algoritmo não existe! Tente novamente")

main(sys.argv[1], sys.argv[2], sys.argv[3]) #sys.argv[1] = tipo de busca; sys.argv[2] = tamanho do tabuleiro; sys.argv[3] = nível de embaralhamento
