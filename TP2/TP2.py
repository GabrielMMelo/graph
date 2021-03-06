#!/usr/bin/env python2

import sys
import math
import copy
from random import *

INF = 9999999999999

# TODO:
''' Criar uma dict ou uma lista com a seguinte estrutura:
0: ["coord_x coord_y", flag, t_visit],
1: ["coord_x coord_y", flag, t_visit],
2: ["coord_x coord_y", flag, t_visit]. OK!

Estutura lista_dist:
0: [distancias de 0 a 105 em relacao a 0],
1: [distancias de 0 a 105 em relacao a 1]. OK!
'''

class Grafo:

	# construtor
	def __init__(self, t_total_dia, qt_hostel, qt_pontos, locais): 
		self.t_total_dia = float(t_total_dia)
		self.qt_hostel = int(qt_hostel)
		self.qt_pontos = int(qt_pontos)
		self.locais = locais
		self.lista_dist = []

	# calcula a distancia entre todos os pontos e armazena em uma estrutura
	def dist_entre_todos(self):
		lista_aux = []
		for x in range(self.qt_hostel+self.qt_pontos):
			lista_aux = []
			for y in range(self.qt_hostel+self.qt_pontos):
				dist = calcula_dist(locais[x][0], locais[y][0])
				lista_aux.append(dist)
			self.lista_dist.append(lista_aux)

# le todo o arquivo e armazena em uma estrutura
def ler_arquivo():
	nome_arquivo = sys.argv[1] 	
	arquivo = open(nome_arquivo, 'r')
	lista_linhas = arquivo.readlines()
	arquivo.close()
	return lista_linhas 

# cria a estrutura locais
def gera_caso(lista_linhas):
	temp = lista_linhas[0].split()
	qt_hostel = temp[0]
	qt_pontos = temp[1]
	t_total_dia = temp[2]
	locais_aux = []
	locais = []

	#apaga primeira linha
	del lista_linhas[0]

	for linha in lista_linhas:
		locais_aux = []
		temp = linha.split()
		if len(temp) == 3:
			locais_aux.append(temp[1] + ' ' + temp[2])
			locais_aux.append(-1)
			locais_aux.append(0)
		else:
			locais_aux.append(temp[1] + ' ' + temp[2])
			locais_aux.append(False)
			locais_aux.append(float(temp[3]))
		locais.append(locais_aux)

	return qt_hostel, qt_pontos, t_total_dia, locais

# calcula a distancia entre dois pontos
def calcula_dist(v1,v2):
	aux = v1.split()
	x1 = float(aux[0])
	y1 = float(aux[1])
	aux = v2.split()
	x2 = float(aux[0])
	y2 = float(aux[1])
	return math.sqrt((x2-x1)**2+(y2-y1)**2)

# retorna o index do ponto mais proximo a partir de um ponto
def mais_proximo(locais, lista_dist, vertice):
	flag = False
	lista_dist_aux = []
	lista_dist_aux = copy.deepcopy(lista_dist)
	for i in range(len(lista_dist_aux[vertice])):
		menor = min(lista_dist_aux[vertice])
		index = lista_dist_aux[vertice].index(menor)
		if locais[index][1] == False:
			menor = min(lista_dist_aux[vertice])
			flag = True
			break
		else:
			# Se o vertice ja foi visitado setar distancia INF
			lista_dist_aux[vertice][index] = INF
	if flag:			
		return index
	else:
		return -1

# retorna o index do hostel mais proximo
def hostel_mais_proximo(G, v_destino):
	menor = min(G.lista_dist[v_destino][:G.qt_hostel])
	index_menor = G.lista_dist[v_destino].index(menor)
	return index_menor

# verifica se um ponto e hostel
def e_hostel(G, v_destino):
	if v_destino < G.qt_hostel:
		return True

def TP2(G, inicio):
	#TODO:
	''' Percorrer o grafo partindo de um ponto qualquer, e andar para o seu vizinho
	mais proximo se o mesmo n foi visitado
	'''
	v_atual = inicio
	t_atual = 0.0
	dias = 0
	t_total = 0.0

	# enquato tiver False na estrutura locais execute
	while(False in [coluna[1] for coluna in G.locais]):
		if not e_hostel(G, v_atual):
			G.locais[v_atual][1] = True
		lista_dist_aux = []
		flag = False
		lista_dist_aux = copy.deepcopy(G.lista_dist)

		for i in range(len(G.lista_dist)):

			v_destino = mais_proximo(G.locais, lista_dist_aux, v_atual)
			if v_destino == -1:
				break
			if not e_hostel(G, v_destino):
				temp = t_atual + G.lista_dist[v_atual][v_destino] + G.locais[v_destino][2] + \
				  G.lista_dist[v_destino][hostel_mais_proximo(G, v_destino)]
				if temp <= G.t_total_dia:
				  	t_atual += G.lista_dist[v_atual][v_destino] + G.locais[v_destino][2]
				  	v_atual = v_destino
				  	flag = True
				  	break
				else:
					lista_dist_aux[v_atual][v_destino] = INF

		if not flag:
			if False in [coluna[1] for coluna in G.locais]:
				hostel_prox = hostel_mais_proximo(G, v_atual)
				t_atual += G.lista_dist[v_atual][hostel_prox]
				t_total += t_atual
				v_atual = hostel_prox
			else:
				t_atual += G.lista_dist[v_atual][inicio]
				v_atual = inicio
				t_total += t_atual
			dias += 1
			t_atual = 0
	return dias, t_total

'''def funcao_verificacao(dias, t_total, instancia):
	if instancia == "P1":

	if instancia == "P2":

	if instancia == "P3":

	if instancia == "P4":

	if instancia == "P5":

	if instancia == "P6":

	if instancia == "P7":

	if instancia == "P8":'''

if __name__ == "__main__":
	lista_linhas = ler_arquivo()
	qt_hostel, qt_pontos, t_total_dia, locais = gera_caso(lista_linhas)
	g = Grafo(t_total_dia, qt_hostel, qt_pontos, locais)
	g.dist_entre_todos()
	random = randint(0, int(qt_hostel)-1)
	dias, t_total = TP2(g, random)
	print "1 " + str(dias) + " " + str(int(t_total))
