%clc 
clear all
tic

% Dados Cidades N = 10
% 1  - UEL, Londrina
% 2  - Ibiporã               
% 3  - Maringá               
% 4  - Cascavel              
% 5  - Paranagua             
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
        Rota_menor = rota;
    end
    if distancia > distanciamaior
        distanciamaior = distancia;
        Indice_Rota_maior = i;
        Rota_maior = rota;
    end

end

% Exibi as distâncias
disp(['A distância total da menor rota é e a rota é a:']);
distanciamenor
Indice_Rota_menor
Rota_menor
disp(['A distância total da maior rota ée a rota é a:']);
distanciamaior
Indice_Rota_maior
Rota_maior


toc























