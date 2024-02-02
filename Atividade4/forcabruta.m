

function FB_func = forcabruta(MatrizDistTrab)

tempoFB = tic;
DistMatriz = MatrizDistTrab;

VetorIndi = 1:size(DistMatriz, 1);

% Permutação dos índices das cidades
Pi = perms(VetorIndi(2:end));

% Adicionar a cidade de partida no início de cada permutação
Pi = [ones(size(Pi, 1), 1), Pi, ones(size(Pi, 1), 1)];

% Variavel da Distancia
distanciamenor  = inf;
distanciamaior = 0;

% Calculo da rota
VetorDistancias = zeros(length(Pi),1);
Indice_Rota_menor = 0;
Indice_Rota_maior = 0;

for i = 1:length(Pi)
    rota = Pi(i, :); % Armazena a rota atual
    distancia   = 0;
    
    for j = 1:length(rota)   
        Cidade_partida = rota(j);
        Cidade_chegada = rota(mod(j, length(rota)) + 1);
        distancia = distancia + DistMatriz(Cidade_partida, Cidade_chegada);
    end

    % Armazenador de distancias
    VetorDistancias(i,1) = distancia;

    % Comparadores
    if distancia < distanciamenor
        distanciamenor = distancia;
        Indice_Rota_menor = i;
    end
    if distancia > distanciamaior
        distanciamaior = distancia;
        Indice_Rota_maior = i;
    end

end

% Obtém a rota com menor distância (desconsiderando a cidade de partida duplicada)
Rota_menor = Pi(Indice_Rota_menor, :);

% Obtém a rota com maior distância (desconsiderando a cidade de partida duplicada)
Rota_maior = Pi(Indice_Rota_maior, :);
tempoFB = toc(tempoFB);
% Preparando a saída da função
FB_func.distanciamenor = distanciamenor;
FB_func.Indice_Rota_menor = Indice_Rota_menor;
FB_func.Rota_menor = Rota_menor;
FB_func.distanciamaior = distanciamaior;
FB_func.Indice_Rota_maior = Indice_Rota_maior;
FB_func.Rota_maior = Rota_maior;
FB_func.tempoFB = tempoFB;
% % Exibi as distâncias
% disp(['A distância total da menor rota é e a rota é a:']);
% distanciamenor
% Indice_Rota_menor
% Rota_menor
% disp(['A distância total da maior rota ée a rota é a:']);
% distanciamaior
% Indice_Rota_maior
% Rota_maior



end






