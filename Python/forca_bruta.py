"""Função força bruta em python versão 1."""

import time  # Import the 'time' module
from itertools import permutations
import numpy as np


""" Core para executar o algoritmo de força bruta."""


def forcabruta(MatrizDistTrab):
    tempoFB = time.time()
    DistMatriz = MatrizDistTrab

    VetorIndi = np.arange(1, DistMatriz.shape[0]+1)

    # Permutação dos índices das cidades
    Pi = list(permutations(VetorIndi[1:]))

    # Adicionar a cidade de partida no início de cada permutação
    Pi = np.concatenate(
        (np.ones((len(Pi), 1)), Pi, np.ones((len(Pi), 1))), axis=1)

    # Variavel da Distancia
    distanciamenor = np.inf
    distanciamaior = 0

    # Variavel da rota
    VetorDistancias = np.zeros((len(Pi), 1))
    Indice_Rota_menor = 0
    Indice_Rota_maior = 0

    # Calcula a distância de cada rota
    for i in range(len(Pi)):
        rota = Pi[i, :]  # Armazena a rota atual
        distancia = 0

        # Calcula a distância da rota atual
        for j in range(len(rota)-1):
            Cidade_partida = int(rota[j])
            Cidade_chegada = int(rota[(j + 1) % len(rota)])
            distancia = distancia + \
                DistMatriz[Cidade_partida-1, Cidade_chegada-1]

        # Armazenador de distancias
        VetorDistancias[i, 0] = distancia

        # Comparadores
        if distancia < distanciamenor:
            distanciamenor = distancia
            Indice_Rota_menor = i
        if distancia > distanciamaior:
            distanciamaior = distancia
            Indice_Rota_maior = i

    # Obtém a rota com menor distância (desconsiderando a cidade de partida duplicada)
    Rota_menor = Pi[Indice_Rota_menor, :]

    # Obtém a rota com maior distância (desconsiderando a cidade de partida duplicada)
    Rota_maior = Pi[Indice_Rota_maior, :]
    tempoFB = time.time() - tempoFB
    # Preparando a saída da função
    FB_func = {}
    FB_func['distanciamenor'] = distanciamenor
    FB_func['Indice_Rota_menor'] = Indice_Rota_menor
    FB_func['Rota_menor'] = Rota_menor
    FB_func['distanciamaior'] = distanciamaior
    FB_func['Indice_Rota_maior'] = Indice_Rota_maior
    FB_func['Rota_maior'] = Rota_maior
    FB_func['tempoFB'] = tempoFB

    return FB_func
