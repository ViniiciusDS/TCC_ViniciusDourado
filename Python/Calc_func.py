"""Funções de cálculo de custo e distância"""

"""Função para calcular o custo, com distâncias e tempo"""


def Calc_Custo(DistMatriz, Populacao, TempMatriz):
    custo = 0
    cidade_ant = Populacao[0]

    for i in range(1, len(Populacao)):
        cidade_atual = Populacao[i]
        custo = custo + \
            DistMatriz[cidade_ant][cidade_atual] / \
            TempMatriz[cidade_ant][cidade_atual]
        cidade_ant = cidade_atual

    Percurso = custo
    return Percurso


"""Função para calcular a distância"""


def Calc_Dist(DistMatriz, Populacao):
    dist = 0
    cidade_ant = int(Populacao[0])

    for i in range(1, len(Populacao)):
        cidade_atual = int(Populacao[i])
        dist = dist + DistMatriz[cidade_ant-1, cidade_atual-1]
        cidade_ant = cidade_atual

    Percurso = dist
    return Percurso
