function SA_Func = simulatedAnnealing(matrizDistancia, temperaturaInicial, taxaResfriamento, numIteracoes)

    tic_total = tic;
    
    %   Definindo variaveis
    numCidades         = size(matrizDistancia, 1);

    %   Gera a solução inicial aleatória
    cidades_aleatorias = randperm(numCidades-1) + 1;
    melhorRota         = [1, cidades_aleatorias, 1]; %  Solução inicial Aleatória
    melhorCusto        = calcularCustoRota(melhorRota, matrizDistancia);
    
    %   Variaveis para parâmetro de comparação
    rotaAtual = melhorRota;
    custoAtual = melhorCusto;

    for iteracao = 1:numIteracoes

        % Gera uma nova solução vizinha alterando aleatoriamente a solução atual
        novaRota = gerarNovaRotaVizinha(rotaAtual);
        novoCusto = calcularCustoRota(novaRota, matrizDistancia);

        % Calcula a diferença de custo entre a nova solução e a solução atual
        deltaCusto = novoCusto - custoAtual;

        % Aceita a nova solução se ela for melhor ou com uma certa probabilidade se for pior
        if (deltaCusto < 0) || (rand() < exp(-deltaCusto / temperaturaInicial))
            rotaAtual = novaRota;
            custoAtual = novoCusto;

            % Atualiza a melhor solução encontrada
            if custoAtual < melhorCusto
                melhorRota = rotaAtual;
                melhorCusto = custoAtual;
            end
        end

        % Atualiza a temperatura
        temperaturaInicial = temperaturaInicial * taxaResfriamento;
    end

    tempoSA = toc(tic_total);

    % Preparando a saída da função
    SA_Func.tempoSA = tempoSA;
    SA_Func.menorDistancia = melhorCusto;
    SA_Func.melhorRota = melhorRota;

    

end

function custo = calcularCustoRota(rota, matrizDistancia)

    % Calcula o custo total da rota
    custo = 0;
    numCidades = length(rota);

    for i = 1:numCidades

        cidadeAtual = rota(i);
        cidadeProxima = rota(mod(i, numCidades) + 1); % Próxima cidade considerando rota circular
        custo = custo + matrizDistancia(cidadeAtual, cidadeProxima);
        
    end
end

function novaRota = gerarNovaRotaVizinha(rotaAtual)

    % Gera uma nova solução vizinha alterando aleatoriamente a solução atual
    numCidades = length(rotaAtual);
    indice1 = randi(numCidades);
    indice2 = randi(numCidades);
    novaRota = rotaAtual;
    novaRota([indice1, indice2]) = novaRota([indice2, indice1]); % Troca duas cidades aleatoriamente

end


