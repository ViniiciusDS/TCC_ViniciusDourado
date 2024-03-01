"""Código main do TCC, afim de realizar testes estatísticos e gráficos"""
# import sys  # Importar a biblioteca sys para obter argumentos de linha de comando
import numpy as np  # Importar a biblioteca numpy
import pandas as pd  # Importar a biblioteca pandas
import matplotlib.pyplot as plt  # Importar a biblioteca matplotlib
from scipy.stats import ttest_rel  # Importar a função ttest_rel
from forca_bruta import forcabruta  # Importar a função forcabruta
from alggenetico import alggenetico  # Importar a função alggenetico
# Importar a função simulatedAnnealing
from simulatedAnnealing import simulated_annealing
import time
import argparse


def calcute_metodos_param(arquivo_matriz: str, incrementar_cidades: bool, num_cidades: int,
                          exec_forca_bruta: bool, exec_alg_genetico: bool,
                          exec_simulated_annealing: bool, inicio_aumento: int, fim_aumento: int):

    # Inicializar o tempo total de execução do programa
    tic_total = time.time()

    # Variáveis
    metodos = ['Força Bruta', 'Algoritmo Genético', 'Simulated Annealing']

    # Carregar matrizes de dados
    DistMatriz = pd.DataFrame(np.zeros((16, 16)))
    # TempMatriz = pd.DataFrame(np.zeros((16, 16)))

    # Ler o arquivo de texto
    data_dist = pd.read_csv(arquivo_matriz, delimiter='\t')
    # data_temp = pd.read_csv('MatrizTempProfessor.txt', delimiter='\t')

    # Converter os dados em uma matriz de banco de dados
    DistMatriz = data_dist
    # TempMatriz = data_temp

    # Definir variáveis de controle para cada método
    # 1 para aumentar, 0 para não aumentar
    aumentar_cidades = incrementar_cidades
    num_cidades_fixo = num_cidades  # Número de cidades fixo
    # 1 para executar, 0 para não executar
    executar_forca_bruta = exec_forca_bruta
    # 1 para executar, 0 para não executar
    executar_alg_genetico = exec_alg_genetico
    # 1 para executar, 0 para não executar
    executar_simulated_annealing = exec_simulated_annealing
    execute_control = executar_alg_genetico + executar_forca_bruta + \
        executar_simulated_annealing  # Variável de controle para o teste t de Student
    ttest_control = 0  # 1 para executar, 0 para não executar

    # Tamanho População inicial e Numero de gerações para o Algoritmo Genético
    tam_Pop_ini_AG = 10
    tam_gera_AG = 100

    # Variáveis para o modelo de Simulated Annealing
    num_int_SA = 100
    temp_ini = 0.7
    taxa_resfri = 0.95

    # Criação da Tabela de Resultados
    n_simulacoes = 8
    if aumentar_cidades:
        num_cidades_vec = np.arange(inicio_aumento, fim_aumento+1)
        n_simulacoes = len(num_cidades_vec)
    else:
        num_cidades_vec = np.array([num_cidades_fixo] * n_simulacoes)
    Tab_Resultados_tempo = np.zeros((n_simulacoes, 3))
    Tab_Resultados_dist = np.zeros((n_simulacoes, 3))

    for sim in range(n_simulacoes):
        if aumentar_cidades:
            N_cidades = num_cidades_vec[sim]  # Altera o número de cidades
        else:
            N_cidades = num_cidades_fixo  # Mantém o número de cidades fixo

        # Sortear cidades
        indi_random = np.random.choice(
            range(len(DistMatriz)), N_cidades, replace=False
        )

        # Selecionar as cidades na matriz original
        MatrizDistTrab = DistMatriz.iloc[indi_random, indi_random].values
        # MatrizTempTrab = TempMatriz.iloc[indi_random, indi_random].values

        # Executar Força Bruta se a variável de controle estiver definida como 1
        if executar_forca_bruta:
            resultados_forca_bruta = forcabruta(MatrizDistTrab)
            tempoFB = resultados_forca_bruta['tempoFB']
            menordistFB = resultados_forca_bruta['distanciamenor']
            Tab_Resultados_tempo[sim, 0] = tempoFB
            Tab_Resultados_dist[sim, 0] = menordistFB

        # Executar Algoritmo Genético se a variável de controle estiver definida como 1
        if executar_alg_genetico:
            resultados_algoritmo_genetico = alggenetico(
                MatrizDistTrab, tam_Pop_ini_AG, tam_gera_AG)
            tempoAG = resultados_algoritmo_genetico['tempoAG']
            menordistAG = resultados_algoritmo_genetico['menorDistancia']
            Tab_Resultados_tempo[sim, 1] = tempoAG
            Tab_Resultados_dist[sim, 1] = menordistAG

        # Executar Simulated Annealing se a variável de controle estiver definida como 1
        if executar_simulated_annealing:
            resultados_SA = simulated_annealing(
                MatrizDistTrab, temp_ini, taxa_resfri, num_int_SA)
            tempoSA = resultados_SA['tempo']
            menordistSA = resultados_SA['menorDistancia']
            Tab_Resultados_tempo[sim, 2] = tempoSA
            Tab_Resultados_dist[sim, 2] = menordistSA

    # Calcula a média dos tempos das simulações
    Resultados_Final_tempo = np.mean(Tab_Resultados_tempo, axis=0)

    # Crie um gráfico de linha para cada método
    plt.figure(figsize=(5, 5))
    if aumentar_cidades:
        for i in range(3):
            plt.plot(
                num_cidades_vec, Tab_Resultados_tempo[:, i], '-o', label=metodos[i], linewidth=5)
    else:
        for i in range(3):
            plt.plot(range(1, n_simulacoes + 1),
                     Tab_Resultados_tempo[:, i], '-o', label=metodos[i], linewidth=5)
    if aumentar_cidades == 1:
        plt.xlabel('Número de Cidades', fontsize=20)
    else:
        plt.xlabel('Simulação', fontsize=20)
    plt.ylabel('Tempo de Execução (segundos)', fontsize=20)
    plt.title('Tempo de Execução x Número de Cidades', fontsize=20)
    plt.legend(loc='upper left', fontsize=20)
    plt.xticks(fontsize=20)
    plt.yticks(fontsize=20)
    plt.grid(True)

    # Crie um gráfico de linha para Algoritmo Genético e Simulated Annealing
    plt.figure(figsize=(5, 5))
    if aumentar_cidades:
        plt.plot(num_cidades_vec,
                 Tab_Resultados_tempo[:, 1], '-o', label='Algoritmo Genético', linewidth=5)
        plt.plot(num_cidades_vec,
                 Tab_Resultados_tempo[:, 2], '-o', label='Simulated Annealing', linewidth=5)
    else:
        plt.plot(range(1, n_simulacoes + 1),
                 Tab_Resultados_tempo[:, 1], '-o', label='Algoritmo Genético', linewidth=5)
        plt.plot(range(1, n_simulacoes + 1),
                 Tab_Resultados_tempo[:, 2], '-o', label='Simulated Annealing', linewidth=5)
    if aumentar_cidades:
        plt.xlabel('Número de Cidades', fontsize=20)
    else:
        plt.xlabel('Simulação', fontsize=20)
    plt.ylabel('Tempo de Execução (segundos)', fontsize=20)
    plt.title('Tempo de Execução de Algoritmo Genético e Simulated Annealing x'
              ' Número de Cidades', fontsize=20)
    plt.legend(loc='upper left', fontsize=20)
    plt.xticks(fontsize=20)
    plt.yticks(fontsize=20)
    plt.grid(True)

    # Crie um gráfico de barras para as menores distâncias de todos os métodos
    plt.figure(figsize=(5, 5))
    largura_barra = 0.2
    posicoes = np.arange(len(num_cidades_vec))
    for i in range(3):
        plt.bar(posicoes + i * largura_barra,
                Tab_Resultados_dist[:, i], width=largura_barra, label=metodos[i])
    plt.xlabel('Número de Cidades', fontsize=20)
    plt.ylabel('Distância', fontsize=20)
    plt.title('Menor Distância x Número de Cidades', fontsize=20)
    plt.legend(fontsize=16, loc='upper right')
    plt.xticks(posicoes, num_cidades_vec, fontsize=20)
    plt.yticks(fontsize=20)
    plt.grid(True)
    plt.show()

    # Exibe o Resultado final
    resultados_finais = []
    list_prints = []

    for i, metodo in enumerate(metodos):
        media_tempo = Resultados_Final_tempo[i]
        desvio_padrao_tempo = np.std(Tab_Resultados_tempo[:, i])
        resultados_finais.append({
            'metodo': metodo,
            'media_tempo': media_tempo,
            'desvio_padrao_tempo': desvio_padrao_tempo
        })
    for i, metodo in enumerate(metodos):
        list_prints.append(
            f'Média dos tempos das simulações do Método \
                {metodo}: {Resultados_Final_tempo[i]} segundos')
        list_prints.append(
            f'Desvio padrão dos tempos das simulações do Método \
                  {metodo}: {np.std(Tab_Resultados_tempo[:, i])} segundos')

    # Exibe o tempo total de execução do programa
    tic_total = time.time() - tic_total
    list_prints.append(
        f'Tempo total de execução do programa: {tic_total} segundos')

    # Cria o Dicionário dos resultados
    resultados_para_interface = {
        "Força Bruta": {
            "media_tempo": Resultados_Final_tempo[0],
            "desvio_padrao_tempo": np.std(Tab_Resultados_tempo[:, 0]),
            "Menor Rota": resultados_forca_bruta['Rota_menor'] if 'resultados_forca_bruta' in locals() else None
        },
        "Algoritmo Genético": {
            "media_tempo": Resultados_Final_tempo[1],
            "desvio_padrao_tempo": np.std(Tab_Resultados_tempo[:, 1]),
            "Menor Rota": resultados_algoritmo_genetico['melhorRota'] if 'resultados_algoritmo_genetico' in locals() else None
        },
        "Simulated Annealing": {
            "media_tempo": Resultados_Final_tempo[2],
            "desvio_padrao_tempo": np.std(Tab_Resultados_tempo[:, 2]),
            "Menor Rota": resultados_SA['melhorRota'] if 'resultados_SA' in locals() else None
        }


    }

    if ttest_control == 1:
        if execute_control >= 2:
            # Realize um teste t de Student pareado (duas amostras relacionadas)
            # ttest_fb = ttest_rel(
            # Tab_Resultados_tempo[:, 0], Resultados_Final_tempo[0])
            # ttest_ag = ttest_rel(
            # Tab_Resultados_tempo[:, 1], Resultados_Final_tempo[1])
            # if execute_control == 3:
            # ttest_sa = ttest_rel(
            # Tab_Resultados_tempo[:, 2], Resultados_Final_tempo[2])

            # Obtenha o valor-p do teste t
            p_value = ttest_rel(
                Tab_Resultados_tempo[:, 1], Tab_Resultados_tempo[:, 2])
            # Exiba o resultado do teste t
            print('Valor-p do teste t de Student:', p_value)

            # Verifique se o valor-p é menor que o nível de significância desejado (0,2)
            nivel_significancia = 0.2
            if p_value < nivel_significancia:
                print(
                    'Rejeita a hipótese nula: Existe uma diferença significativa entre os métodos.')
            else:
                print('Não rejeita a hipótese nula: Não há evidência suficiente para concluir'
                      'que existe uma diferença significativa entre os métodos.')
    return resultados_para_interface


if __name__ == '__main__':
    argparser = argparse.ArgumentParser(description='TCC Program')
    argparser.add_argument('arquivo_matriz', type=str,
                           help='Arquivo de matriz')
    argparser.add_argument('incrementar_cidades',
                           type=bool, help='Incrementar cidades')
    argparser.add_argument('num_cidades', type=int, help='Número de cidades')
    argparser.add_argument('exec_forca_bruta', type=bool,
                           help='Executar Força Bruta')
    argparser.add_argument('exec_alg_genetico', type=bool,
                           help='Executar Algoritmo Genético')
    argparser.add_argument('exec_simulated_annealing',
                           type=bool, help='Executar Simulated Annealing')
    argparser.add_argument('inicio_aumento', type=int,
                           help='Início do aumento')
    argparser.add_argument('fim_aumento', type=int, help='Fim do aumento')
    args = argparser.parse_args()

    # Executar o programa principal
    calcute_metodos_param(args.arquivo_matriz, args.incrementar_cidades, args.num_cidades,
                          args.exec_forca_bruta, args.exec_alg_genetico,
                          args.exec_simulated_annealing, args.inicio_aumento, args.fim_aumento)
