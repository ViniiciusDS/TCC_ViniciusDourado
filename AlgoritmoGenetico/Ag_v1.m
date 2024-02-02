
%clc 
clear all
tic

% Dados Cidades N = 10
% 1  - UEL, Londrina
% 2  - Ibiporã               ; Raio de 20km
% 3  - Maringá               ; Raio de 40km
% 4  - Cascavel              ; Raio de 80km
% 5  - Paranagua             ; Raio maior que 160km
% 6  - Pérola
% 7  - Palmas
% 8  - Brasilandia do Sul
% 9  - Sengés
% 10 - Santo Antonio do Sudoeste

DistMatriz = [0      21     98      378     485     309     525     319     308     534;
              21     0      111     391     498     322     538     332     285     547;
              98     111    0       283     523     212     508     222     399     439;
              378    391    283     0       603     171     310     106     556     163;
              485    498    523     603     0       693     450     697     371     657; 
              309    322    212     171     693     0       497     63      638     327;
              525    538    508     310     450     497     0       409     493     221;
              319    332    222     106     697     63      409     0       648     262;
              308    285    399     556     371     638     493     648     0       622;
              534    547    439     163     657     327     221     262     622     0];


numCidades = 10;

%indices
tam_Pop_ini = 10;              %Tamanho População Inicial
tam_gera    = 100;            %Nmr de gerações

% Gere a população inicial contendo todas as cidades, mas em ordem aleatória
Populacao = zeros(tam_Pop_ini, numCidades+1); % +1 para incluir a cidade de origem no fim da rota

%Geracao da Populacao Inicial
for k = 1:tam_Pop_ini
    
    % Gera um vetor de cidades (exceto a cidade de origem) em ordem aleatória
    cidades_aleatorias = randperm(numCidades-1) + 1;
    
    % Cria o cromossomo (rota) com a cidade de origem no início e fim
    Populacao(k, :) = [1, cidades_aleatorias, 1];


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
        [a b] = sort(rand(1,9));
        b = b + 1;

        FilhosPai(k, :) = Pai;
        FilhosPai(k, b(1, 1)) = Pai(1, b(1, 2));
        FilhosPai(k, b(1, 2)) = Pai(1, b(1, 1));
    end

    %Sorteia e permuta as duas posicoes da Mae
    for k = 1:4,
        clear a b;
        [a b] = sort(rand(1,9));
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







