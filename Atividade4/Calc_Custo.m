
function Percurso = Calc_Custo(DistMatriz, Populacao,TempMatriz)
    custo = 0;
    cidade_ant = Populacao(1);

    for i = 2:length(Populacao)
        cidade_atual = Populacao(i);
        custo = custo + DistMatriz(cidade_ant, cidade_atual) / TempMatriz(cidade_ant, cidade_atual);
        cidade_ant = cidade_atual;
    end

    Percurso = custo;
end