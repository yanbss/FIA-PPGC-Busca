# FIA-PPGC-Busca
Trabalho sobre algoritmos de busca realizado na cadeira de Fundamento de Inteligência Artificial do PPGC da UFPel.

Modo de utilização:

python buscas.py arg1 arg2 arg3

arg1 = Tipo de busca:
	0 -> Busca em Largura
	1 -> Busca em Profundidade
	2 -> Busca em Profundidade Iterativa
	3 -> Algoritmo A* com heurística de número de peças em lugar errado
	4 -> Algoritmo A* com heurística de Distância de Manhattan

arg2 = Tamanho do tabuleiro:
	3 -> Tabuleiro 3x3
	4 -> Tabuleiro 4x4
	... (aceita qualquer tamanho, porém apenas os tabuleiros 3x3 e 4x4 têm uma solução garantida sem estouro de memória)

arg3 = Nível de embaralhamento:
	10 -> Embaralhado 10 vezes
	100 -> Embaralhado 100 vezes
	... (aceita qualquer valor e garante um problema solucionável)
