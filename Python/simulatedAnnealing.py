import numpy as np
import time


def simulated_annealing(matriz_distancia, temperatura_inicial, taxa_resfriamento, num_iteracoes):
    tempo_sa = time.time()
    num_cidades = matriz_distancia.shape[0]

    # Gera a solução inicial aleatória
    cidades_aleatorias = np.random.permutation(np.arange(2, num_cidades+1))
    # Solução inicial aleatória
    melhor_rota = np.concatenate(([1], cidades_aleatorias, [1]))
    melhor_custo = calcular_custo_rota(melhor_rota, matriz_distancia)

    # Variáveis para parâmetro de comparação
    rota_atual = melhor_rota.copy()
    custo_atual = melhor_custo

    for iteracao in range(num_iteracoes):
        # Gera uma nova solução vizinha alterando aleatoriamente a solução atual
        nova_rota = gerar_nova_rota_vizinha(rota_atual)
        novo_custo = calcular_custo_rota(nova_rota, matriz_distancia)

        # Calcula a diferença de custo entre a nova solução e a solução atual
        delta_custo = novo_custo - custo_atual

        # Aceita a nova solução se ela for melhor ou com uma certa probabilidade se for pior
        if delta_custo < 0 or np.random.rand() < np.exp(-delta_custo / temperatura_inicial):
            rota_atual = nova_rota.copy()
            custo_atual = novo_custo

            # Atualiza a melhor solução encontrada
            if custo_atual < melhor_custo:
                melhor_rota = rota_atual
                melhor_custo = custo_atual

        # Atualiza a temperatura
        temperatura_inicial *= taxa_resfriamento

    # tempo_sa = time.process_time()
    tempo_sa = time.time() - tempo_sa

    # Preparando a saída da função
    sa_func = {}
    sa_func['tempo'] = tempo_sa
    sa_func['menorDistancia'] = melhor_custo
    sa_func['melhorRota'] = melhor_rota

    return sa_func


def calcular_custo_rota(rota, matriz_distancia):
    # Calcula o custo total da rota
    custo = 0
    num_cidades = len(rota)

    for i in range(num_cidades):
        cidade_atual = rota[i]
        # Próxima cidade considerando rota circular
        cidade_proxima = rota[(i+1) % num_cidades]
        custo += matriz_distancia[cidade_atual-1, cidade_proxima-1]

    return custo


def gerar_nova_rota_vizinha(rota_atual):
    # Gera uma nova solução vizinha alterando aleatoriamente a solução atual
    num_cidades = len(rota_atual)
    indice1, indice2 = np.random.choice(range(1, num_cidades-1), 2, replace=False)
    nova_rota = rota_atual.copy()
    # Troca duas cidades aleatoriamente
    nova_rota[[indice1, indice2]] = nova_rota[[indice2, indice1]]

    return nova_rota
