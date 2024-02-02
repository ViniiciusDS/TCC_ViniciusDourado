"""Arquivo para método Algortimo Genético"""
import numpy as np
from Calc_func import Calc_Dist
import time


""" Função para executar o algoritmo genético """


def alggenetico(MatrizDistTrab, tam_Pop_ini, tam_gera):
    tempoAG = time.time()
    DistMatriz = MatrizDistTrab

    numCidades = len(DistMatriz)

    # Criando as variáveis para economizar memória
    Populacao = np.zeros((tam_Pop_ini, (numCidades+1)))
    FilhosPai = np.zeros((4, (numCidades+1)))
    FilhosMae = np.zeros((4, (numCidades+1)))
    nmr_filhos = np.zeros(((tam_Pop_ini-2), (numCidades+1)))
    Percurso = np.zeros((tam_Pop_ini, tam_gera))

    # Criando a população inicial
    for k in range(tam_Pop_ini):
        # cidades_aleatorias = np.random.permutation(
        #    np.arange(1, numCidades)) + 1
        cidades_aleatorias = np.random.choice(np.setdiff1d(
            np.arange(2, numCidades+1), [1]), size=numCidades-1, replace=False)

        Populacao[k, :] = np.concatenate(([1], cidades_aleatorias, [1]))

    # Calculando o percurso
    for g in range(tam_gera):
        for k in range(Populacao.shape[0]):
            Percurso[k, g] = Calc_Dist(DistMatriz, Populacao[k, :])

        # Escolhendo os mais aptos
        indices_ordenados = np.argsort(Percurso[:, g])
        menorDistancia = Percurso[indices_ordenados[0], g]
        melhorRota = Populacao[indices_ordenados[0], :]

        # Selecionando os pais
        Pai = Populacao[indices_ordenados[0], :].reshape(1, -1)
        Mae = Populacao[indices_ordenados[1], :].reshape(1, -1)

        # Definindo os filhos
        num_filhos = nmr_filhos.shape[0]

        if num_filhos % 2 == 0:
            palim = num_filhos // 2
            malim = num_filhos // 2
        else:
            escolha = np.random.randint(1, 3)
            if escolha == 1:
                palim = (num_filhos + 1) // 2
                malim = (num_filhos - 1) // 2
            else:
                palim = (num_filhos - 1) // 2
                malim = (num_filhos + 1) // 2

        # Criando os filhos por permutação
        for pa in range(palim):
            b = np.random.permutation(np.arange(1, numCidades))[:2]
            FilhosPai[pa, :] = Pai
            FilhosPai[pa, b[0]] = Pai[0, b[1]]
            FilhosPai[pa, b[1]] = Pai[0, b[0]]

        for ma in range(malim):
            b = np.random.permutation(np.arange(1, numCidades))[:2]
            FilhosMae[ma, :] = Mae
            FilhosMae[ma, b[0]] = Mae[0, b[1]]
            FilhosMae[ma, b[1]] = Mae[0, b[0]]

        #   Formando a nova população
        Populacao = np.concatenate((Pai, Mae, FilhosPai, FilhosMae))

    tempoAG = time.time() - tempoAG

    AG_Func = {}
    AG_Func['tempoAG'] = tempoAG
    AG_Func['menorDistancia'] = menorDistancia
    AG_Func['melhorRota'] = melhorRota

    return AG_Func
