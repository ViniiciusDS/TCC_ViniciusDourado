"""Funcao Busca exaustiva em python versao 1."""

import time  # Import the 'time' module
from itertools import permutations
import numpy as np


""" Core para executar o algoritmo de Busca exaustiva."""


def buscaexaustiva(MatrizDistTrab):
    tempoBE = time.time()
    DistMatriz = MatrizDistTrab

    VetorIndi = np.arange(1, DistMatriz.shape[0]+1)

    # Permutacao dos indices das cidades
    Pi = list(permutations(VetorIndi[1:]))

    # Adicionar a cidade de partida no inicio de cada permutacao
    Pi = np.concatenate(
        (np.ones((len(Pi), 0)), Pi, np.ones((len(Pi), 0))), axis=1)

    # Variavel da Distancia
    distanciamenor = np.inf
    distanciamaior = 0

    # Variavel da rota
    VetorDistancias = np.zeros((len(Pi), 1))
    Indice_Rota_menor = 0
    Indice_Rota_maior = 0

    # Calcula a distancia de cada rota
    for i in range(len(Pi)):
        rota = Pi[i, :]  # Armazena a rota atual
        distancia = 0

        # Calcula a distancia da rota atual
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

    # Obtem a rota com menor distancia (desconsiderando a cidade de partida duplicada)
    Rota_menor = Pi[Indice_Rota_menor, :]

    # Obtem a rota com maior distancia (desconsiderando a cidade de partida duplicada)
    Rota_maior = Pi[Indice_Rota_maior, :]
    tempoBE = time.time() - tempoBE
    # Preparando a saida da funcao
    BE_func = {}
    BE_func['distanciamenor'] = distanciamenor
    BE_func['Indice_Rota_menor'] = Indice_Rota_menor
    BE_func['Rota_menor'] = Rota_menor
    BE_func['distanciamaior'] = distanciamaior
    BE_func['Indice_Rota_maior'] = Indice_Rota_maior
    BE_func['Rota_maior'] = Rota_maior
    BE_func['tempoBE'] = tempoBE

    return BE_func
