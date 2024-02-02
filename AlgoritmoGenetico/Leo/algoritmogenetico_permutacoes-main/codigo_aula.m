%Programa do Caixeiro Viajante
%Autor: Ernesto F. F. Ramirez
%Data: 02/12/2022


clear all;

%Matriz de Distancias em km
Dist(1,:) = [0, 89.5, 24.7, 15.8, 39.2, 100];
Dist(2,:) = [85.1, 0, 72.5, 91.4, 84.1, 121];
Dist(3,:) = [24.4, 72.2, 0, 34.9, 18.0,  79];
Dist(4,:) = [15.6, 91.2, 35,   0, 52.1, 113];
Dist(5,:) = [39,    84, 18.4, 49.5, 0, 61.2];
Dist(6,:) = [99.7, 120, 79.4, 110, 60.9, 0];

%   1 = Londrina
%   2 = Porecatu
%   3 = Rolandia
%   4 = Ibipora
%   5 = Arapongas
%   6 = Maringa

%Geracao da Populacao Inicial
for k = 1:10,
    
    %Gera um vetor de 5 posicoes com numeros
    %de 2 a 6 distribuidos aleatoriamente
    [a b] = sort(rand(1,5));
    b = b + 1;
    
    %Cada linha serah um cromossomo
    Populacao(k, :) = [1, b, 1];
end

for g = 1:20,
    %Calcula o percurso total de cada vetor solucao
    for k = 1:size(Populacao,1),
        Percurso(k, g) = DistTotal(Populacao(k,:),Dist);
    end

    %Escolhe os 2 mais aptos (menores valores de Percurso)
    clear a b;
    [a b] = sort(Percurso(:,g));
    
    Pai = Populacao(b(1,1), :);
    Mae = Populacao(b(2,1), :);


    %- - - Forma a nova Geracao - - -

    %Cada Genitor vai gerar 2 filhos por permuta
    %Sorteia e permuta as duas posicoes do Pai
    for k = 1:4,
        clear a b;
        [a b] = sort(rand(1,5));
        b = b + 1;

        FilhosPai(k, :) = Pai;
        FilhosPai(k, b(1, 1)) = Pai(1, b(1, 2));
        FilhosPai(k, b(1, 2)) = Pai(1, b(1, 1));
    end

    %Sorteia e permuta as duas posicoes da Mae
    for k = 1:4,
        clear a b;
        [a b] = sort(rand(1,5));
        b = b + 1;

        FilhosMae(k, :) = Mae;
        FilhosMae(k, b(1, 1)) = Mae(1, b(1, 2));
        FilhosMae(k, b(1, 2)) = Mae(1, b(1, 1));
    end


    %Atualiza a Populacao
    Populacao = [Pai; Mae; FilhosPai; FilhosMae];
  
end

plot(min(Percurso, [], 1));
