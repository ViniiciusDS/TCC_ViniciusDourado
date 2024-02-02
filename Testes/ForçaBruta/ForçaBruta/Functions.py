


def calc_dist(dist_matriz, populacao):
    dist = 0
    cidade_ant = int(populacao[0])

    for i in range(1, len(populacao)):
        cidade_atual = int(populacao[i])
        dist += dist_matriz[cidade_ant - 1, cidade_atual - 1]
        cidade_ant = cidade_atual

    return dist