#!/usr/bin/env python2

# Leitura e geracao de multiplos casos (X)
# DFS (X)
# Djikstra (X)
# Intersecao ()
# Calculo do segundo mais proximo (X)
# Calcular a distancia somente apos tratamento da intersecao ()
# Add vertices no grafo 

import sys
import math
import datetime
import copy

class Grafo():
	def __init__(self):
		self.vertices = {}
		self.deposito = ""
	
	def deposito_coincide_rua(self):
		if self.deposito in self.vertices:
			return True
		else:
			return False

	def dois_mais_prox_deposito(self):
		menor1 = 999999999
		menor2 = 999999999
		v1proximo = ""
		v2proximo = ""

		d = G.vertices.iterkeys()
		for i in range(len(self.vertices)-1):
			v = d.next()
			if menor1 > calcula_dist(self.deposito, v):
				menor1 = calcula_dist(self.deposito, v)
				v1proximo = v
		d = G.vertices.iterkeys()
		for i in range(len(self.vertices)-1):
			v = d.next()
			if menor2 > calcula_dist(self.deposito, v) and v != v1proximo:
				menor2 = calcula_dist(self.deposito, v)
				v2proximo = v
		return menor1, v1proximo, menor2, v2proximo

	def resolve_intersecoes(self):
		cont = 1
		for i in self.vertices.keys():
			split1 = i.split()
			for j in self.vertices[i]:
				split2 = j[0].split()
				cont_aux = cont
				for k in self.vertices.keys():
					if cont_aux>0:
						cont_aux -= 1
						continue
					split3 = k.split()
					for l in self.vertices[k]:
						split4 = l[0].split()
						#TODO: PENSAR ESSAS CONDICOES
#						if split1[0] != split3[0] and split1[0] != split3[1] and split1[1] != split3[0] and split1[1] != split3[1] \
#						or split1[0] == split3[0] and split1[1] != split3[1] or split1[1] == split3[0] and split1[1] != split3[1] \
#						or split1[0] == split3[1] and split1[1] != split3[0] or split1[1] == split3[1] and split1[0] != split3[0] \
#						and split1[0] != split4[0] and split1[0] != split4[1] and split1[1] != split4[0] and split1[1] != split4[1] \
#						or split1[0] == split4[0] and split1[1] != split4[1] or split1[1] == split4[0] and split1[1] != split4[1] \
#						or split1[0] == split4[1] and split1[1] != split4[0] or split1[1] == split4[1] and split1[0] != split4[0] \
#						and split2[0] != split3[0] and split2[0] != split3[1] and split2[1] != split3[0] and split2[1] != split3[1] \
#						or split2[0] == split3[0] and split2[1] != split3[1] or split2[1] == split3[0] and split2[1] != split3[1] \
#						or split2[0] == split3[1] and split2[1] != split3[0] or split2[1] == split3[1] and split2[0] != split3[0] \
#						and split2[0] != split4[0] and split2[0] != split4[1] and split2[1] != split4[0] and split2[1] != split4[1] \
#						or split2[0] == split4[0] and split2[1] != split4[1] or split2[1] == split4[0] and split2[1] != split4[1] \
#						or split2[0] == split4[1] and split2[1] != split4[0] or split2[1] == split4[1] and split2[0] != split4[0]:
						intersecao = []
						intersecao = self.get_intersecao(int(split1[0]),int(split1[1]),int(split2[0]),int(split2[1]),int(split3[0]),int(split3[1]),int(split4[0]),int(split4[1]))
						if intersecao:
							novaKey = str(int(intersecao[0])) + " " + str(int(intersecao[1]))
							if not novaKey in self.vertices:
								self.vertices[novaKey] = [[split1[0]+ " " + split1[1], 1],[split2[0]+ " " + split2[1],1],[split3[0]+ " " + split3[1],1],[split4[0]+ " " + split4[1],1]]
								self.vertices[split1[0]+ " " + split1[1]] #.remove(split2[0]+ " " + split2[1])
								self.vertices[split1[0]+ " " + split1[1]] #.add([novaKey,1])
								self.vertices[split2[0]+ " " + split2[1]] #.remove(split1[0]+ " " + split1[1])
								self.vertices[split2[0]+ " " + split2[1]] #.add([novaKey,1])
								self.vertices[split3[0]+ " " + split3[1]] #.remove(split4[0]+ " " + split4[1])
								self.vertices[split3[0]+ " " + split3[1]] #.add([novaKey,1])
								self.vertices[split4[0]+ " " + split4[1]] #.remove(split3[0]+ " " + split3[1])
								self.vertices[split4[0]+ " " + split4[1]] #.add([novaKey,1])

						else:
							print "nao achou"
			cont += 1
		return self

	#Retorna as coordenadas de intersecao entre dois segmentos de reta
	def get_intersecao(self,k1,k2,l1,l2,m1,m2,n1,n2):
		d = float((n1 - m1) * (l2 - k2)  -  (n2 - m2) * (l1 - k1))
		if (d == 0.0):
			return False
		s = ((n1 - m1) * (m2 - k2) - (n2 - m2) * (m1 - k1)) / d
		t = ((l1 - k1) * (m2 - k2) - (l2 - k2) * (m1 - k1)) / d
		x = k1 + (l1-k1)*s
		y = k2 + (l2-k2)*s
		return x,y


def ler_arquivo():
	nome_arquivo = sys.argv[1]

	arquivo = open(nome_arquivo, 'r')
	caso = arquivo.readline()
	arquivo.readline()
	lista_linhas = arquivo.readlines()

	arquivo.close()

	return lista_linhas, caso

def calcula_dist(v1,v2):
	aux = v1.split()
	x1 = float(aux[0])
	y1 = float(aux[1])
	aux = v2.split()
	x2 = float(aux[0])
	y2 = float(aux[1])
	return math.sqrt((x2-x1)**2+(y2-y1)**2)

def gera_caso(lista_linhas, pos):
	#TODO: SUPORTAR MULTIPLOS CASOS
	G = Grafo()
	G.deposito = lista_linhas[pos].replace('\n', '')
	#G.vertices[G.deposito] = []

	for i in range(pos, len(lista_linhas)):
		if len(lista_linhas[i].split()) == 4: # testa se eh uma linha do arquivo com coordenadas
			temp = lista_linhas[i].split()
			aux = temp[0] + " " + temp[1] # junta 1a coordenada
			aux2 = temp[2] + " " + temp[3] # junta 2a coordenada
			if aux not in G.vertices and aux2 not in G.vertices:
				G.vertices[aux] = [[aux2,0]]
				G.vertices[aux2] = [[aux,0]]
			elif aux not in G.vertices:
				dictAux = G.vertices[aux2] 
				dictAux.append([aux,0])
				G.vertices[aux] = [[aux2,0]]
				
			elif aux2 not in G.vertices:
				dictAux = G.vertices[aux] 
				dictAux.append([aux2,0])
				G.vertices[aux2] = [[aux,0]]
			else:
				dictAux = G.vertices[aux] 
				dictAux.append([aux2,0])
				dictAux = G.vertices[aux2] 
				dictAux.append([aux,0])

		elif i > pos and len(lista_linhas[i].split()) == 2:
			pos = i
			break
		armazena_dist(G)
		G.resolve_intersecoes()
	return pos, G

# guarda as distancias das coordenadas adjacentes no dict
def armazena_dist(G):
	for chave, val in G.vertices.items():
		for c in val:
			c[1] = calcula_dist(chave, c[0])

# soma todas as distancias 
def soma_dists(G):
	soma = 0
	for chave, val in G.vertices.items():
		for c in val:
			soma += c[1]
	return soma

def DFS(G):
	global cycle
	cycle = []
	dict_aux = copy.deepcopy(G.vertices)
	for i in dict_aux.keys():		
		dict_aux[i].append("branco")
	for i in dict_aux.keys():
		dict_aux[i].append(-1)
	flag = False
	dict_aux[G.deposito][len(dict_aux[G.deposito])-1] = -2
	DFS_VISIT(dict_aux, G.deposito, flag, G.deposito)
	for chave in dict_aux.keys():
		if dict_aux[chave][len(dict_aux[chave])-2] == "branco" and len(dict_aux[chave])-2 > 0:
			DFS_VISIT(dict_aux, 
				chave, flag, G.deposito)
#	cycle.append(G.deposito)

def DFS_VISIT(vertices, chave, flag, inicio):
	vertices[chave][len(vertices[chave])-2] = "cinza"
	cycle.append(chave)

	for v in range(len(vertices[chave])-2):
		# Se o V for o INICIO e o PI de CHAVE nao eh INICIO
		if vertices[ vertices[chave][v][0] ][ len(vertices[vertices[chave][v][0]])-1 ] != -1 and \
		vertices[ chave ][ len(vertices[chave])-1 ] != inicio and vertices[chave][v][0] == inicio:
			cycle.append(inicio)
			flag = True

		# Se a COR do vertice V adjacente a CHAVE for == BRANCO
		if vertices[ vertices[chave][v][0] ][ len(vertices[vertices[chave][v][0]])-2 ] == "branco":
			# PI do vertice V adjacente a CHAVE = CHAVE
			vertices[ vertices[chave][v][0] ][ len(vertices[vertices[chave][v][0]])-1 ] = chave
			DFS_VISIT(vertices, vertices[chave][v][0], flag, inicio)
			continue

		if flag:
			cycle.append(chave)

	# Forma o caminho inverso da busca, gerando o ciclo completo
	if vertices[chave][ len(vertices[chave])-1 ] != -2:
		cycle.append(vertices[chave][ len(vertices[chave])-1 ])
		
	vertices[chave][len(vertices[chave])-2] = "preto"

def hierholzer(G):
	new_cycle = []
	DFS(G)
	print cycle
	new_cycle += cycle
	vertices_aux = copy.deepcopy(G.vertices)
	cont = 0
	for i in cycle:
		auxSoma = 0
		for j in range(len(vertices_aux[i])):
			if cont == len(cycle)-2 and j == len(vertices_aux[i])-1:
				if vertices_aux[i][j-auxSoma][0] == cycle[cont+1]:
					vertices_aux[i].pop(j)
					auxSoma +=1
				break
			elif vertices_aux[i][j-auxSoma][0] == cycle[cont+1]:
				vertices_aux[i].pop(j)
				auxSoma +=1
				print vertices_aux
		cont += 1
	print vertices_aux
	return new_cycle

def djikstra(vertices, origem, destino):
	dict_aux = copy.deepcopy(vertices)
	for i in dict_aux.keys():
		dict_aux[i].append(True)
	for i in dict_aux.keys():
		dict_aux[i].append(999999999)
	for i in dict_aux.keys():
		dict_aux[i].append('-1')

	#dist = 0
	dict_aux[origem][len(dict_aux[origem])-2] = 0

	# enquanto a flag for false
	while(dict_aux[destino][len(dict_aux[destino])-3] != False):
		menor = 999999999

		#pega menor distancia e o indice
		for k in dict_aux.keys():
			if dict_aux[k][len(dict_aux[k])-2] < menor and dict_aux[k][len(dict_aux[k])-3]:
				menor = dict_aux[k][len(dict_aux[k])-2]
				k_menor = k
		u = k_menor

		#flag = False
		dict_aux[u][len(dict_aux[u])-3] = False

		# percorre os vertices adjacentes
		for v in range(len(dict_aux[u])-3):
			if dict_aux[dict_aux[u][v][0]][len(dict_aux[dict_aux[u][v][0]])-3] and \
			dict_aux[dict_aux[u][v][0]][len(dict_aux[dict_aux[u][v][0]])-2] >   \
			dict_aux[u][len(dict_aux[u])-2] + dict_aux[u][v][1]:
				dict_aux[dict_aux[u][v][0]][len(dict_aux[dict_aux[u][v][0]])-2] = \
				dict_aux[u][len(dict_aux[u])-2] + dict_aux[u][v][1]
				dict_aux[dict_aux[u][v][0]][len(dict_aux[dict_aux[u][v][0]])-1] = u
	
	x = destino
	caminho = []
	while x != origem:
		caminho.append(x)
		x = dict_aux[x][len(dict_aux[x])-1]
	caminho.append(origem)
	caminho = caminho[::-1]
	print caminho

	#return dict_aux[destino][len(dict_aux[destino])-1]


def p2(G):
	# se for eureliano
	if G.deposito_coincide_rua:
		seg = soma_dists(G) / (20000.0/3600.0)			#  ARRUMAR
		print str(datetime.timedelta(seconds=int(seg)))
	else:
		pass

if __name__ == "__main__":
	#TODO: FAZER FOR PARA OS CASOS
	pos = 0
	lista_linhas, caso = ler_arquivo()
	for i in range(int(caso)):
		pos, G = gera_caso(lista_linhas, pos)
	#	print G.vertices
#		print G.deposito
	#print G.dois_mais_prox_deposito()
	#DFS(G)
	#djikstra(G.vertices,"0 0", "25000 5000")
	#print cycle
	#dijkstra(G.vertices, '0 0', '0 0')
	#if G.deposito_coincide_rua():
	#	print "TRUE"
	#print calcula_dist("0 0","1 1")
	#hierholzer(G)
	#print cycle