"""Código main do TCC, afim de realizar testes estatísticos e gráficos"""
import numpy as np  # Importar a biblioteca numpy
import pandas as pd  # Importar a biblioteca pandas
import matplotlib.pyplot as plt  # Importar a biblioteca matplotlib
from scipy.stats import ttest_rel  # Importar a função ttest_rel
from forca_bruta import forcabruta  # Importar a função forcabruta
from alggenetico import alggenetico  # Importar a função alggenetico
# Importar a função simulatedAnnealing
from simulatedAnnealing import simulated_annealing
import time

# Inicializar o tempo total de execução do programa
tic_total = time.time()

# Carregar matrizes de dados
DistMatriz = pd.DataFrame(np.zeros((16, 16)))
TempMatriz = pd.DataFrame(np.zeros((16, 16)))

# Ler o arquivo de texto
# data_dist = pd.read_csv('MatriDistAlmoco.txt', delimiter='\t')
data_dist = pd.read_csv('MatriDistJanta.txt', delimiter='\t')
# data_dist = pd.read_csv('MatrizDistProfessor.txt', delimiter='\t')
# data_dist = pd.read_csv('MatrizDistOriginal.txt', delimiter='\t')
data_temp = pd.read_csv('MatrizTempProfessor.txt', delimiter='\t')

# Converter os dados em uma matriz de banco de dados
DistMatriz = data_dist
TempMatriz = data_temp

# Definir variáveis de controle para cada método
executar_forca_bruta = 1  # 1 para executar, 0 para não executar
executar_alg_genetico = 1  # 1 para executar, 0 para não executar
executar_simulated_annealing = 1  # 1 para executar, 0 para não executar
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
num_cidades_vec = np.arange(4, 12)
Tab_Resultados_tempo = np.zeros((n_simulacoes, 3))
Tab_Resultados_dist = np.zeros((n_simulacoes, 3))

for sim in range(n_simulacoes):
    N_cidades = num_cidades_vec[sim]  # Altera o número de cidades

    # Sortear cidades
    indi_random = np.random.choice(
        range(len(DistMatriz)), N_cidades, replace=False
    )

    # Selecionar as cidades na matriz original
    MatrizDistTrab = DistMatriz.iloc[indi_random, indi_random].values
    MatrizTempTrab = TempMatriz.iloc[indi_random, indi_random].values

    # Executar Força Bruta se a variável de controle estiver definida como 1
    if executar_forca_bruta == 1:
        resultados_forca_bruta = forcabruta(MatrizDistTrab)
        tempoFB = resultados_forca_bruta['tempoFB']
        menordistFB = resultados_forca_bruta['distanciamenor']
        Tab_Resultados_tempo[sim, 0] = tempoFB
        Tab_Resultados_dist[sim, 0] = menordistFB

    # Executar Algoritmo Genético se a variável de controle estiver definida como 1
    if executar_alg_genetico == 1:
        resultados_algoritmo_getenico = alggenetico(
            MatrizDistTrab, tam_Pop_ini_AG, tam_gera_AG)
        tempoAG = resultados_algoritmo_getenico['tempoAG']
        menordistAG = resultados_algoritmo_getenico['menorDistancia']
        Tab_Resultados_tempo[sim, 1] = tempoAG
        Tab_Resultados_dist[sim, 1] = menordistAG

    # Executar Simulated Annealing se a variável de controle estiver definida como 1
    if executar_simulated_annealing == 1:
        resultados_SA = simulated_annealing(
            MatrizDistTrab, temp_ini, taxa_resfri, num_int_SA)
        tempoSA = resultados_SA['tempo']
        menordistSA = resultados_SA['menorDistancia']
        Tab_Resultados_tempo[sim, 2] = tempoSA
        Tab_Resultados_dist[sim, 2] = menordistSA


# Calcula a média dos tempos das simulações
Resultados_Final_tempo = np.mean(Tab_Resultados_tempo, axis=0)

# Calcula o desvio padrão dos tempos das simulações
desvio_padrao_temposFB = np.std(Tab_Resultados_tempo[:, 0])
desvio_padrao_temposAG = np.std(Tab_Resultados_tempo[:, 1])
desvio_padrao_temposSA = np.std(Tab_Resultados_tempo[:, 2])

# Crie um gráfico de linha para cada método
fig1 = plt.figure(figsize=(5, 5))
plt.plot(num_cidades_vec,
         Tab_Resultados_tempo[:, 0], '-o', label='Força Bruta', linewidth=5)
plt.plot(num_cidades_vec,
         Tab_Resultados_tempo[:, 1], '-o', label='Algoritmo Genético', linewidth=5)
plt.plot(num_cidades_vec,
         Tab_Resultados_tempo[:, 2], '-o', label='Simulated Annealing', linewidth=5)

plt.xlabel('Número de Cidades', fontsize=20)
plt.ylabel('Tempo de Execução (segundos)', fontsize=20)
plt.title('Tempo de Execução x Número de Cidades', fontsize=20)
plt.legend(loc='upper left', fontsize=20)
plt.xticks(fontsize=20)
plt.yticks(fontsize=20)
plt.grid(True)


# Crie um gráfico de linha para Algoritmo Genético e Simulated Annealing
fig2 = plt.figure(figsize=(5, 5))
plt.plot(num_cidades_vec,
         Tab_Resultados_tempo[:, 1], '-o', label='Algoritmo Genético', linewidth=5)
plt.plot(num_cidades_vec,
         Tab_Resultados_tempo[:, 2], '-o', label='Simulated Annealing', linewidth=5)

plt.xlabel('Número de Cidades', fontsize=20)
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

plt.bar(posicoes - largura_barra,
        Tab_Resultados_dist[:, 0], width=largura_barra, label='Força Bruta')
plt.bar(posicoes, Tab_Resultados_dist[:, 1],
        width=largura_barra, label='Algoritmo Genético')
plt.bar(posicoes + largura_barra,
        Tab_Resultados_dist[:, 2], width=largura_barra, label='Simulated Annealing')

plt.xlabel('Número de Cidades', fontsize=20)
plt.ylabel('Distância', fontsize=20)
plt.title('Menor Distância x Número de Cidades', fontsize=20)
plt.legend(fontsize=16, loc='upper right')
plt.xticks(posicoes, num_cidades_vec, fontsize=20)
plt.yticks(fontsize=20)
plt.grid(True)
plt.show()


# Exibe o Resultado final
# Força bruta
print('Média dos tempos das simulações do Método Força Bruta:',
      Resultados_Final_tempo[0], 'segundos')
print('Desvio padrão dos tempos das simulações, Força Bruta:',
      desvio_padrao_temposFB, 'segundos')
# Algoritmo Genético
print('Média dos tempos das simulações do Método Algoritmo Genético:',
      Resultados_Final_tempo[1], 'segundos')
print('Desvio padrão dos tempos das simulações, Algoritmo Genético:',
      desvio_padrao_temposAG, 'segundos')
# Simulated Annealing
print('Média dos tempos das simulações do Método Simulated Annealing:',
      Resultados_Final_tempo[2], 'segundos')
print('Desvio padrão dos tempos das simulações, Simulated Annealing:',
      desvio_padrao_temposSA, 'segundos')

# Exibe o tempo total de execução do programa
tic_total = time.time() - tic_total
print('Tempo total de execução do programa:', tic_total, 'segundos')

if ttest_control == 1:
    if execute_control >= 2:
        # Realize um teste t de Student pareado (duas amostras relacionadas)
        ttest_fb = ttest_rel(
            Tab_Resultados_tempo[:, 0], Resultados_Final_tempo[0])
        ttest_ag = ttest_rel(
            Tab_Resultados_tempo[:, 1], Resultados_Final_tempo[1])
        if execute_control == 3:
            ttest_sa = ttest_rel(
                Tab_Resultados_tempo[:, 2], Resultados_Final_tempo[2])

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
