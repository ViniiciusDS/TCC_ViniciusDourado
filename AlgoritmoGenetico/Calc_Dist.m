


function  Percurso = Calc_Dist(DistMatriz,Populacao) 
    
    dist = 0;
    cidade_ant = Populacao(1);

    for i = 2:length(Populacao)

        cidade_atual = Populacao(i);
        dist = dist + (DistMatriz(cidade_ant,cidade_atual));
        cidade_ant   = cidade_atual;

    end
Percurso = dist;
end