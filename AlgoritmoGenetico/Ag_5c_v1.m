
%clc 
clear all
tic

% Dados Cidades N = 10
% 1  - UEL, Londrina
% 2  - Ibiporã               ; Raio de 20km
% 3  - Maringá               ; Raio de 40km
% 4  - Cascavel              ; Raio de 80km
% 5  - Paranagua             ; Raio maior que 160km


DistMatriz = [0      21      98      378     485;
              21     0       111     391     498;
              98     111     0       283     523;
              378    391     283     0       603;
              485    498     523     603     0  ];

numCidades = 5;

%indices
tam_Pop_ini = 10;              %Tamanho População Inicial
tam_gera    = 100;            %Nmr de gerações

%Geracao da Populacao Inicial
for k = 1:tam_Pop_ini
    
    %Gera um vetor de 11 posicoes com numeros de 2 a 10 (cidades) distribuidos aleatoriamente

    [a b] = sort(rand(1,4));
    b = b + 1;
    
    %Cromossomo
    Populacao(k, :) = [1, b, 1];

end


for g = 1:tam_gera

    %Calcula o percurso total de cada vetor solucao
    for k = 1:size(Populacao,1),
        Percurso(k, g) = Calc_Dist(DistMatriz, Populacao(k,:));
    end

    %Escolhe os mais aptos 
    clear a b;
    [a b] = sort(Percurso(:,g));
    
    Pai = Populacao(b(1,1), :);
    Mae = Populacao(b(2,1), :);

    %Cada Genitor vai gerar 2 filhos por permuta
    %Sorteia e permuta as duas posicoes do Pai
    for k = 1:4,
        clear a b;
        [a b] = sort(rand(1,4));
        b = b + 1;

        FilhosPai(k, :) = Pai;
        FilhosPai(k, b(1, 1)) = Pai(1, b(1, 2));
        FilhosPai(k, b(1, 2)) = Pai(1, b(1, 1));
    end

    %Sorteia e permuta as duas posicoes da Mae
    for k = 1:4,
        clear a b;
        [a b] = sort(rand(1,4));
        b = b + 1;

        FilhosMae(k, :) = Mae;
        FilhosMae(k, b(1, 1)) = Mae(1, b(1, 2));
        FilhosMae(k, b(1, 2)) = Mae(1, b(1, 1));
    end


    %Atualiza a Populacao
    Populacao = [Pai; Mae; FilhosPai; FilhosMae];
  
end

toc
plot(min(Percurso, [], 1));







