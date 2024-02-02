
import itertools
import numpy as np
import time

start_time = time.time()

# Dados Cidades N = 5
# 1 - Londrina
# 2 - Ibiporã               ; Raio de 20km
# 3 - Maringá               ; Raio de 40km
# 4 - Cascavel              ; Raio de 80km
# 5 - Paranagua             ; Raio maior que 160km

DistMatriz = np.array([[0,      21,      98,      378,     485],
                       [21,     0,       111,     391,     498],
                       [98,     111,     0,       283,     523],
                       [378,    391,     283,     0,       603],
                       [485,    498,     523,     603,     0]])

VetorIndi = np.array([1, 2, 3, 4, 5])

# permutação dos indices
Pi = list(itertools.permutations(VetorIndi))

rotateste = [1, 2, 3, 4, 5]

# Variavel da Distancia
distanciamenor = np.inf
distanciamaior = 0

# Calculo da rota
VetorDistancias = np.zeros((len(Pi),1))
Indice_Rota_menor = 0
Indice_Rota_maior = 0



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

# Exibi as distâncias
print('A distancia total da menor rota eh e a rota eh a:')
print(distanciamenor)
print(Indice_Rota_menor)
print(Rota_menor)
print('A distancia total da maior rota eh e a rota eh a:')
print(distanciamaior)
print(Indice_Rota_maior)
print(Rota_maior)

print('Tempo de execucao: %.6f segundos' % (time.time() - start_time))