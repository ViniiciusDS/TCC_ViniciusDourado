
import numpy as np
import random
import matplotlib.pyplot as plt
from Functions import calc_dist
import time

start_time = time.time()

np.random.seed()
random.seed()

dist_matriz = np.array([[0, 21, 98, 378, 485, 309, 525, 319, 308, 534],
                        [21, 0, 111, 391, 498, 322, 538, 332, 285, 547],
                        [98, 111, 0, 283, 523, 212, 508, 222, 399, 439],
                        [378, 391, 283, 0, 603, 171, 310, 106, 556, 163],
                        [485, 498, 523, 603, 0, 693, 450, 697, 371, 657],
                        [309, 322, 212, 171, 693, 0, 497, 63, 638, 327],
                        [525, 538, 508, 310, 450, 497, 0, 409, 493, 221],
                        [319, 332, 222, 106, 697, 63, 409, 0, 648, 262],
                        [308, 285, 399, 556, 371, 638, 493, 648, 0, 622],
                        [534, 547, 439, 163, 657, 327, 221, 262, 622, 0]])

num_cidades = 10
tam_pop_ini = 10  # Tamanho População Inicial
tam_gera = 100  # Nmr de gerações

populacao = np.zeros((tam_pop_ini, num_cidades + 1))

# Geração da População Inicial
for k in range(tam_pop_ini):
    b = random.sample(range(2, num_cidades + 1), num_cidades - 1)

    populacao[k, :] = np.insert(b, [0, len(b)], [1, 1])

percurso = np.zeros((tam_pop_ini, tam_gera))


for g in range(tam_gera):
    # Calcula o percurso total de cada vetor solução
    for k in range(tam_pop_ini):
        dist =  calc_dist(dist_matriz, populacao[k, :])
        percurso[k,g] = dist

    # Escolhe os mais aptos
    b = np.argsort(percurso[:, g])
    pai = populacao[b[0]]
    mae = populacao[b[1]]

    filhos_pai = np.zeros((4, num_cidades + 1))
    filhos_mae = np.zeros((4, num_cidades + 1))

    # Cada Genitor vai gerar 2 filhos por permuta
    # Sorteia e permuta as duas posições do Pai
    for k in range(4):
        b = random.sample(range(1, num_cidades), 2)
        filhos_pai[k] = pai
        filhos_pai[k, b[0]], filhos_pai[k, b[1]] = filhos_pai[k, b[1]], filhos_pai[k, b[0]]

        b = random.sample(range(1, num_cidades), 2)
        filhos_mae[k] = mae
        filhos_mae[k, b[0]], filhos_mae[k, b[1]] = filhos_mae[k, b[1]], filhos_mae[k, b[0]]

    # Nova População
    
    populacao = np.concatenate((np.array([pai]), np.array([mae]), filhos_pai, filhos_mae))
    


# Plot do percurso da melhor solução encontrada
melhor_solucao_idx = np.argmin(percurso[:, -1])
melhor_solucao = populacao[melhor_solucao_idx]
melhor_percurso = calc_dist(dist_matriz, melhor_solucao)

print("Melhor solucao encontrada:", melhor_solucao)
print("Melhor percurso encontrado:", melhor_percurso)
print('Tempo de execucao: %.6f segundos' % (time.time() - start_time))

plt.plot(percurso[melhor_solucao_idx])
plt.xlabel("Geracao")
plt.ylabel("Distancia percorrida")
plt.title("Melhor percurso encontrado")
plt.show()



