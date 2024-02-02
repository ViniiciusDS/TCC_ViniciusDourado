import itertools
import numpy as np
import time

start_time = time.time()

# Dados Cidades N = 10
# 1 - UEL, Londrina
# 2 - Ibiporã ; Raio de 20km
# 3 - Maringá ; Raio de 40km
# 4 - Cascavel ; Raio de 80km
# 5 - Paranagua ; Raio maior que 160km
# 6 - Pérola
# 7 - Palmas
# 8 - Brasilandia do Sul
# 9 - Sengés
# 10 - Santo Antonio do Sudoeste

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

vetor_indi = np.arange(1, 11)

# permutação dos indices
pi = itertools.permutations(vetor_indi)

# Variavel da Distancia
distancia_menor = np.inf
distancia_maior = 0

# Calculo da rota
vetor_distancias = np.zeros(len(list(pi)))
indice_rota_menor = 0
indice_rota_maior = 0

for i, rota in enumerate(pi):
    distancia = 0
    for j in range(len(rota)):
        cidade_partida = rota[j]
        cidade_chegada = rota[(j+1) % len(rota)]
        distancia += dist_matriz[cidade_partida-1, cidade_chegada-1]
    
    # Armazenador de distancias
    vetor_distancias[i] = distancia

    # Comparadores
    if distancia < distancia_menor:
        distancia_menor = distancia
        indice_rota_menor = i
        rota_menor = rota
    if distancia > distancia_maior:
        distancia_maior = distancia
        indice_rota_maior = i
        rota_maior = rota

# Exibi as distâncias
print('A distância total da menor rota é e a rota é a:')
print(distancia_menor)
