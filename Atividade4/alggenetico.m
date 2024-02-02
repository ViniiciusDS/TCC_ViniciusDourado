

function AG_Func = alggenetico(MatrizDistTrab,tam_Pop_ini,tam_gera)

tempoAG = tic;
DistMatriz = MatrizDistTrab;

numCidades = length(DistMatriz);

%   Alocação de variaveis para aumentar a velocidade
Populacao = zeros(tam_Pop_ini, (numCidades+1));
FilhosPai = zeros(4, (numCidades+1));
FilhosMae = zeros(4, (numCidades+1));
nmr_filhos = zeros((tam_Pop_ini-2),(numCidades+1));

% Gere a população inicial contendo todas as cidades, mas em ordem aleatória
Percurso = zeros(tam_Pop_ini, numCidades+1); % +1 para incluir a cidade de origem no fim da rota

%Geracao da Populacao Inicial
for k = 1:tam_Pop_ini
    
    % Gera um vetor de cidades (exceto a cidade de origem) em ordem aleatória
    cidades_aleatorias = randperm(numCidades-1) + 1;
    
    % Cria o cromossomo (rota) com a cidade de origem no início e fim
    Populacao(k, :) = [1, cidades_aleatorias, 1];


end


for g = 1:tam_gera
    

    %Calcula o percurso total de cada vetor solucao
    for k = 1:size(Populacao,1)
        Percurso(k, g) = Calc_Dist(DistMatriz, Populacao(k,:));
    end

    %Escolhe os mais aptos 
    clear a b;
    [a, b] = sort(Percurso(:,g));
    
    % Recupera a menor distância encontrada
    menorDistancia = a(1);

    % Recupera a melhor rota encontrada
    melhorRota = Populacao(b(1,1), :);

    Pai = Populacao(b(1,1), :);
    Mae = Populacao(b(2,1), :);

    %   Calcula o Nmr de filhos
    num_filhos = size(nmr_filhos,1);
    
    if rem(num_filhos, 2) == 0
        %   Número de filhos é par, logo ambos possuem a mesma quantidade
        palim = num_filhos/2;
        malim = num_filhos/2;

    else
        %   Número de filhos é impar, logo sortea um genitor para ter mais
        %   filhos
        escolha = randi([1,2]);

        if escolha == 1
            %   Pai com mais filhos
            palim = (num_filhos + 1) / 2;
            malim = (num_filhos - 1) / 2;
        
        else
            %   Mae com mais filhos
            palim = (num_filhos - 1) / 2;
            malim = (num_filhos + 1) / 2;
        end    
    end

    %Cada Genitor vai gerar 2 filhos por permuta
    %Sorteia e permuta as duas posicoes do Pai
    for pa = 1:palim
        clear a b;
        [~, b] = sort(rand(2,numCidades));
        %b = b + 1;

        FilhosPai(pa, :) = Pai;
        FilhosPai(pa, b(1, 1)) = Pai(1, b(1, 2));
        FilhosPai(pa, b(1, 2)) = Pai(1, b(1, 1));
    end

    %Sorteia e permuta as duas posicoes da Mae
    for ma = 1:malim
        clear a b;
        [~, b] = sort(rand(2,numCidades));
        %b = b + 1;

        FilhosMae(ma, :) = Mae;
        FilhosMae(ma, b(1, 1)) = Mae(1, b(1, 2));
        FilhosMae(ma, b(1, 2)) = Mae(1, b(1, 1));
    end


    %Atualiza a Populacao
    Populacao = [Pai; Mae; FilhosPai; FilhosMae];
  
end

tempoAG = toc(tempoAG);
%plot(min(Percurso, [], 1));


% Preparando a saída da função
AG_Func.tempoAG = tempoAG;
AG_Func.menorDistancia = menorDistancia;
AG_Func.melhorRota = melhorRota;







end











