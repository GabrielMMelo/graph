#!/usr/bin/env python2

import sys
import copy

def ler_arquivo():
    nome_arquivo = sys.argv[1]
    # Armazena quantidade de vertices e aresta e armazena o
    # conteudo do arquivo em uma matriz de adjacencia
    arquivo = open(nome_arquivo, 'r')

    temp = arquivo.readline().split()
    qt_vertice = int(temp[0])
    qt_aresta = int(temp[1])

    # Inicializa a matriz = 0
    ma = [[0 for i in range(qt_vertice)] for j in range(qt_vertice)]

    temp = 0
    for linha in arquivo:
        temp = temp + 1
        valores = linha.split()
        if int(valores[0]) != 0 and int(valores[1]) != 0 and temp <= qt_aresta:
            ma[ int(valores[0])-1 ][ int(valores[1])-1 ] = int(valores[2])
            ma[ int(valores[1])-1 ][ int(valores[0])-1 ] = int(valores[2])

    arquivo.close()

    # Armazena o vertice de origem e destino, e a quantidade
    # de pessoas
    arquivo = open(nome_arquivo, 'r')

    lista_linhas = arquivo.readlines()
    qt_linhas = len(lista_linhas)
    temp = lista_linhas[qt_linhas-2].split()

    v_origem = int(temp[0])
    v_destino = int(temp[1])
    qt_pessoas = int(temp[2])

    arquivo.close()

    return ma, qt_vertice, qt_aresta, v_origem, v_destino, qt_pessoas
    
class Grafo:
    def __init__(self, ma, qt_vertice, qt_aresta, v_origem, v_destino, qt_pessoas):
        self.ma = ma
        self.adj = [[] for i in range(qt_vertice)]

        # cria lista de adjacencias
        for i in range(qt_vertice):          
            for j in range(qt_vertice):
                if self.ma[i][j]!=0:
                    self.adj[i].append(j+1)

        self.qt_vertice = qt_vertice
        self.qt_aresta = qt_aresta
        self.v_origem = v_origem
        self.v_destino = v_destino
        self.qt_pessoas = qt_pessoas
        self.flag = []
        self.valor = []
        self.pi = []

        # preenche os vetores com valores padrao para iniciar a busca em largura
        for x in range(qt_vertice):      
            self.flag.append(True)
        for x in range(qt_vertice):
            self.valor.append(-1)
        for x in range(qt_vertice):
            self.pi.append(-1)

def Dijkstra(G):
	G.valor[G.v_origem-1] = 0
	while (G.flag[G.v_destino-1] != False):

        #Seleciona o vertice de maior valorancia
		maior = -1
		indice = 0
		indice_maior = 0
		for v in G.valor:
			if v > maior and G.flag[indice]:
				maior = v
				indice_maior = indice
			indice = indice + 1
		u = indice_maior

		G.flag[u] = False
		adjAux = []
		adjAux = copy.deepcopy(G.adj[u])

		for i in range(len(G.adj[u])):
			#Pega o vertice adjacente de maior peso de aresta
			maior = 0
			indice_maior
			for v in adjAux:
				if (G.ma[u][v-1] > maior):
					indice_maior = v
			v = indice_maior
			adjAux.remove(v)

			#Caso esteja na primeira iteracao, onde estamos no vertice de origem
			if u == (G.v_origem - 1):
    				G.valor[v-1] =  G.ma[u][v-1]
    				G.pi[v-1] = u+1

			else:
				# Se o peso para vertice adjacente for maior do que o valor do vertice atual 
				if (G.flag[v-1]) and (G.ma[u][v-1] >= G.valor[u]):
					if(G.valor[v-1] < G.valor[u]):
						G.valor[v-1] =  G.valor[u]
						G.pi[v-1] = u+1
				# Se o peso para vertice adjacente for menor do que o valor do vertice atual 
				elif (G.flag[v-1]) and (G.ma[u][v-1] < G.valor[u]):
					if G.valor[v-1] < G.ma[u][v-1]:
						G.valor[v-1] = G.ma[u][v-1]
						G.pi[v-1] = u+1
	total = G.qt_pessoas
	contador = 0
	while total > 0:
		total = total - (G.valor[v_destino-1]-1)
		contador = contador + 1
	print ("Minimo de viagens = " + str(contador))
	caminho = []
	aux = G.v_destino
	while aux != G.v_origem:
		caminho.append(aux)
		aux = G.pi[aux-1]
	caminho.append(G.v_origem)
	caminho.reverse()
	sys.stdout.write('Caminho: ')
	for x in range(len(caminho)-1):
		sys.stdout.write(str(caminho[x]) + '-' )
	sys.stdout.write(str(caminho[len(caminho)-1]))
	print

if __name__ == "__main__":
    ma, qt_vertice, qt_aresta, v_origem, v_destino, qt_pessoas = ler_arquivo()
    g = Grafo(ma, qt_vertice, qt_aresta, v_origem, v_destino, qt_pessoas)
    Dijkstra(g)
