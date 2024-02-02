

import itertools
import numpy as np
import time

start_time = time.time()

# Dados Cidades N = 10
# 1 - UEL, Londrina
# 2 - Ibipor� ; Raio de 20km
# 3 - Maring� ; Raio de 40km
# 4 - Cascavel ; Raio de 80km
# 5 - Paranagua ; Raio maior que 160km
# 6 - P�rola
# 7 - Palmas
# 8 - Brasilandia do Sul
# 9 - Seng�s
# 10 - Santo Antonio do Sudoeste

DistMatriz = np.array([[0, 21, 98, 378, 485, 309, 525, 319, 308, 534, 387, 250, 260, 38, 72],
                       [21, 0, 111, 391, 498, 322, 538, 332, 285, 547, 400, 263, 273, 50, 76],
                       [98, 111, 0, 283, 523, 212, 508, 222, 399, 439, 426, 148, 162, 61, 153],
                       [378, 391, 283, 0, 603, 171, 310, 106, 556, 163, 501, 324, 168, 336, 435],
                       [485, 498, 523, 603, 0, 693, 450, 697, 371, 657, 90, 668, 644, 472, 545],
                       [309, 322, 212, 171, 693, 0, 497, 63, 638, 327, 605, 209, 49, 272, 366],
                       [525, 538, 508, 310, 450, 497, 0, 409, 493, 221, 374, 645, 471, 494, 593],
                       [319, 332, 222, 106, 697, 63, 409, 0, 648, 262, 598, 219, 64, 282, 375],
                       [308, 285, 399, 556, 371, 638, 493, 648, 0, 622, 273, 502, 588, 302, 332],
                       [534, 547, 439, 163, 657, 327, 221, 262, 622, 0, 567, 479, 324, 496, 592],
                       [387, 400, 426, 501, 90, 605, 374, 598, 273, 567, 0, 577, 554, 381, 454],
                       [250, 263, 148, 324, 668, 209, 645, 219, 502, 479, 577, 0, 156, 214, 255],
                       [260, 273, 162, 168, 644, 49, 471, 64, 588, 324, 554, 156, 0, 223, 316],
                       [38, 50, 61, 336, 472, 272, 494, 282, 302, 496, 381, 214, 223, 0, 94],
                       [72, 76, 153, 435, 545, 366, 593, 375, 332, 592, 454, 255, 316, 94, 0]])



VetorIndi = np.arange(1, 11)

# permuta��o dos indices
Pi = list(itertools.permutations(VetorIndi))

# Variavel da Distancia
distanciamenor = np.inf
distanciamaior = 0

# Calculo da rota
VetorDistancias = np.zeros((len(Pi),1))
indice_rota_menor = 0
indice_rota_maior = 0
Rota_menor = 0
   
for i in range(len(Pi)):
    rota = Pi[i]  # Armazena a rota atual
    distancia = 0

    for j in range(len(rota)):
        Cidade_partida = rota[j]
        Cidade_chegada = rota[(j+1) % len(rota)]
        distancia = distancia + DistMatriz[Cidade_partida-1, Cidade_chegada-1]

    # Armazenador de distancias
    VetorDistancias[i, 0] = distancia

    # Comparadores
    if distancia < distanciamenor:
        distanciamenor = distancia
        Indice_Rota_menor = i
        Rota_menor = rota
    if distancia > distanciamaior:
        distanciamaior = distancia
        Indice_Rota_maior = i
        Rota_maior = rota


# Exibi as dist�ncias
print('A distancia total da menor rota eh e a rota eh a:')
print(distanciamenor)
print(Indice_Rota_menor)
print(Rota_menor)
print('A distancia total da maior rota eh e a rota eh a:')
print(distanciamaior)
print(Indice_Rota_maior)
print(Rota_maior)

print('Tempo de execucao: %.6f segundos' % (time.time() - start_time))