"""Funções de cálculo de custo e distância"""

"""Função para calcular a distância (usada no AG)"""


def Calc_Dist(DistMatriz, Populacao):
    dist = 0
    cidade_ant = int(Populacao[0])

    for i in range(1, len(Populacao)):
        cidade_atual = int(Populacao[i])
        dist = dist + DistMatriz[cidade_ant-1, cidade_atual-1]
        cidade_ant = cidade_atual

    Percurso = dist
    return Percurso
