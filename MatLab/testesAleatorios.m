clear all;
clc;
tic

%% Dados Cidades N = 5
% 1 - Londrina
% 2 - Ibiporã               ; Raio de 20km
% 3 - Maringá               ; Raio de 40km
% 4 - Cascavel              ; Raio de 80km
% 5 - Paranagua             ; Raio maior que 160km

% Distâncias em km
DistMatriz = [0     20.2    97.4    378     485;
              20.2    0     111     391     498;
              97.4   111     0      283     523;
              378    391    283     0       603;
              485    498    523     603     0  ];

% Vetor de índices das cidades
VetorIndi = [1 2 3 4 5];

% Permutação dos índices
Pi = perms(VetorIndi);

% Matriz de distâncias para cada rota
Distancias = pdist(DistMatriz(Pi, :));

% Encontra a menor distância e sua respectiva rota
[distanciamenor, Indice_Rota_menor] = min(Distancias);
Rota_menor = Pi(Indice_Rota_menor, :);

% Encontra a maior distância e sua respectiva rota
[distanciamaior, Indice_Rota_maior] = max(Distancias);
Rota_maior = Pi(Indice_Rota_maior, :);

% Exibe as distâncias e rotas
disp(['A distância total da menor rota é ' num2str(distanciamenor) ' e a rota é:']);
disp(Rota_menor);
disp(['A distância total da maior rota é ' num2str(distanciamaior) ' e a rota é:']);
disp(Rota_maior);
toc